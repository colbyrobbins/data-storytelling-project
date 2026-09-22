"""
eda.py

Exploratory analysis on the feature-engineered dataset in data/processed/.
Reproduces the EDA charts from preliminary-eda-colby.ipynb and saves them
to FIGURES_DIR.
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import contextily as ctx

PROCESSED_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"
FIGURES_DIR = Path(__file__).resolve().parent.parent / "figures"

def show_info(df):
    """Print basic info about the dataframe."""
    print("DataFrame Info:")
    print(df.info())

def load_data_calls(filename="dpd_calls_2025_features.csv"):
    """Read the feature-engineered dataset."""
    filepath = PROCESSED_DIR / filename
    df = pd.read_csv(filepath, parse_dates=['datetime'])

    # Recast dtypes lost on CSV round-trip
    for col in ['Nature', 'District', 'Disposition']:
        df[col] = df[col].astype('category')
    df['month'] = df['month'].astype('period[M]')

    return df


def plot_calls_by_district(df):
    """Bar chart of call counts by district."""
    district_counts = df['District'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    district_counts.plot(kind='bar', color='steelblue')
    plt.title('Call Counts by District')
    plt.xlabel('District')
    plt.ylabel('Number of Calls')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'calls_by_district.png', dpi=150)
    plt.close()


def plot_call_density_by_priority(df):
    """Hexbin maps of call density, one panel per priority level, on a shared extent."""
    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df['X'], df['Y']),
        crs='EPSG:2264'
    ).to_crs(epsg=3857)

    gdf_valid = gdf.dropna(subset=['Priority'])
    priorities = sorted(gdf_valid['Priority'].unique())

    # Lock every panel to the SAME extent, taken from the full valid dataset —
    # this is what forces consistent zoom/area across all subplots
    xmin, ymin, xmax, ymax = gdf_valid.total_bounds
    pad_x = (xmax - xmin) * 0.05
    pad_y = (ymax - ymin) * 0.05
    xmin, xmax = xmin - pad_x, xmax + pad_x
    ymin, ymax = ymin - pad_y, ymax + pad_y

    ncols = 5
    nrows = -(-len(priorities) // ncols)  # ceil division

    fig, axes = plt.subplots(nrows, ncols, figsize=(28, 12))
    axes = axes.flatten()

    for ax, p in zip(axes, priorities):
        group = gdf_valid[gdf_valid['Priority'] == p]
        ax.hexbin(group.geometry.x, group.geometry.y, gridsize=40, cmap='inferno', mincnt=1)

        # Force identical extent on every panel — must be set BEFORE add_basemap
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)

        ctx.add_basemap(ax, source=ctx.providers.Esri.WorldStreetMap)
        ax.set_axis_off()
        ax.set_title(f'Priority {int(p)}', fontsize=10)

    for ax in axes[len(priorities):]:
        ax.axis('off')

    fig.suptitle('Call Density by Priority Rank (9 = highest urgency)', fontsize=14)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'call_density_by_priority.png', dpi=150)
    plt.close()


def plot_report_outcomes(df):
    """Pie chart of overall report outcome split, and stacked bar by district."""
    colors = {'Crime Report': 'indianred', 'Other Report': 'steelblue', 'No Report': 'lightgray'}

    # 1. Overall 3-part pie
    report_counts = df['report_category'].value_counts()

    plt.figure(figsize=(10, 10))
    plt.pie(
        report_counts,
        labels=report_counts.index,
        autopct='%1.1f%%',
        colors=[colors[c] for c in report_counts.index],
        startangle=90,
        textprops={'fontsize': 16} 
    )
    plt.title('Overall Split: Report Outcome of Calls for Service', fontsize=20, fontweight='bold')
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'report_outcome_pie.png', dpi=150)
    plt.close()

    # 2. Stacked bar by district — percentages
    district_pivot = pd.crosstab(df['District'], df['report_category'], normalize='index') * 100
    district_pivot = district_pivot[['Crime Report', 'Other Report', 'No Report']]  # consistent order

    ax = district_pivot.plot(
        kind='bar',
        stacked=True,
        figsize=(10, 6),
        color=[colors[c] for c in district_pivot.columns]
    )
    ax.set_title('Report Outcome by District (%)')
    ax.set_ylabel('Percentage of Calls')
    ax.set_xlabel('District')
    plt.xticks(rotation=0)
    plt.legend(title='Outcome', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'report_outcome_by_district.png', dpi=150)
    plt.close()


def plot_monthly_trends(df):
    """Monthly calls vs. reports filed, and monthly report rate."""
    monthly = df.groupby('month').agg(
        total_calls=('Disposition', 'count'),
        total_reports=('filed_report', 'sum')
    )

    # Calls vs. reports, log scale
    fig, ax = plt.subplots(figsize=(14, 8))
    monthly['total_calls'].plot(ax=ax, marker='o', label='Total Calls for Service', color='steelblue')
    monthly['total_reports'].plot(ax=ax, marker='o', label='Total Reports Filed', color='indianred')

    ax.set_yscale('log')
    ax.set_title('Calls for Service vs. Reports Filed, by Month (2025)', fontsize=20, fontweight='bold')
    ax.set_ylabel('Count (log scale)', fontsize=16)
    ax.set_xlabel('Month', fontsize=16)
    ax.tick_params(axis='both', labelsize=14)
    ax.legend(fontsize=14)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'monthly_calls_vs_reports.png', dpi=150)
    plt.close()

    # Report rate by month
    monthly['report_rate'] = monthly['total_reports'] / monthly['total_calls'] * 100

    fig, ax = plt.subplots(figsize=(14, 8))
    monthly['report_rate'].plot(ax=ax, marker='o', color='darkorange')
    ax.set_title('Report Rate by Month (2025)', fontsize=20, fontweight='bold')
    ax.set_ylabel('% of Calls Resulting in a Report', fontsize=16)
    ax.set_xlabel('Month', fontsize=16)
    ax.tick_params(axis='both', labelsize=14)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'monthly_report_rate.png', dpi=150)
    plt.close()


def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    df = load_data_calls()
    show_info(df)
    plot_calls_by_district(df)
    plot_call_density_by_priority(df)
    plot_report_outcomes(df)
    plot_monthly_trends(df)


if __name__ == "__main__":
    main()