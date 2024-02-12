import streamlit as st
import pandas as pd
import plotly.express as px

# Load and cache the data
@st.cache
def load_data():
    return pd.read_csv("mandatory.csv")

df = load_data()

# Function to plot the map with a year slider
def plot_map(df):
    year = st.slider("Year", int(df['year'].min()), int(df['year'].max()), step=1)
    filtered_df = df[df['year'] == year]
    
    # Plot using ISO country codes
    fig = px.scatter_geo(filtered_df, locations="ISO", color="value",
                         hover_name="country", size="value",
                         projection="natural earth", title=f"Poverty Rates in {year}",
                         locationmode='ISO-3')  # Use ISO-3 mode for ISO country codes
    st.plotly_chart(fig, use_container_width=True)

def main():
    st.title("Global Poverty Rates Visualization")
    
    # Plot the map visualization
    plot_map(df)

if __name__ == "__main__":
    main()
