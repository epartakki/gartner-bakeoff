import streamlit as st
import pandas as pd
import plotly.express as px

# Load and cache the data
@st.cache
def load_data():
    data = pd.read_csv("mandatory.csv")
    # Remove leading/trailing whitespaces from column names
    data.columns = data.columns.str.strip()
    return data

# Function to plot the data
def plot_data(filtered_df):
    fig = px.scatter(filtered_df, x="country", y="value", color="age", 
                     title="Poverty Rates by Age Group and Country")
    st.plotly_chart(fig, use_container_width=True)

# Main app function
def main():
    df = load_data()

    # Display the app title
    st.title("Poverty Rates by Age Group")

    # Sidebar filters
    country_options = df['country'].unique()
    age_group_options = df['age'].unique()

    countries = st.sidebar.multiselect("Select Countries", options=country_options, default=country_options)
    age_groups = st.sidebar.multiselect("Select Age Groups", options=age_group_options, default=age_group_options)

    # Filter data based on selections
    if countries and age_groups:
        # Use the corrected column names here
        filtered_data = df[df['country'].isin(countries) & df['age'].isin(age_groups)]
        plot_data(filtered_data)
    else:
        st.write("Please select at least one country and one age group to display the data.")

if __name__ == "__main__":
    main()
