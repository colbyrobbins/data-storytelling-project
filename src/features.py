"""
features.py

Feature engineering on the cleaned dataset in data/processed/. Adds any
derived columns/aggregations used in the analysis and re-saves the result.

TODO: once preprocessing.py is in place, implement load_processed(),
engineer_features(), and save() below.
"""
import pandas as pd
from pathlib import Path

PROCESSED_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"


def load_processed_calls(filename="dpd_calls_2025_cleaned.csv"):
    """Read the cleaned dataset."""
    filepath = PROCESSED_DIR / filename
    df = pd.read_csv(filepath, parse_dates=['datetime'])

    # Recast dtypes lost on CSV round-trip
    for col in ['Nature', 'District', 'Disposition']:
        df[col] = df[col].astype('category')

    return df


def engineer_features_calls(df):
    """Add engineered features to the dataframe."""
    df = df.copy()

    # Time-based features
    df['hour'] = df['datetime'].dt.hour
    df['day_of_week'] = df['datetime'].dt.day_name()
    df['month'] = df['datetime'].dt.to_period('M')
    df['date'] = df['datetime'].dt.date

    # Report outcome categorization
    crime_report = ['Incident Report', 'CIT - Incident Report']
    other_report = ['Accident Report', 'Property Report']

    def categorize_disposition(d):
        if d in crime_report:
            return 'Crime Report'
        elif d in other_report:
            return 'Other Report'
        else:
            return 'No Report'

    df['report_category'] = df['Disposition'].apply(categorize_disposition)
    df['resulted_in_report'] = df['report_category'] == 'Crime Report'
    df['filed_report'] = df['report_category'].isin(['Crime Report', 'Other Report'])

    return df


def save_features_calls(df, filename="dpd_calls_2025_features.csv"):
    """Write the feature-engineered dataframe to PROCESSED_DIR."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / filename, index=False)


def main():
    df = load_processed_calls()
    df = engineer_features_calls(df)
    save_features_calls(df)


if __name__ == "__main__":
    main()
