"""
features.py

Feature engineering on the cleaned dataset in data/processed/. Adds any
derived columns/aggregations used in the analysis and re-saves the result.

TODO: once preprocessing.py is in place, implement load_processed(),
engineer_features(), and save() below.
"""

from pathlib import Path

PROCESSED_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"


def load_processed(filename="cleaned.csv"):
    """Read the cleaned dataset. TODO: implement."""
    raise NotImplementedError


def engineer_features(df):
    """Add engineered features to the dataframe. TODO: implement."""
    raise NotImplementedError


def save(df, filename="features.csv"):
    """Write the feature-engineered dataframe to PROCESSED_DIR."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / filename, index=False)


def main():
    df = load_processed()
    df = engineer_features(df)
    save(df)


if __name__ == "__main__":
    main()
