# Raw Data

Put the original, unmodified dataset(s) here exactly as downloaded from the source.

Once a dataset is chosen, add:

- **Source & citation** — where it came from and how to cite it (link to the README's Dataset section too).
- **Date retrieved.**
- **Any access steps** — if the file is too large or restricted to commit to GitHub (e.g. over ~100MB, or behind an API key/login), don't commit it. Instead, document here exactly how a teammate (or grader) can obtain or regenerate it — a download link, an API + script, or a small sample file plus instructions for the full set.

Do not edit files in this folder by hand — all cleaning happens in `src/preprocessing.py` and writes to `data/processed/`.
