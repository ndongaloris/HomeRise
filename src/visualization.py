import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_trends(df):
    """Line chart of rent price trends by year and location."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=df, x="Year Completed", y="Price", hue="Location", ax=ax)
    ax.set_title("Rent Price Trends by Location")
    ax.set_ylabel("Monthly Rent Price")
    ax.set_xlabel("Year Completed")
    ax.grid(True)
    return fig

def plot_typology_distribution(df):
    """Bar chart showing number of projects per typology."""
    fig, ax = plt.subplots(figsize=(8, 5))
    typology_counts = df["Typology"].value_counts()
    sns.barplot(x=typology_counts.index, y=typology_counts.values, ax=ax)
    ax.set_title("Distribution of Housing Typologies")
    ax.set_ylabel("Number of Projects")
    ax.set_xlabel("Typology")
    ax.tick_params(axis='x', rotation=45)
    return fig

def plot_price_by_development(df):
    """Boxplot comparing rent prices across development types."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x="Type Of Development", y="Price", ax=ax)
    ax.set_title("Rent Price by Development Type")
    ax.set_ylabel("Monthly Rent Price")
    ax.set_xlabel("Development Type")
    ax.tick_params(axis='x', rotation=45)
    return fig

def plot_project_timeline(df):
    """Histogram comparing project start vs completion years."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df["Year Started"], color="blue", label="Started", kde=False, bins=20)
    sns.histplot(df["Year Completed"], color="green", label="Completed", kde=False, bins=20)
    ax.set_title("Project Start vs Completion Timeline")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Projects")
    ax.legend()
    return fig

def plot_duration_distribution(df):
    """Histogram of project durations."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["Duration"], bins=15, color="purple", ax=ax)
    ax.set_title("Distribution of Project Durations")
    ax.set_xlabel("Duration (Years)")
    ax.set_ylabel("Number of Projects")
    return fig