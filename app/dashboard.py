import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import folium
from streamlit_folium import st_folium

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

# ─────────────────────────────────────────────────────────────
# 🏠 App Configuration
st.set_page_config(page_title="HouseRise", layout="wide")
st.title("🏠 HouseRise: Housing Market Insights")
st.markdown("Explore housing trends, project timelines, and affordability across African cities.")

# ─────────────────────────────────────────────────────────────
# 📦 Load and Clean Data
df = load_data("data/raw/MapProjects_data.csv")
df = clean_data(df)

# ─────────────────────────────────────────────────────────────
# 🔍 Sidebar Filters
st.sidebar.header("🔍 Filter Options")

dev_types = df["Type Of Development"].dropna().unique()
selected_dev = st.sidebar.selectbox("Development Type", dev_types)

typologies = df["Typology"].dropna().unique()
selected_typology = st.sidebar.selectbox("Typology", typologies)

statuses = df["Project Status"].dropna().unique()
selected_status = st.sidebar.selectbox("Project Status", statuses)

min_year, max_year = int(df["Year Completed"].min()), int(df["Year Completed"].max())
if min_year == max_year:
    st.sidebar.warning(f"⚠️ Only one year ({min_year}) found. Year filter disabled.")
    year_range = (min_year, max_year)
else:
    year_range = st.sidebar.slider("📆 Year Completed Range", min_year, max_year, (min_year, max_year))

# ─────────────────────────────────────────────────────────────
# 🧮 Apply Filters
filtered_df = filter_data(
    df,
    dev_type=selected_dev,
    typology=selected_typology,
    year_range=year_range,
    status=selected_status
)

# ─────────────────────────────────────────────────────────────
# 📊 Summary Statistics
st.subheader("📊 Summary Statistics")
stats = get_summary_stats(filtered_df)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Projects", stats["Total Projects"])
col2.metric("Average Rent", f"${stats['Average Rent']}")
col3.metric("Avg. Duration", f"{stats['Average Duration']} years")
col4.metric("Unique Locations", stats["Unique Locations"])

# ─────────────────────────────────────────────────────────────
# 📈 Visualizations
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

# ─────────────────────────────────────────────────────────────
# 🗺️ Map View
st.subheader("🗺️ Project Locations")
map_center = [filtered_df["Latitude"].mean(), filtered_df["Longitude"].mean()]
m = folium.Map(location=map_center, zoom_start=6)

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

st_folium(m, width=700, height=500)

# ─────────────────────────────────────────────────────────────
# 📥 Export Filtered Data
st.subheader("📥 Export Filtered Data")
st.download_button(
    label="Download CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_housing_data.csv",
    mime="text/csv"
)

# ─────────────────────────────────────────────────────────────
# 🏢 Developer Leaderboard
st.subheader("🏢 Top Developers")
top_devs = group_by_developer(filtered_df).head(10)
st.dataframe(top_devs.reset_index().rename(columns={"index": "Developer", "Developer Name": "Projects"}))
