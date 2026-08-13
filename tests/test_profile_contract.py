from __future__ import annotations

from pathlib import Path
import re
import xml.etree.ElementTree as ET


ROOT = Path(__file__).parents[1]


def test_readme_references_only_local_visual_assets() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert 'src="assets/ascii-portrait.svg"' in readme
    assert 'src="assets/info-card.svg"' in readme
    assert 'src="assets/contrib-heatmap.svg"' in readme
    assert not re.search(r"<script|github-readme-stats|streak-stats|komarev|shields\.io", readme, re.I)
    assert not re.search(r"(?:ghp_|github_pat_|AKIA[0-9A-Z]{16})", readme)


def test_local_profile_svgs_are_well_formed_and_self_contained() -> None:
    for name in ("ascii-portrait.svg", "info-card.svg", "contrib-heatmap.svg"):
        path = ROOT / "assets" / name
        root = ET.parse(path).getroot()
        assert root.tag.endswith("svg")
        text = path.read_text(encoding="utf-8").lower()
        assert "<script" not in text
        # The SVG namespace is required XML metadata; no external image/font
        # request is allowed.
        assert "<image" not in text
        assert "@import" not in text


def test_profile_workflow_contract() -> None:
    workflow = (ROOT / ".github" / "workflows" / "refresh-profile.yml").read_text(
        encoding="utf-8"
    )
    assert 'cron: "17 6 * * *"' in workflow
    assert "workflow_dispatch:" in workflow
    assert "contents: write" in workflow
    assert "push:" not in workflow
    assert "github.token" not in workflow
    assert "secrets." not in workflow
    assert "actions/checkout@" in workflow and "actions/setup-python@" in workflow
