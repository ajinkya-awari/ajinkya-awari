# Animated GitHub Profile README — Implementation Plan

> **Execution note:** Work only in `E:/application/MS CS/ajinkya-awari-profile`. Do not read/write/commit/push `E:/application/MS CS/solomonoff-bench`.

**Goal:** Create and publish a privacy-safe, terminal-style GitHub profile README for `ajinkya-awari` with deterministic local SVG assets and a resilient daily contribution-heatmap refresh.

**Architecture:** A small Python package owns parsing, validation, escaping, and deterministic SVG rendering. Offline fixtures drive tests. Checked-in SVGs are the README’s only visual dependencies. A least-privilege GitHub Actions workflow refreshes the heatmap with the built-in repository token and preserves the last valid asset on network/parser failure.

## Task 1 — Repository and policy foundation

Files: `.gitignore`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `pyproject.toml`, `requirements.txt`, package/test directories.

- Initialize a new local Git repository in the profile workspace.
- Add a permissive license with the owner’s name and current year.
- Ignore Python caches, virtual environments, local secrets, and generated temporary files; do not ignore the checked-in SVG assets.
- Define a minimal Python 3.11+ package and test dependencies with bounded versions.
- Document contribution expectations and security reporting without exposing contact details that were not supplied.
- Add a `src/profile_assets` package and `tests` package with no network calls at import time.

Verification: `git status --short`, `python --version`, `python -m pytest --collect-only` (after tests exist), and a secret-pattern scan over tracked candidate files.

## Task 2 — Heatmap parser and renderer (agent-owned)

Files: `src/profile_assets/heatmap.py`, `scripts/generate_heatmap.py`, fixture files, parser/renderer tests.

- Parse only the public contribution day-cell contract (`data-date`, `data-level` and/or `data-count`); reject missing attributes, invalid ISO dates, non-integer counts, levels outside 0–4, duplicate dates, and implausible cell counts.
- Keep the parser pure and fixture-testable. Use a bounded `requests.Session` in the CLI with a clear User-Agent, timeout, limited retries, and no credential headers.
- Render deterministic SVG: fixed dimensions/viewBox, stable ordering by date, escaped text/attributes, accessible title/description, green terminal palette, and subtle non-semantic animation.
- Write through a sibling temporary file and `os.replace` only after the complete output parses as XML; on fetch/parse/write failure, leave the existing output byte-identical and return non-zero.
- Support `--input-html` for offline generation and `--output` for tests/workflow.

Verification: parser valid/invalid fixtures, XML parse, byte-identical repeated rendering, output-preservation failure test, and CLI offline fixture run.

## Task 3 — Profile SVG assets (agent-owned)

Files: `assets/ascii-portrait.svg`, `assets/info-card.svg`, `assets/contrib-heatmap.svg`.

- Create a privacy-safe abstract `AA` terminal portrait with escaped text, no external fonts/images, and reduced-motion-friendly animation.
- Create a neofetch-style info card using only verified public facts: ML Engineer, published researcher, Python/PyTorch/TensorFlow, Pune, and selected project themes. Avoid unsupported metrics.
- Generate the initial heatmap from a checked-in fixture using the renderer; keep the asset valid even if the network is unavailable.
- Ensure all SVGs are self-contained, XML-valid, readable at their README display sizes, and free of scripts/external URLs.

Verification: XML parser, `rg` for `<script`, external `http`, data URI, and secret patterns; visual dimensions/viewBox sanity checks.

## Task 4 — README content and links (agent-owned)

Files: `README.md`.

- Build a concise terminal opening with local SVG image embeds and a no-JavaScript fallback alt text.
- Add human-first positioning, research interests, selected public projects, and contact/profile links only when verified.
- Feature `solomonoff-bench` as the research flagship without claiming unverified benchmark scope; include complementary public repositories with accurate one-line descriptions.
- Explain that the heatmap is GitHub’s public contribution calendar and may be stale when refresh is unavailable.
- Use accessible headings, descriptive alt text, HTTPS links, and mobile-tolerant Markdown; avoid external widgets and tracking.

Verification: link audit against public GitHub API, Markdown text scan for unsupported claims/secrets, and local asset-reference check.

## Task 5 — Scheduled refresh workflow (agent-owned)

Files: `.github/workflows/refresh-profile.yml`, optional workflow contract tests.

- Trigger on daily cron and `workflow_dispatch`; do not trigger on pushes to avoid self-looping generated commits.
- Set only `permissions: contents: write`; run on a current Ubuntu runner with pinned/reviewed action SHAs where practical.
- Install the package/dependencies, run the offline-safe generator against the public contributions URL, and commit only when `assets/contrib-heatmap.svg` changes.
- Use the ephemeral `${{ github.token }}` through the checkout/commit action; never reference the personal PAT.
- Ensure a failed fetch/parser exits clearly and does not overwrite the last valid asset.

Verification: YAML parse, exact trigger/permission assertions, no PAT-like strings, and a dry-run script invocation.

## Task 6 — Integration tests and quality gates

Files: `tests/test_workflow_contract.py`, `tests/test_profile_contract.py`, updates to existing tests.

- Validate every local SVG referenced by README exists and is XML-valid.
- Assert README has no external stats widgets, scripts, private-repository names, or credential-like values.
- Assert parser/rendering determinism and failure preservation.
- Assert workflow has manual/daily triggers, `contents: write`, no push trigger, and no secret other than the built-in token.
- Run `python -m pytest -q`, `python -m pytest tests/test_heatmap_parser.py -q`, `python -m compileall src scripts`, `git diff --check`, and a tracked-file secret scan.

## Task 7 — GitHub publication (only after local verification)

- Confirm Project 00’s pre-existing status/hash remains unchanged.
- Create public repository `ajinkya-awari/ajinkya-awari` only if it does not already exist, with issues/projects/wiki disabled unless needed.
- Commit the profile repository locally with a clear message; inspect the diff and commit contents.
- Push using a short-lived credential mechanism that never places the PAT in command arguments, files committed to the repo, or logs. Do not touch Project 00.
- Verify the remote repository, profile README rendering, workflow file, and default-branch status using read-only API checks.

## Final verification report

Before claiming completion, record command outputs for:

1. full and focused pytest;
2. SVG/XML and README contract checks;
3. workflow YAML/permission checks;
4. `git diff --check` and secret scan;
5. Project 00 isolation status/hash check;
6. remote repository/profile README visibility after publication.

If publication fails, leave the local repository intact, report the exact blocker, and do not retry with broader permissions or touch Project 00.
