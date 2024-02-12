import streamlit as st
import pandas as pd
import plotly.express as px

# Create three columns for layout
col1, col2, col3 = st.columns([1,2,1])  # Middle column is larger for a logo or image

# Display the logo in the middle column if you have a logo to display
with col2:
    st.image("tamr.png", use_column_width=True)

# Set the title and introductory text of the app
st.title('Tamr Gartner Bake-Off')
st.text('')

# Introductory markdowns
st.markdown("What's your perception of income inequality? ...")
st.markdown('The OECD Income Distribution database (IDD) ...')

# Load and cache the data
@st.cache
def load_data():
    data = pd.read_csv("mandatory.csv")
    data.columns = data.columns.str.strip()  # Remove leading/trailing whitespaces
    # Pre-filter to include specific methodology and exclude year 2022
    filtered_data = data[(data['methodology'] == 'age all groups: poverty rate after taxes and transfers') & (data['year'] != 2022)]
    return filtered_data

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
    # Since methodology is pre-filtered, no selector is needed for it
    year_options = ['Select All'] + sorted(df['year'].astype(str).unique().tolist())  # Ensure years are strings for consistency

    # Filter selectors with explicit keys
    countries = st.multiselect("Select Countries", options=country_options, default='Select All', key='countries_select')
    age_groups = st.multiselect("Select Age Groups", options=age_group_options, default='Select All', key='age_groups_select')
    selected_year = st.selectbox("Select Year", options=year_options, index=0, key='year_select')

    # Handle 'Select All' functionality for filters
    if 'Select All' in countries:
        countries = country_options[1:]  # Exclude 'Select All'
    if 'Select All' in age_groups:
        age_groups = age_group_options[1:]  # Exclude 'Select All'

    # Apply filters to data
    filtered_data = df[df['country'].isin(countries) & df['age'].isin(age_groups)]
    if selected_year != 'Select All':
        filtered_data = filtered_data[filtered_data['year'].astype(str) == selected_year]

    # Plot the data if selections are made
    if not filtered_data.empty:
        plot_data(filtered_data)
    else:
        st.write("No data available for the selected criteria.")

if __name__ == "__main__":
    main()
    
    main()

