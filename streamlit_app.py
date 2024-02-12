import streamlit as st
import pandas as pd
import plotly.express as px

# Create three columns
col1, col2, col3 = st.columns([1,2,1])  # The middle column is larger

# Display the logo in the middle column
with col2:
    st.image("tamr.png", use_column_width=True)

# Set the title of the app
st.title('Tamr Gartner Bake-Off')
st.text('')

st.markdown("What's your perception of income inequality? The OECD tool Compare your income allows you to see whether your perception is in line with reality. In only a few clicks, you can see where you fit in your country's income distribution. In June 2020, an updated edition was released to explore how people’s perceptions of inequality impact their willingness to support redistribution and to see what areas users would prioritise for public spending.")


st.markdown('The OECD Income Distribution database (IDD) has been developed to benchmark and monitor countries’ performance in the field of income inequality and poverty. It contains a number of standardised indicators based on the central concept of “equivalised household disposable income”, i.e. the total income received by the households less the current taxes and transfers they pay, adjusted for household size with an equivalence scale. While household income is only one of the factors shaping people’s economic well-being, it is also the one for which comparable data for all OECD countries are most common. Income distribution has a long-standing tradition among household-level statistics, with regular data collections going back to the 1980s (and sometimes earlier) in many OECD countries.') 
st.markdown('Achieving comparability in this field is a challenge, as national practices differ widely in terms of concepts, measures, and statistical sources. In order to maximise international comparability as well as inter-temporal consistency of data, the IDD data collection and compilation process is based on a common set of statistical conventions (e.g. on income concepts and components). The information obtained by the OECD through a network of national data providers, via a standardized questionnaire, is based on national sources that are deemed to be most representative for each country.')

# Load and cache the data
@st.cache
def load_data():
    data = pd.read_csv("mandatory.csv")
    # Remove leading/trailing whitespaces from column names
    data.columns = data.columns.str.strip()
    # Pre-filter the dataframe to include only the specific methodology
    data = data[data['methodology'] == 'age all groups: poverty rate after taxes and transfers']
    return data

# Main app function
def main():
    df = load_data()

    # Assuming 'year' is stored as an integer. If it's stored as string, you might need to convert it before comparison
    df = df[df['year'] != 2022]  # Exclude year 2022 from the dataset

    # Display the app title and markdowns
    st.title('Tamr Gartner Bake-Off')
    # Your markdown texts here...

    # Filters above the graph
    country_options = ['Select All'] + sorted(df['country'].unique().tolist())
    age_group_options = ['Select All'] + sorted(df['age'].unique().tolist())
    # Methodology options pre-filtered, so no need to select it in the UI
    year_options = ['Select All'] + sorted(df['year'].unique().tolist())
    year_options.remove(2022)  # Remove 2022 from the list if it's still present

    # Filter selectors
    countries = st.multiselect("Select Countries", options=country_options, default='Select All')
    age_groups = st.multiselect("Select Age Groups", options=age_group_options, default='Select All')
    selected_year = st.selectbox("Select Year", options=year_options, index=0)

    # Handle 'Select All' functionality
    if 'Select All' in countries:
        countries = country_options[1:]  # Exclude 'Select All'
    if 'Select All' in age_groups:
        age_groups = age_group_options[1:]  # Exclude 'Select All'
    # Since we've pre-filtered methodology, we don't have a selector for it anymore

    if selected_year == 'Select All':
        filtered_data = df[(df['country'].isin(countries)) & (df['age'].isin(age_groups))]
    else:
        filtered_data = df[(df['country'].isin(countries)) & (df['age'].isin(age_groups)) & (df['year'] == selected_year)]

    # Plot the data if selections are made
    if not filtered_data.empty:
        plot_data(filtered_data)
    else:
        st.write("No data available for the selected criteria.")

if __name__ == "__main__":
    main()

