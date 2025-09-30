# 📦 Import pandas for powerful data manipulation and analysis
import pandas as pd

def validate_columns(df, required_cols):
    """Ensure all required columns are present in the DataFrame.

    Raises a ValueError if any expected column is missing.
    This helps catch schema mismatches early in the pipeline.
    """
    
    # 🔍 Identify any columns from required_cols that are missing in the DataFrame
    missing = [col for col in required_cols if col not in df.columns]
    
    # 🚨 Raise an error with a clear message if any required columns are missing
    if missing:
        raise ValueError(f"Missing columns: {missing}")

def clean_data(df):
    """Clean and prepare the housing dataset for analysis and visualization."""
    
    # 📋 Define the columns that must be present for meaningful analysis
    required_cols = [
        "Rent Price Per Month", "Type Of Development", "Typology",
        "Year Completed", "Year Started", "Location",
        "Latitude", "Longitude", "Project Status"
    ]
    
    # ✅ Validate that all required columns exist in the dataset
    validate_columns(df, required_cols)

    # 🧹 Drop rows with missing values in any of the required columns
    df = df.dropna(subset=required_cols)

    # 📆 Convert year columns to numeric year format (e.g., 2020)
    # - Handles both string and datetime formats
    # - Coerces invalid formats to NaT, which are dropped later
    df["Year Started"] = pd.to_datetime(df["Year Started"], errors="coerce").dt.year
    df["Year Completed"] = pd.to_datetime(df["Year Completed"], errors="coerce").dt.year

    # ⏳ Calculate project duration in years
    df["Duration"] = df["Year Completed"] - df["Year Started"]

    # 💰 Convert rent price to numeric format
    # - Handles strings with commas or currency symbols
    df["Price"] = pd.to_numeric(df["Rent Price Per Month"], errors="coerce")

    # 🧽 Drop rows with failed conversions or missing geolocation
    df = df.dropna(subset=["Price", "Year Completed", "Year Started", "Latitude", "Longitude"])

    # ✅ Return the cleaned DataFrame for downstream use
    return df

def filter_data(df, dev_type=None, typology=None, year_range=None, status=None):
    """Apply user-defined filters to the dataset.

    Parameters:
    - dev_type: Filter by development type (e.g., 'Public', 'Private')
    - typology: Filter by housing typology (e.g., 'Apartment', 'Duplex')
    - year_range: Tuple of (start_year, end_year) to filter by completion year
    - status: Filter by project status (e.g., 'Completed', 'Ongoing')

    Returns:
    - Filtered DataFrame
    """
    
    if dev_type:
        df = df[df["Type Of Development"] == dev_type]
    if typology:
        df = df[df["Typology"] == typology]
    if year_range:
        df = df[(df["Year Completed"] >= year_range[0]) & (df["Year Completed"] <= year_range[1])]
    if status:
        df = df[df["Project Status"] == status]
    
    return df

def get_summary_stats(df):
    """Generate key summary statistics for dashboard display.

    Returns:
    - Dictionary with total projects, average rent, average duration,
      year range, and number of unique locations.
    """
    
    return {
        "Total Projects": len(df),
        "Average Rent": round(df["Price"].mean(), 2),
        "Average Duration": round(df["Duration"].mean(), 1),
        "Year Range": (df["Year Completed"].min(), df["Year Completed"].max()),
        "Unique Locations": df["Location"].nunique()
    }

def group_by_typology(df):
    """Return count of projects per housing typology.

    Useful for bar charts and categorical breakdowns.
    """
    return df["Typology"].value_counts()

def group_by_developer(df):
    """Return number of projects per developer.

    Assumes 'Developer Name' column exists in the dataset.
    """
    return df["Developer Name"].value_counts()
