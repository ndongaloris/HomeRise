# app/dashboard.py

import streamlit as st
from src.data_loader import load_data
from src.analysis import filter_data
from src.visualization import plot_trends

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Trends", "Demand Analysis"])

if page == "Overview":
    st.title("Welcome to AnaliHouse")
    st.write("Explore housing trends across Africa.")
elif page == "Trends":
    data = load_data()
    filtered = filter_data(data)
    fig = plot_trends(filtered)
    st.pyplot(fig)
elif page == "Demand Analysis":
    st.write("Coming soon: demand heatmaps and affordability metrics.")
