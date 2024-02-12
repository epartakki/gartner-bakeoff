import streamlit as st
import pandas as pd
import plotly.express as px

# Load and cache the data
@st.cache
def load_data():
    return pd.read_csv("mandatory.csv")

# Function to plot the data
def plot_data(filtered_df):
    fig = px.scatter(filtered_df, x="Country", y="Poverty Rate", color="Age Group", 
                     symbol="Age Group", title="Poverty Rates by Age Group and Country")
    st.plotly_chart(fig, use_container_width=True)

# Main app function
def main():
    df = load_data()

    # Display the app title
    st.title("Poverty Rates by Age Group")

    # Sidebar filters
    # Use the actual column names from the DataFrame
    country_options = df['Country'].unique()
    age_group_options = ['Total population', 'Working age population', 'Retirement age population']
    
    countries = st.sidebar.multiselect("Select Countries", options=country_options, default=country_options)
    age_groups = st.sidebar.multiselect("Select Age Groups", options=age_group_options, default=age_group_options)

    # Filter data based on selections
    if countries and age_groups:
        filtered_data = df[df['Country'].isin(countries) & df['Age Group'].isin(age_groups)]
        plot_data(filtered_data)
    else:
        st.write("Please select at least one country and one age group to display the data.")

if __name__ == "__main__":
    main()
