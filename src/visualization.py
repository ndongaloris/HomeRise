# Importing essential visualization libraries
import matplotlib.pyplot as plt  # Core plotting library for creating figures and axes
import seaborn as sns            # High-level interface for attractive and informative statistical graphics

def plot_price_trends(df):
    """Line chart of rent price trends by year and location."""
    
    # Create a figure and axis object with a custom size for better readability
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot a line chart showing how rent prices evolve over time, differentiated by location
    # - x-axis: Year the project was completed
    # - y-axis: Monthly rent price
    # - hue: Color-coded by location to compare trends across regions
    sns.lineplot(data=df, x="Year Completed", y="Price", hue="Location", ax=ax)
    
    # Add a descriptive title to the chart
    ax.set_title("Rent Price Trends by Location")
    
    # Label the y-axis to clarify the metric being visualized
    ax.set_ylabel("Monthly Rent Price")
    
    # Label the x-axis to indicate the time dimension
    ax.set_xlabel("Year Completed")
    
    # Add gridlines to improve visual alignment and readability
    ax.grid(True)
    
    # Return the figure object for rendering or saving
    return fig

def plot_typology_distribution(df):
    """Bar chart showing number of projects per typology."""
    
    # Create a figure and axis with a slightly smaller size for compact display
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Count the number of occurrences of each housing typology
    typology_counts = df["Typology"].value_counts()
    
    # Plot a bar chart using the typology names and their respective counts
    sns.barplot(x=typology_counts.index, y=typology_counts.values, ax=ax)
    
    # Title to explain what the chart represents
    ax.set_title("Distribution of Housing Typologies")
    
    # Label the y-axis to show the number of projects
    ax.set_ylabel("Number of Projects")
    
    # Label the x-axis to show the typology categories
    ax.set_xlabel("Typology")
    
    # Rotate x-axis labels for better readability, especially if typology names are long
    ax.tick_params(axis='x', rotation=45)
    
    # Return the figure for display or export
    return fig

def plot_price_by_development(df):
    """Boxplot comparing rent prices across development types."""
    
    # Create a wide figure to accommodate multiple development types
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Boxplot shows distribution (median, quartiles, outliers) of rent prices per development type
    sns.boxplot(data=df, x="Type Of Development", y="Price", ax=ax)
    
    # Title to describe the comparison being made
    ax.set_title("Rent Price by Development Type")
    
    # Label the y-axis to indicate the price metric
    ax.set_ylabel("Monthly Rent Price")
    
    # Label the x-axis to show the development categories
    ax.set_xlabel("Development Type")
    
    # Rotate x-axis labels to prevent overlap and improve clarity
    ax.tick_params(axis='x', rotation=45)
    
    # Return the figure for further use
    return fig

def plot_project_timeline(df):
    """Histogram comparing project start vs completion years."""
    
    # Create a wide figure to show temporal distribution clearly
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot histogram of project start years
    sns.histplot(df["Year Started"], color="blue", label="Started", kde=False, bins=20)
    
    # Overlay histogram of project completion years
    sns.histplot(df["Year Completed"], color="green", label="Completed", kde=False, bins=20)
    
    # Title to explain the dual timeline comparison
    ax.set_title("Project Start vs Completion Timeline")
    
    # Label x-axis to show the year range
    ax.set_xlabel("Year")
    
    # Label y-axis to show how many projects fall into each year bin
    ax.set_ylabel("Number of Projects")
    
    # Add legend to distinguish between start and completion distributions
    ax.legend()
    
    # Return the figure object
    return fig

def plot_duration_distribution(df):
    """Histogram of project durations."""
    
    # Create a compact figure for duration distribution
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Plot histogram of project durations (in years)
    sns.histplot(df["Duration"], bins=15, color="purple", ax=ax)
    
    # Title to describe what the chart shows
    ax.set_title("Distribution of Project Durations")
    
    # Label x-axis to indicate duration in years
    ax.set_xlabel("Duration (Years)")
    
    # Label y-axis to show how many projects fall into each duration bin
    ax.set_ylabel("Number of Projects")
    
    # Return the figure for rendering or saving
    return fig
