from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET

import pytest

from profile_assets.heatmap import (
    ContributionParseError,
    atomic_write_svg,
    parse_contributions,
    render_heatmap_svg,
)


FIXTURES = Path(__file__).parent / "fixtures"


def fixture(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


def test_valid_fixture_is_sorted_and_preserves_contract_values() -> None:
    days = parse_contributions(fixture("contributions_valid.html"))

    assert [item.date.isoformat() for item in days] == [
        "2025-01-01",
        "2025-01-02",
        "2025-01-03",
        "2025-01-05",
        "2025-01-06",
    ]
    assert [(item.level, item.count) for item in days] == [
        (2, 5),
        (1, 1),
        (3, 8),
        (0, 0),
        (4, 42),
    ]


def test_count_only_fixture_gets_deterministic_display_levels() -> None:
    days = parse_contributions(fixture("contributions_count_only.html"))

    assert [(item.count, item.level) for item in days] == [(0, 0), (4, 2), (10, 4)]


@pytest.mark.parametrize(
    "name",
    [
        "contributions_missing_attributes.html",
        "contributions_duplicate_date.html",
        "contributions_invalid_level.html",
        "contributions_invalid_count.html",
    ],
)
def test_invalid_fixtures_are_rejected(name: str) -> None:
    with pytest.raises(ContributionParseError):
        parse_contributions(fixture(name))


@pytest.mark.parametrize(
    "document",
    [
        '<td data-date="2025-02-30" data-level="1"></td>',
        '<td data-date="2025-02-01" data-level="-1"></td>',
        '<td data-date="2025-02-01" data-level="1" data-count="-2"></td>',
        '<td data-date="2025-02-01" data-level="1" data-count="100001"></td>',
        "<main>no day cells</main>",
    ],
)
def test_parser_rejects_invalid_or_ambiguous_contract(document: str) -> None:
    with pytest.raises(ContributionParseError):
        parse_contributions(document)


def test_rendering_is_deterministic_and_xml_valid() -> None:
    days = parse_contributions(fixture("contributions_valid.html"))
    first = render_heatmap_svg(days)
    second = render_heatmap_svg(tuple(reversed(days)))

    assert first == second
    root = ET.fromstring(first)
    assert root.tag.endswith("svg")
    assert root.attrib["width"] == "860"
    assert root.attrib["height"] == "150"
    assert "<script" not in first.lower()
    assert "http://" in first  # only the SVG namespace, not an external asset


def test_atomic_write_preserves_existing_output_on_validation_failure(tmp_path: Path) -> None:
    output = tmp_path / "contrib-heatmap.svg"
    original = b"known-good-svg\n"
    output.write_bytes(original)

    with pytest.raises(ValueError):
        atomic_write_svg(output, "<svg>")

    assert output.read_bytes() == original
    assert list(tmp_path.glob(".*.tmp")) == []


def test_atomic_write_replaces_only_after_complete_xml(tmp_path: Path) -> None:
    output = tmp_path / "nested" / "contrib-heatmap.svg"
    svg = render_heatmap_svg(parse_contributions(fixture("contributions_valid.html")))

    atomic_write_svg(output, svg)

    assert output.read_text(encoding="utf-8") == svg
    ET.parse(output)
