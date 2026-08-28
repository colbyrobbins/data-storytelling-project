"""
eda.py

Exploratory data analysis: generates the charts behind our key findings
and saves them to reports/figures/ for use in the write-up and slides.

TODO: once features.py is in place, implement load_data() and add one
function per chart/finding below.
"""

from pathlib import Path

PROCESSED_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"
FIGURES_DIR = Path(__file__).resolve().parent.parent / "reports" / "figures"


def load_data(filename="features.csv"):
    """Read the feature-engineered dataset. TODO: implement."""
    raise NotImplementedError


def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    df = load_data()
    # TODO: add EDA charts here, e.g.:
    # plot_trend_over_time(df)
    # plot_top_categories(df)


if __name__ == "__main__":
    main()
