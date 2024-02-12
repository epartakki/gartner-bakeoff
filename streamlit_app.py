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
                     title="Poverty Rates by Age Group, Methodology, and Year")
    st.plotly_chart(fig, use_container_width=True)

# Main app function
def main():
    df = load_data()

    # Display the app title
    st.title("Poverty Rates by Age Group, Methodology, and Year")

    # Filters above the graph
    country_options = ['Select All'] + sorted(df['country'].unique().tolist())
    age_group_options = ['Select All'] + sorted(df['age'].unique().tolist())
    methodology_options = ['Select All'] + sorted(df['methodology'].unique().tolist())
    year_options = ['Select All'] + sorted(df['year'].unique().tolist())

    # Filter selectors
    countries = st.multiselect("Select Countries", options=country_options, default='Select All')
    age_groups = st.multiselect("Select Age Groups", options=age_group_options, default='Select All')
    methodologies = st.multiselect("Select Methodology", options=methodology_options, default='Select All')
    selected_year = st.selectbox("Select Year", options=year_options, index=0)

    # Handle 'Select All' functionality
    if 'Select All' in countries:
        countries = country_options[1:]  # Exclude 'Select All'
    if 'Select All' in age_groups:
        age_groups = age_group_options[1:]  # Exclude 'Select All'
    if 'Select All' in methodologies:
        methodologies = methodology_options[1:]  # Exclude 'Select All'
    if selected_year == 'Select All':
        filtered_data = df[(df['country'].isin(countries)) &
                           (df['age'].isin(age_groups)) &
                           (df['methodology'].isin(methodologies))]
    else:
        filtered_data = df[(df['country'].isin(countries)) &
                           (df['age'].isin(age_groups)) &
                           (df['methodology'].isin(methodologies)) &
                           (df['year'] == selected_year)]

    # Plot the data if selections are made
    if not filtered_data.empty:
        plot_data(filtered_data)
    else:
        st.write("No data available for the selected criteria.")

if __name__ == "__main__":
    main()
