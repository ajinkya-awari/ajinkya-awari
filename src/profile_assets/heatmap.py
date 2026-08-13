"""Parse GitHub's public contribution calendar and render a local SVG.

The parser deliberately accepts only the small public contract used by the
contribution calendar: a day element has ``data-date`` and at least one of
``data-level`` or ``data-count``.  It does not parse repository information,
scripts, or response text beyond those attributes.  This keeps the generated
profile asset independent from private GitHub data and makes it easy to test
against offline fixtures.
"""

from __future__ import annotations

import html
import os
import re
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

MAX_CONTRIBUTION_DAYS = 400
MAX_DAILY_COUNT = 100_000
SVG_WIDTH = 860
SVG_HEIGHT = 150
_DATE_PATTERN = re.compile(r"\A\d{4}-\d{2}-\d{2}\Z")
_INTEGER_PATTERN = re.compile(r"\A\d+\Z")


class ContributionParseError(ValueError):
    """Raised when input is not a safe, unambiguous contribution calendar."""


@dataclass(frozen=True, slots=True)
class ContributionDay:
    """One contribution calendar cell.

    ``count`` is optional because GitHub has exposed calendars containing
    only ``data-level`` in the past.  The level remains the rendering source;
    when a count is available it is retained for accessible labels.
    """

    day: date
    level: int
    count: int | None = None

    @property
    def date(self) -> date:
        """Compatibility alias for callers that use ``date`` as the field."""

        return self.day


