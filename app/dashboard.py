import sys
import os
# Dynamically add the parent directory to the Python path to enable relative imports from /src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Streamlit for UI, Folium for interactive maps, and streamlit-folium for embedding maps
import streamlit as st
import folium
from streamlit_folium import st_folium

# Modular imports from your custom data and visualization pipeline
from src.data_loader import load_data
from src.analysis import (
    clean_data, 
    filter_data, 
    get_summary_stats, 
    group_by_developer
)
from src.visualization import (
    plot_price_trends,
    plot_typology_distribution,
    plot_price_by_development,
    plot_project_timeline,
    plot_duration_distribution
)

# Set page title and layout for a wide, dashboard-style interface
st.set_page_config(page_title="HouseRise", layout="wide")

# Main title and introductory markdown
st.title("🏠 HouseRise: Housing Market Insights")
st.markdown("Explore housing trends, project timelines, and affordability across African cities.")

# Load raw CSV data and clean it using your pipeline
df = load_data("data/raw/MapProjects_data.csv")
df = clean_data(df)

# Sidebar UI for filtering the dataset
st.sidebar.header("🔍 Filter Options")

# Dropdowns for categorical filters
dev_types = df["Type Of Development"].dropna().unique()
selected_dev = st.sidebar.selectbox("Development Type", dev_types)

typologies = df["Typology"].dropna().unique()
selected_typology = st.sidebar.selectbox("Typology", typologies)

statuses = df["Project Status"].dropna().unique()
selected_status = st.sidebar.selectbox("Project Status", statuses)

# Slider for year range filtering
min_year, max_year = int(df["Year Completed"].min()), int(df["Year Completed"].max())
if min_year == max_year:
    st.sidebar.warning(f"⚠️ Only one year ({min_year}) found. Year filter disabled.")
    year_range = (min_year, max_year)
else:
    year_range = st.sidebar.slider("📆 Year Completed Range", min_year, max_year, (min_year, max_year))

# Sidebar UI for filtering the dataset
st.sidebar.header("🔍 Filter Options")

# Dropdowns for categorical filters
dev_types = df["Type Of Development"].dropna().unique()
selected_dev = st.sidebar.selectbox("Development Type", dev_types)

typologies = df["Typology"].dropna().unique()
selected_typology = st.sidebar.selectbox("Typology", typologies)

statuses = df["Project Status"].dropna().unique()
selected_status = st.sidebar.selectbox("Project Status", statuses)

# Slider for year range filtering
min_year, max_year = int(df["Year Completed"].min()), int(df["Year Completed"].max())
if min_year == max_year:
    st.sidebar.warning(f"⚠️ Only one year ({min_year}) found. Year filter disabled.")
    year_range = (min_year, max_year)
else:
    year_range = st.sidebar.slider("📆 Year Completed Range", min_year, max_year, (min_year, max_year))

# Apply all selected filters to the dataset
filtered_df = filter_data(
    df,
    dev_type=selected_dev,
    typology=selected_typology,
    year_range=year_range,
    status=selected_status
)

# Display key metrics in a clean, column-based layout
st.subheader("📊 Summary Statistics")
stats = get_summary_stats(filtered_df)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Projects", stats["Total Projects"])
col2.metric("Average Rent", f"${stats['Average Rent']}")
col3.metric("Avg. Duration", f"{stats['Average Duration']} years")
col4.metric("Unique Locations", stats["Unique Locations"])

# Render each chart using your modular plotting functions
st.subheader("📈 Rent Price Trends")
st.pyplot(plot_price_trends(filtered_df))

st.subheader("🏘️ Typology Distribution")
st.pyplot(plot_typology_distribution(filtered_df))

st.subheader("🏗️ Price by Development Type")
st.pyplot(plot_price_by_development(filtered_df))

st.subheader("📆 Project Timeline")
st.pyplot(plot_project_timeline(filtered_df))

st.subheader("⏳ Duration Distribution")
st.pyplot(plot_duration_distribution(filtered_df))

# Create an interactive map centered on the average coordinates
st.subheader("🗺️ Project Locations")
map_center = [filtered_df["Latitude"].mean(), filtered_df["Longitude"].mean()]
m = folium.Map(location=map_center, zoom_start=6)

# Add markers for each project with rich popup info
for _, row in filtered_df.iterrows():
    popup_text = f"""
    <b>{row['Project Name']}</b><br>
    Location: {row['Location']}<br>
    Price: ${row['Price']}<br>
    Status: {row['Project Status']}<br>
    Typology: {row['Typology']}
    """
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=folium.Popup(popup_text, max_width=300),
        tooltip=row["Location"]
    ).add_to(m)

# Embed the map in the Streamlit app
st_folium(m, width=700, height=500)

# Allow users to download the filtered dataset as a CSV
st.subheader("📥 Export Filtered Data")
st.download_button(
    label="Download CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_housing_data.csv",
    mime="text/csv"
)

# Display top developers by project count
st.subheader("🏢 Top Developers")
top_devs = group_by_developer(filtered_df).head(10)

# Format the DataFrame for display
st.dataframe(top_devs.reset_index().rename(columns={"index": "Developer", "Developer Name": "Projects"}))
