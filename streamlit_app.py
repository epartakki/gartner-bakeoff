import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def load_data():
    data = pd.read_csv("mandatory.csv")
    data.columns = data.columns.str.strip()  # Clean column names
    return data

df = load_data()

# Function to plot the scatter plot
def plot_scatter(filtered_df):
    fig = px.scatter(filtered_df, x="country", y="value", color="age", 
                     title="Poverty Rates by Age Group and Country")
    st.plotly_chart(fig, use_container_width=True)

# Function to plot the map
def plot_map(df, year):
    filtered_df = df[df['year'] == year]
    fig = px.scatter_geo(filtered_df, locations="country", color="value",
                         hover_name="country", size="value",
                         projection="natural earth", title=f"Poverty Rates in {year}")
    st.plotly_chart(fig, use_container_width=True)

def main():
    st.title("Poverty Rates by Age Group")

    # Sidebar filters for the scatter plot
    country_options = df['country'].unique()
    age_group_options = df['age'].unique()
    countries = st.sidebar.multiselect("Select Countries", options=country_options, default=country_options)
    age_groups = st.sidebar.multiselect("Select Age Groups", options=age_group_options, default=age_group_options)

    # Year slider for the map
    year = st.slider("Year", int(df['year'].min()), int(df['year'].max()), step=1)

    # Scatter plot
    if countries and age_groups:
        filtered_data = df[df['country'].isin(countries) & df['age'].isin(age_groups)]
        plot_scatter(filtered_data)

    # Map visualization
    plot_map(df, year)

if __name__ == "__main__":
    main()