class _DayCellParser(HTMLParser):
    """Collect raw day-cell attributes without interpreting arbitrary HTML."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.cells: list[dict[str, str | None]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {name.lower(): value for name, value in attrs}
        if "data-date" in attributes:
            self.cells.append(
                {
                    "data-date": attributes.get("data-date"),
                    "data-level": attributes.get("data-level"),
                    "data-count": attributes.get("data-count"),
                }
            )


def _strict_date(raw: str | None, index: int) -> date:
    if raw is None or not _DATE_PATTERN.fullmatch(raw):
        raise ContributionParseError(
            f"day cell {index} has an invalid ISO date (expected YYYY-MM-DD)"
        )
    try:
        return date.fromisoformat(raw)
    except ValueError as exc:
        raise ContributionParseError(f"day cell {index} has an invalid ISO date") from exc


def _strict_integer(raw: str, attribute: str, index: int) -> int:
    if not _INTEGER_PATTERN.fullmatch(raw):
        raise ContributionParseError(
            f"day cell {index} has a non-integer {attribute} attribute"
        )
    try:
        return int(raw)
    except ValueError as exc:  # pragma: no cover - guarded by the regex
        raise ContributionParseError(
            f"day cell {index} has a non-integer {attribute} attribute"
        ) from exc


def parse_contributions(document: str) -> tuple[ContributionDay, ...]:
    """Parse and validate contribution cells from public GitHub HTML.

    The output is sorted by date regardless of input order.  This is both
    useful for callers and a determinism guarantee for SVG generation.
    """

    if not isinstance(document, str) or not document.strip():
        raise ContributionParseError("contribution response is empty")

    parser = _DayCellParser()
    try:
        parser.feed(document)
        parser.close()
    except Exception as exc:  # HTMLParser can surface malformed input errors.
        raise ContributionParseError("contribution response is malformed HTML") from exc

    if not parser.cells:
        raise ContributionParseError("no contribution day cells were found")
    if len(parser.cells) > MAX_CONTRIBUTION_DAYS:
        raise ContributionParseError(
            f"implausible contribution cell count: {len(parser.cells)} "
            f"(maximum is {MAX_CONTRIBUTION_DAYS})"
        )

    parsed: list[ContributionDay] = []
    seen: set[date] = set()
    for index, cell in enumerate(parser.cells, start=1):
        current_date = _strict_date(cell.get("data-date"), index)
        if current_date in seen:
            raise ContributionParseError(f"duplicate contribution date: {current_date.isoformat()}")
        seen.add(current_date)

        raw_level = cell.get("data-level")
        raw_count = cell.get("data-count")
        if raw_level is None and raw_count is None:
            raise ContributionParseError(
                f"day cell {index} must contain data-level or data-count"
            )

        level: int
        if raw_level is None:
            # A count-only cell is supported for forward compatibility.  The
            # thresholds are intentionally documented and deterministic; the
            # exact count is retained separately for accessibility.
            count_for_level = _strict_integer(raw_count or "", "data-count", index)
            level = _level_from_count(count_for_level)
        else:
            level = _strict_integer(raw_level, "data-level", index)
            if level > 4:
                raise ContributionParseError(
                    f"day cell {index} has data-level outside 0-4: {level}"
                )

        count: int | None = None
        if raw_count is not None:
            count = _strict_integer(raw_count, "data-count", index)
            if count > MAX_DAILY_COUNT:
                raise ContributionParseError(
                    f"day cell {index} has implausible data-count: {count}"
                )

        parsed.append(ContributionDay(day=current_date, level=level, count=count))

    return tuple(sorted(parsed, key=lambda item: item.day))


def _level_from_count(count: int) -> int:
    """Map count-only cells to a stable display level.

    GitHub's level thresholds are presentation details and are not relied on
    for claims.  These conservative bins make old/count-only HTML useful
    without pretending that a count is already a level.
    """

    if count == 0:
        return 0
    if count <= 3:
        return 1
    if count <= 6:
        return 2
    if count <= 9:
        return 3
    return 4


def render_heatmap_svg(days: Iterable[ContributionDay]) -> str:
    """Render contribution days as deterministic, self-contained SVG.

    The SVG has a fixed canvas and stable date ordering.  No timestamp or
    network-derived value is included, so identical input produces identical
    bytes.  Animation is limited to a decorative cursor and has no semantic
    role in the chart.
    """

    ordered = tuple(sorted(days, key=lambda item: item.day))
    if not ordered:
        raise ContributionParseError("cannot render an empty contribution calendar")
    if len(ordered) > MAX_CONTRIBUTION_DAYS:
        raise ContributionParseError("too many contribution cells to render")
    if len({item.day for item in ordered}) != len(ordered):
        raise ContributionParseError("cannot render duplicate contribution dates")
    for item in ordered:
        if not 0 <= item.level <= 4:
            raise ContributionParseError(f"invalid rendering level: {item.level}")
        if item.count is not None and not 0 <= item.count <= MAX_DAILY_COUNT:
            raise ContributionParseError(f"invalid rendering count: {item.count}")

    first_day = ordered[0].day
    last_day = ordered[-1].day
    # Python weekday is Monday=0; the calendar starts on Sunday.
    first_sunday = first_day - timedelta(days=(first_day.weekday() + 1) % 7)
    last_saturday = last_day + timedelta(days=(5 - last_day.weekday()) % 7)
    week_count = ((last_saturday - first_sunday).days + 1) // 7
    if week_count > 53:
        # 53 is the fixed GitHub calendar width; a larger input is likely an
        # accidental page scrape rather than a single contribution calendar.
        raise ContributionParseError(f"calendar spans too many weeks: {week_count}")

    by_day = {item.day: item for item in ordered}
    colors = ("#161b22", "#0e4429", "#006d32", "#26a641", "#39d353")
    cell_size = 11
    gap = 3
    left = 24
    top = 38
    cell_parts: list[str] = []
    for offset in range((last_saturday - first_sunday).days + 1):
        current = first_sunday + timedelta(days=offset)
        item = by_day.get(current)
        if item is None:
            continue
        column = (current - first_sunday).days // 7
        row = (current - first_sunday).days % 7
        label_count = (
            f"{item.count} contributions" if item.count is not None else f"level {item.level}"
        )
        title = html.escape(
            f"{current.isoformat()}: {label_count}", quote=True
        )
        x = left + column * (cell_size + gap)
        y = top + row * (cell_size + gap)
        cell_parts.append(
            f'  <rect class="day level-{item.level}" x="{x}" y="{y}" '
            f'width="{cell_size}" height="{cell_size}" rx="2" '
            f'fill="{colors[item.level]}" aria-label="{title}">'
            f"<title>{title}</title></rect>"
        )

    range_label = html.escape(
        f"{first_day.isoformat()} to {last_day.isoformat()}", quote=True
    )
    description = html.escape(
        "Public GitHub contribution calendar; color intensity represents the "
        "reported contribution level.",
        quote=True,
    )
    cells = "\n".join(cell_parts)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" role="img" '
        f'aria-labelledby="heatmap-title heatmap-description" width="{SVG_WIDTH}" '
        f'height="{SVG_HEIGHT}" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}">\n'
        "  <title id=\"heatmap-title\">GitHub contribution heatmap</title>\n"
        f'  <desc id="heatmap-description">{description} {range_label}</desc>\n'
        '  <rect width="860" height="150" rx="10" fill="#0d1117"/>\n'
        '  <text x="24" y="24" fill="#7ee787" font-family="ui-monospace, SFMono-Regular, Consolas, monospace" font-size="12">'
        f"contributions · {range_label}</text>\n"
        f"{cells}\n"
        '  <rect x="805" y="18" width="7" height="7" rx="2" fill="#39d353" opacity="0.75">\n'
        '    <animate attributeName="opacity" values="0.35;0.9;0.35" dur="2.4s" repeatCount="indefinite"/>\n'
        "  </rect>\n"
        '  <style>@media (prefers-reduced-motion: reduce) { animate { display: none; } }</style>\n'
        "</svg>\n"
    )


def validate_svg(svg: str) -> None:
    """Raise ``ValueError`` unless *svg* is complete, well-formed XML."""

    try:
        root = ET.fromstring(svg)
    except ET.ParseError as exc:
        raise ValueError("generated heatmap is not valid XML") from exc
    if root.tag.rsplit("}", 1)[-1] != "svg":
        raise ValueError("generated output root is not SVG")


def atomic_write_svg(output: str | os.PathLike[str], svg: str) -> None:
    """Atomically replace *output* after validating complete SVG XML.

    Any failure removes only the sibling temporary file.  An existing output
    is never truncated or removed before ``os.replace`` succeeds.
    """

    validate_svg(svg)
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temp_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            prefix=f".{destination.name}.",
            suffix=".tmp",
            dir=destination.parent,
            delete=False,
        ) as temporary:
            temp_name = temporary.name
            temporary.write(svg)
            temporary.flush()
            os.fsync(temporary.fileno())
        # Parse the bytes as written, not merely the in-memory string.
        ET.parse(temp_name)
        os.replace(temp_name, destination)
        temp_name = None
    finally:
        if temp_name is not None:
            try:
                os.unlink(temp_name)
            except FileNotFoundError:
                pass
