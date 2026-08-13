from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET

from scripts.generate_heatmap import main


FIXTURE = Path(__file__).parent / "fixtures" / "contributions_valid.html"


def test_cli_offline_fixture_run_writes_valid_svg(tmp_path: Path) -> None:
    output = tmp_path / "contrib-heatmap.svg"

    assert main(["--input-html", str(FIXTURE), "--output", str(output)]) == 0
    root = ET.parse(output).getroot()
    assert root.tag.endswith("svg")


def test_cli_parse_failure_preserves_existing_output(tmp_path: Path) -> None:
    output = tmp_path / "contrib-heatmap.svg"
    original = b"existing-good-output"
    output.write_bytes(original)
    invalid = Path(__file__).parent / "fixtures" / "contributions_invalid_count.html"

    assert main(["--input-html", str(invalid), "--output", str(output)]) == 1
    assert output.read_bytes() == original
