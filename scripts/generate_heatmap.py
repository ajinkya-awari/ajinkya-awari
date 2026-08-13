#!/usr/bin/env python3
"""Generate the local profile contribution heatmap.

Use ``--input-html`` for deterministic offline generation and tests.  Without
it, only the public GitHub contribution page is fetched; no credential header
or personal access token is ever used.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:  # pragma: no cover - exercised only in an uninstalled checkout
    requests = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from profile_assets.heatmap import (  # noqa: E402
    ContributionParseError,
    atomic_write_svg,
    parse_contributions,
    render_heatmap_svg,
)

_USERNAME_PATTERN = re.compile(r"\A[A-Za-z0-9-]{1,39}\Z")
_MAX_RESPONSE_BYTES = 4_000_000


def _session() -> requests.Session:
    if requests is None:
        raise RuntimeError("requests is required for network generation; use --input-html offline")
    retry = Retry(
        total=2,
        connect=2,
        read=2,
        status=2,
        backoff_factor=0.25,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session = requests.Session()
    session.headers.update({"User-Agent": "ajinkya-awari-profile-heatmap/1.0"})
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def fetch_contributions(username: str, timeout: float = 10.0) -> str:
    """Fetch only the public contribution HTML with bounded network behavior."""

    if not _USERNAME_PATTERN.fullmatch(username):
        raise ValueError("username must contain only letters, digits, and hyphens")
    url = f"https://github.com/users/{username}/contributions"
    try:
        with _session() as session:
            response = session.get(url, timeout=(timeout, timeout))
            response.raise_for_status()
            content = response.content
    except requests.RequestException as exc:
        # Convert transport/HTTP failures into the same concise, non-secret
        # error path used by parser failures.  The CLI then exits non-zero
        # without printing a response body or traceback.
        raise ValueError(f"public contribution fetch failed: {exc}") from exc
    if len(content) > _MAX_RESPONSE_BYTES:
        raise ValueError("contribution response is unexpectedly large")
    return content.decode("utf-8", errors="strict")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", default="ajinkya-awari")
    parser.add_argument(
        "--input-html",
        type=Path,
        help="read a checked-in HTML fixture instead of making a network request",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "assets" / "contrib-heatmap.svg",
        help="destination SVG (default: assets/contrib-heatmap.svg)",
    )
    parser.add_argument("--timeout", type=float, default=10.0)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.input_html is not None:
            document = args.input_html.read_text(encoding="utf-8")
        else:
            document = fetch_contributions(args.username, timeout=args.timeout)
        days = parse_contributions(document)
        atomic_write_svg(args.output, render_heatmap_svg(days))
    except (OSError, ValueError, ContributionParseError, UnicodeError) as exc:
        print(f"heatmap generation failed: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {args.output} ({len(days)} contribution days)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
