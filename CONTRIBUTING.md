# Contributing

## Team Workflow

1. Pull the latest `main` branch.
2. Create a branch for your task.
3. Make and test your changes.
4. Commit with a clear, descriptive message.
5. Push your branch to GitHub.
6. Open a pull request describing what changed and why.
7. Request a review from your teammate.
8. Merge only after review.

Each of us needs at least one visible pull request over the course of the project — smaller, more frequent PRs are easier to review than one giant one at the end.

## Branch Names

Use a short, descriptive name for what the branch does, e.g.:

- `data-sourcing`
- `preprocessing`
- `eda-<topic>` (e.g. `eda-trends-by-region`)
- `feature-engineering`
- `viz-<chart-name>`
- `docs-readme`
- `fix-<short-description>`

## Commits & PRs

- Keep each pull request focused on one task or one piece of the analysis.
- Write brief, descriptive commit messages.
- In the PR description, note how you tested/verified the change (e.g. "ran `preprocessing.py` end to end, spot-checked 5 rows against the source").
- Pull the latest `main` before starting new work to avoid painful merge conflicts.

## Data & Secrets

- Do not commit `.env` files, API keys, or other secrets.
- `.venv/` and other environment/build artifacts are already covered by `.gitignore` — don't commit them.
- Raw and cleaned data belong in `data/raw/` and `data/processed/`. If a file is too large or restricted to commit (check GitHub's ~100MB hard limit), don't force-push it — document how to obtain/regenerate it in `data/raw/README.md` instead and leave the folder empty (or with a small sample).

## Code Style

- Put reusable/pipeline logic in `src/` scripts (`preprocessing.py`, `features.py`, `eda.py`)
- Notebooks in `notebooks/` are fine for exploration, but anything that needs to run to reproduce the analysis should end up as a script.
- Add a short docstring or comment at the top of new scripts/functions explaining what they do.
