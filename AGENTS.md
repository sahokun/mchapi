# mchapi

<!-- Working rules for this repository, for both AI agents (Claude Code, Codex, etc.) and people.
     Rewrite the "Project-specific" section per project; keep the "Common rules" section identical across all of sahokun's repositories. -->

## Project-specific

### Overview

A Python wrapper for the My Crypto Heroes API (https://my-crypto-heroes.gitbook.io/mch-api/).

### Tech stack and layout

- Python package `mchapi`, installable with `setup.py`.
  - `mchapi/mch/`: game API models and calls.
  - `mchapi/eth/`: Ethereum-related models.
  - `mchapi/metadata/`: metadata API models.
  - `mchapi/enum.py`, `mchapi/util.py`: shared enums and helpers.
- Dependencies are listed in `requirements.txt` (`requests`, `bs4`, `pytz`).

### Verification

```bash
pip install -r requirements.txt
python -m unittest discover -s tests -p "*_test.py"
```

- The tests in `tests/` call the live API, so they need network access.

## Common rules

### Branches and PRs

<!-- branch-model:begin -->
- The default branch is `main`. Work on a branch and open a PR into `main`.
- PRs are squash-merged. Each PR leaves a single commit on main, titled with the PR title only.
<!-- branch-model:end -->
- Write PR titles in Conventional Commits form (`feat: ...`, `fix: ...`, etc.) so the change is clear from one line.
- Merged branches are deleted automatically.

### Never put these in history or anything published

- Do not write email addresses, tokens, passwords, details of a personal environment, or links to AI agent sessions in commits, PRs, issues, or comments.
  - Work-branch commits and PRs stay on GitHub after merging, and even the owner cannot delete them. Rewriting main's history needs a force push and a request to GitHub Support. Only PR descriptions can be fixed later by editing.
- Commit with your GitHub noreply address (`<ID>+<username>@users.noreply.github.com`) as the author email.
- Do not commit `.env`, key files, or local settings (`.claude/settings.local.json`, etc.).

### Dependencies

- Only add or update to versions published at least 7 days ago. Hijacked or swapped releases are often discovered shortly after publication.
  - Dependabot version updates wait 7 days via `cooldown`. For npm, `min-release-age=7` in `.npmrc` applies the same limit to manual updates.
- Pin GitHub Actions to a full 40-character commit SHA and keep the version as a trailing comment (e.g. `actions/checkout@<SHA> # v7.0.1`). Tags can be moved.
- Treat Dependabot PRs as a signal that updates exist. Merge them once CI passes, and for major updates, after reviewing the changes.
