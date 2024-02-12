import streamlit as st
import pandas as pd
import plotly.express as px

# Create three columns
col1, col2, col3 = st.columns([1, 2, 1])  # The middle column is larger

# Display the logo in the middle column
with col2:
    st.image("tamr.png", use_column_width=True)

# Set the title of the app
st.title('Tamr Gartner Bake-Off')
st.text('')

st.markdown("What's your perception of income inequality? The OECD tool Compare your income allows you to see whether your perception is in line with reality. In only a few clicks, you can see where you fit in your country's income distribution. In June 2020, an updated edition was released to explore how people’s perceptions of inequality impact their willingness to support redistribution and to see what areas users would prioritise for public spending.")

st.markdown('The OECD Income Distribution database (IDD) has been developed to benchmark and monitor countries’ performance in the field of income inequality and poverty. It contains a number of standardised indicators based on the central concept of “equivalised household disposable income”, i.e., the total income received by the households less the current taxes and transfers they pay, adjusted for household size with an equivalence scale. While household income is only one of the factors shaping people’s economic well-being, it is also the one for which comparable data for all OECD countries are most common. Income distribution has a long-standing tradition among household-level statistics, with regular data collections going back to the 1980s (and sometimes earlier) in many OECD countries.')

st.markdown('[The poverty rate is the ratio of the number of people (in a given age group) whose income falls below the poverty line; taken as half the median household income of the total population. It is also available by broad age group: child poverty (0-17 years old), working-age poverty and elderly poverty (66 year-olds or more).](https://stats.oecd.org/index.aspx?lang=en#)')

# Load and cache the data
@st.cache
def load_data():
    data = pd.read_csv("mandatory.csv")
    data.columns = data.columns.str.strip()  # Remove leading/trailing whitespaces
    # Filter for specific measure
    filtered_data = data[data['measure'] == "All age groups: Poverty rate after taxes and transfers"]
    return filtered_data

# Function to plot the data
def plot_data(filtered_df):
    fig = px.scatter(filtered_df, x="country", y="value", color="measure",
                     title="Poverty Rates by Country and Year")
    st.plotly_chart(fig, use_container_width=True)

# Main app function
def main():
    df = load_data()

    # Filters above the graph
    country_options = ['Select All'] + sorted(df['country'].unique().tolist())
    year_options = ['Select All'] + sorted(df['year'].unique().tolist())

    # Filter selectors
    countries = st.multiselect("Select Countries", options=country_options, default='Select All')
    selected_year = st.selectbox("Select Year", options=year_options, index=0)

    # Handle 'Select All' functionality
    if 'Select All' in countries:
        countries = country_options[1:]  # Exclude 'Select All'
    
    # Apply filters to data
    if selected_year == 'Select All':
        filtered_data = df[df['country'].isin(countries)]
    else:
        filtered_data = df[df['country'].isin(countries) & (df['year'] == selected_year)]

    # Plot the data if selections are made
    if not filtered_data.empty:
        plot_data(filtered_data)
    else:
        st.write("No data available for the selected criteria.")

if __name__ == "__main__":
    main()
