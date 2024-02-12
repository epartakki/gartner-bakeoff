import streamlit as st
import pandas as pd
import plotly.express as px

# Assuming 'mandatory.csv' is structured appropriately for this plot
# with columns 'Country', 'Age Group', 'Poverty Rate', and 'Year'

@st.cache
def load_data():
    data = pd.read_csv("mandatory.csv")
    return data

df = load_data()

st.title("Poverty Rates by Age Group")

# Sidebar filters
countries = st.sidebar.multiselect("Select Countries", options=df['Country'].unique())
age_groups = st.sidebar.multiselect("Select Age Groups", options=df['Age Group'].unique())
years = st.sidebar.multiselect("Select Years", options=df['Year'].unique(), default=df['Year'].max())

# Filtering data
filtered_data = df[df['Country'].isin(countries) & df['Age Group'].isin(age_groups) & df['Year'].isin(years)]

# Plotting
fig = px.scatter(filtered_data, x="Country", y="Poverty Rate", color="Age Group", symbol="Age Group",
                 title="Poverty Rates by Age Group and Country")

st.plotly_chart(fig, use_container_width=True)
