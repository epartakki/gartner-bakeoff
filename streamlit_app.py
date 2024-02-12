import streamlit as st
import pandas as pd
import plotly.express as px

# Ensure the CSV file is in your GitHub repo in the correct directory
@st.cache
def load_data():
    data = pd.read_csv("mandatory.csv")
    return data

df = load_data()

# Use the printed column names to set these variables correctly
country_column_name = 'Country'  # Replace with the actual column name for countries
age_group_column_name = 'Age Group'  # Replace with the actual column name for age groups

# ... (rest of your code) ...

# Update the filtering step with the correct column names
filtered_data = df[df[country_column_name].isin(countries) & df[age_group_column_name].isin(age_groups)]

# Check your column names and ensure they match these values
age_group_column_name = 'Age Group'  # Adjust if your actual column name is different

st.title("Poverty Rates by Age Group")

# Sidebar filters
countries = st.sidebar.multiselect("Select Countries", options=df['Country'].unique())

# Use the actual age group names from your dataset
age_groups = st.sidebar.multiselect(
    "Select Age Groups", 
    options=['Total population', 'Working age population', 'Retirement age population'],
    default=['Total population', 'Working age population', 'Retirement age population']  # You can set defaults as you like
)

# Filter based on selections, make sure to use the actual column name from your CSV
filtered_data = df[df['Country'].isin(countries) & df[age_group_column_name].isin(age_groups)]

# Proceed with your plotting code...
# For example, using plotly to create a scatter plot
fig = px.scatter(filtered_data, x="Country", y="Poverty Rate", color=age_group_column_name, 
                 symbol=age_group_column_name, title="Poverty Rates by Age Group and Country")
st.plotly_chart(fig, use_container_width=True)
