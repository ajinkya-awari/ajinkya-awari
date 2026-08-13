# Animated GitHub Profile README — Design Specification

Date: 2026-08-13
Status: Approved direction; implementation pending final spec review
Owner: Ajinkya Avinash Awari
Target repository: `ajinkya-awari/ajinkya-awari` (public GitHub profile repository)

## Problem and outcome

The GitHub account has strong technical projects but no profile README. A concise, credible landing page should make the research/engineering narrative obvious within one screen, point visitors to the strongest work, and remain maintainable without third-party statistics widgets or a personal access token stored in the repository.

The outcome is a public profile repository whose `README.md` is human-first and whose visual assets provide an article-inspired terminal aesthetic: a small animated monogram/ASCII panel, a neofetch-style information card, and a locally rendered contribution heatmap. The profile must still be useful when the scheduled refresh cannot reach GitHub.

## Goals

1. Establish a polished public profile README for `ajinkya-awari`.
2. Present a precise positioning statement: ML engineer and published researcher building reliable learning systems.
3. Feature only verified public projects, with `solomonoff-bench` as the research flagship and links to complementary ML/RL/XAI work.
4. Use local SVG assets that render through normal GitHub Markdown image embeds; do not depend on JavaScript, external stats cards, or badge farms.
5. Refresh the contribution heatmap daily through GitHub Actions using the repository-scoped built-in `GITHUB_TOKEN` only.
6. Preserve the last known-good generated heatmap if the public contribution page is unavailable or malformed.
7. Make generated output deterministic and testable so changes are reviewable.
8. Keep the implementation privacy-safe: no personal photograph, email, PAT, or private-repository metadata in the public repository.

## Non-goals

- No edits, commits, pushes, or generated files in `E:/application/MS CS/solomonoff-bench` (Project 00).
- No changes to any existing project repository.
- No Kaggle benchmark execution or Zenodo record changes.
- No JavaScript, embedded tracking, external statistics services, or token-based contribution API calls.
- No claim that the heatmap is a complete activity/research metric; it visualizes GitHub's public contribution calendar only.
- No personal photo until the owner explicitly supplies and approves one.

## User experience and content

The README opens with a centered terminal block and then a short, readable profile:

- one-line identity and current focus;
- a compact “what I build” paragraph;
- links for GitHub, LinkedIn, email/contact (only if explicitly supplied), and publications;
- “Selected work” table with verified repository links and one-line outcomes;
- research interests and a brief “currently exploring” line;
- the generated contribution heatmap and a small maintenance note.

Visual copy must be factual and modest. Existing profile facts may be used only when visible on the public GitHub profile or repository README. Avoid unsupported user counts, rankings, or model-performance claims.

## Visual system

- Background: terminal near-black (`#0d1117`-family) with high-contrast text.
- Accent: restrained green/teal terminal palette; accessible contrast for body text.
- Typography: system monospace inside SVGs; normal GitHub-rendered Markdown outside SVGs.
- Layout: responsive Markdown with a centered header and a two-column table only where it remains readable on narrow screens.
- Motion: subtle SVG SMIL/CSS animation (cursor blink, staggered line reveal, heatmap shimmer). Respect `prefers-reduced-motion` where supported; animations must not carry semantic information.
- Assets: `assets/ascii-portrait.svg`, `assets/info-card.svg`, `assets/contrib-heatmap.svg`. The portrait is an abstract `AA` monogram/terminal silhouette, not an image of a person.

## Data and refresh architecture

The refresh script fetches `https://github.com/users/ajinkya-awari/contributions` as public HTML, parses contribution day cells, validates the date/value ranges, and writes a deterministic SVG. It must:

- use a bounded timeout, a descriptive user agent, and retry/backoff limits;
- reject unexpected HTML, missing cells, impossible dates, or excessive cell counts;
- write to a temporary file and atomically replace the SVG only after validation;
- return a non-zero status without deleting the previous valid SVG on failure;
- record a machine-readable generation timestamp/source note without nondeterministic layout changes;
- avoid logging response bodies, credentials, or private repository data.

The workflow runs on a daily cron plus `workflow_dispatch`. It has only `contents: write` permission, does not run on its own generated commits, and uses a path/file-change check before committing. Actions should be pinned to reviewed commit SHAs where practical.

## Proposed repository layout

```text
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
requirements.txt
pyproject.toml
assets/
  ascii-portrait.svg
  info-card.svg
  contrib-heatmap.svg
scripts/
  generate_heatmap.py
  render_profile_assets.py
src/profile_assets/
  __init__.py
  heatmap.py
tests/
  test_heatmap_parser.py
  test_svg_generation.py
  test_workflow_contract.py
.github/workflows/refresh-profile.yml
docs/superpowers/specs/2026-08-13-animated-github-profile-design.md
docs/superpowers/plans/<implementation-plan>.md
```

The exact package split may be simplified if tests and separation of concerns remain clear; generated assets must remain easy to locate.

## Safety and maintenance controls

- Public repository contains no secrets and includes a secret-scanning-friendly `.gitignore`.
- Workflow uses the ephemeral Actions token; no personal PAT is placed in YAML, code, or repository secrets for this feature.
- Network failure is a normal, tested state. The workflow must leave a valid existing heatmap untouched and report the failure clearly.
- SVG text is escaped; parsed dates and counts are range-checked to prevent malformed markup.
- Dependencies are minimal and pinned/upper-bounded where practical; test and runtime dependencies are explicit.
- README links are checked for correct repository names and HTTPS URLs before publication.
- A license is included so reuse expectations are explicit.

## Acceptance criteria

1. `README.md` renders using only repository-local assets and standard GitHub Markdown/HTML.
2. The README contains no JavaScript, external analytics, external stats widgets, PATs, or private-repository references.
3. Every featured repository link resolves to an existing public `ajinkya-awari` repository and its description is accurate.
4. `ascii-portrait.svg`, `info-card.svg`, and `contrib-heatmap.svg` are valid SVG/XML and render without external requests.
5. The heatmap parser handles valid public contribution HTML and rejects malformed/ambiguous input.
6. Two runs over identical fixture HTML produce byte-identical SVG output apart from an explicitly isolated, documented timestamp field (preferably no timestamp in the SVG).
7. A fetch/parse failure leaves the previous valid heatmap file byte-identical and exits non-zero.
8. The workflow is cron + manual dispatch, has least-privilege `contents: write`, avoids self-trigger loops, and does not expose secrets.
9. Tests cover parser validation, deterministic SVG output, failure preservation, XML escaping, and workflow permissions/triggers.
10. `pytest` and the script’s offline fixture mode pass from a clean checkout.
11. A local `git diff --check` and link/content audit pass before publication.
12. No file under `E:/application/MS CS/solomonoff-bench` changes; this is verified with a before/after status/hash check.

## Alternatives considered

### Static README only

Lowest maintenance risk, but it misses the requested article-inspired visual identity and gives the profile less visual distinction.

### External stats/typing widgets

Rejected because they add outages, privacy/tracking, supply-chain, and availability risk to a public profile.

### Personal photo in the animated portrait

Deferred. It increases privacy and asset-management concerns without improving the initial technical signal; the abstract monogram is distinctive and safe.

## Review checklist

- [x] User approved the terminal-style animated SVG direction.
- [x] Project 00 isolation is explicit.
- [x] Article-inspired features are adapted without copying an identity/photo.
- [x] Failure preservation and secret hygiene are first-class requirements.
- [ ] User reviews this written specification before implementation begins.
