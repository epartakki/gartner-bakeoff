import streamlit as st
import pandas as pd
import plotly.express as px

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("OECD Report on Poverty", "Provider Location in the United States", "About"))

if page == "OECD Report on Poverty":
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

    @st.cache
    def load_data():
        data = pd.read_csv("mandatory.csv")
        data.columns = data.columns.str.strip()  # Remove leading/trailing whitespaces
        # Filter for specific measure
        filtered_data = data[data['measure'] == "All age groups: Poverty rate after taxes and transfers"]
        return filtered_data

    def plot_data(filtered_df):
        fig = px.scatter(filtered_df, x="country", y="value", color="measure",
                         title="Poverty Rates by Country and Year")
        st.plotly_chart(fig, use_container_width=True)

    df = load_data()
    country_options = ['Select All'] + sorted(df['country'].unique().tolist())
    year_options = ['Select All'] + sorted(df['year'].unique().tolist())
    countries = st.multiselect("Select Countries", options=country_options, default='Select All')
    selected_year = st.selectbox("Select Year", options=year_options)

    if 'Select All' in countries:
        countries = country_options[1:]
    if selected_year == 'Select All':
        filtered_data = df[df['country'].isin(countries)]
    else:
        filtered_data = df[df['country'].isin(countries) & (df['year'] == selected_year)]

    if not filtered_data.empty:
        plot_data(filtered_data)
    else:
        st.write("No data available for the selected criteria.")

elif page == "Provider Location in the United States":
    st.title("Provider Location in the United States")
    # This section is left empty per user request
    st.write("Content for 'Provider Location in the United States' goes here.")

    @st.cache
    def load_provider_data():
        data = pd.read_csv("providers.csv")
        # Assuming "Enriched Region" needs to be split into latitude and longitude
        # This is a placeholder: adjust according to your actual data format
        # data[['Latitude', 'Longitude']] = data['Enriched Region'].str.split(',', expand=True).astype(float)
        return data

    df = load_provider_data()

    # Assuming your CSV has these columns split already; if not, you'll need to preprocess
    # If "Enriched Region" is not in lat/lon format, you'll need to convert or map these regions to coordinates
    specialty_options = ['All'] + sorted(df['Taxonomy Description'].unique().tolist())
    selected_specialty = st.selectbox("Select Specialty", options=specialty_options)

    if selected_specialty != 'All':
        df_filtered = df[df['Taxonomy Description'] == selected_specialty]
    else:
        df_filtered = df

    # Assuming 'Latitude' and 'Longitude' columns exist in your dataframe
    # Plotting the map
    if not df_filtered.empty:
        fig = px.scatter_mapbox(df_filtered,
                                lat="Latitude", 
                                lon="Longitude",
                                color="Specialty",
                                hover_name="Specialty",
                                zoom=3,
                                height=300)
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No data available for the selected criteria.")

elif page == "About":
    st.title("About This App")
    st.write("This app is designed to visualize income inequality and poverty rates across different countries and years, using data from the OECD. It aims to provide insights into how income distribution varies globally and to encourage discussions on the impacts of inequality.")
