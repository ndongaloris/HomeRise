import pandas as pd

def validate_columns(df, required_cols):
    """Ensure all required columns are present."""
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

def clean_data(df):
    """Clean and prepare the housing dataset."""
    required_cols = [
        "Rent Price Per Month", "Type Of Development", "Typology",
        "Year Completed", "Year Started", "Location",
        "Latitude", "Longitude", "Project Status"
    ]
    validate_columns(df, required_cols)

    df = df.dropna(subset=required_cols)

    # Convert years
    df["Year Started"] = pd.to_datetime(df["Year Started"], errors="coerce").dt.year
    df["Year Completed"] = pd.to_datetime(df["Year Completed"], errors="coerce").dt.year

    # Calculate duration
    df["Duration"] = df["Year Completed"] - df["Year Started"]

    # Convert rent price
    df["Price"] = pd.to_numeric(df["Rent Price Per Month"], errors="coerce")

    # Drop rows with failed conversions
    df = df.dropna(subset=["Price", "Year Completed", "Year Started", "Latitude", "Longitude"])

    return df

def filter_data(df, dev_type=None, typology=None, year_range=None, status=None):
    """Apply filters based on user selections."""
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
    """Return basic statistics for dashboard display."""
    return {
        "Total Projects": len(df),
        "Average Rent": round(df["Price"].mean(), 2),
        "Average Duration": round(df["Duration"].mean(), 1),
        "Year Range": (df["Year Completed"].min(), df["Year Completed"].max()),
        "Unique Locations": df["Location"].nunique()
    }

def group_by_typology(df):
    """Return count of projects per typology."""
    return df["Typology"].value_counts()

def group_by_developer(df):
    """Return number of projects per developer."""
    return df["Developer Name"].value_counts()
