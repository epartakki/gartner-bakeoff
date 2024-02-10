import streamlit as st
import pandas as pd
import pydeck as pdk

# Set the title of the app
st.title('Tamr Gartner Bake-Off')

# Display a logo
logo_path = 'tamr.png'  
st.image(logo_path, caption='')

st.markdown("What's your perception of income inequality? The OECD tool Compare your income allows you to see whether your perception is in line with reality. In only a few clicks, you can see where you fit in your country's income distribution. In June 2020, an updated edition was released to explore how people’s perceptions of inequality impact their willingness to support redistribution and to see what areas users would prioritise for public spending.")


# Data including all the specified countries, their latitudes, longitudes, and placeholder counts
data = {
    'country': [
        'Australia', 'Austria', 'Belgium', 'Canada', 'Czechia',
        'Denmark', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland',
        'Ireland', 'Italy', 'Japan', 'Korea', 'Luxembourg', 'Mexico', 'Netherlands',
        'New Zealand', 'Norway', 'Poland', 'Portugal', 'Slovak Republic', 'Spain',
        'Sweden', 'Switzerland', 'Türkiye', 'United Kingdom', 'United States', 'Chile',
        'Estonia', 'Israel', 'Russia', 'Slovenia', 'Latvia', 'Lithuania', 'Brazil',
        'China (People\'s Republic of)', 'Costa Rica', 'India', 'South Africa', 'Bulgaria',
        'Romania', 'Croatia'
    ],
    'lat': [
        -25.274398, 47.516231, 50.503887, 56.130366, 49.817492,
        56.26392, 61.92411, 46.227638, 51.165691, 39.074208, 47.162494, 64.963051,
        53.41291, 41.87194, 36.204824, 35.907757, 49.815273, 23.634501, 52.132633,
        -40.900557, 60.472024, 51.919438, 39.399872, 48.669026, 40.463667,
        60.128161, 46.818188, 38.963745, 55.378051, -95.712891, -35.675147,
        58.595272, 31.046051, 61.52401, 46.151241, 56.879635, 55.169438, -14.235004,
        35.86166, 9.748917, 20.593684, -30.559482, 42.733883,
        45.943161, 45.1
    ],
    'lon': [
        133.775136, 14.550072, 4.469936, -106.346771, 15.472962,
        9.501785, 25.748151, 2.213749, 10.451526, 21.824312, 19.503304, -19.020835,
        -8.24389, 12.56738, 138.252924, 127.766922, 6.129583, -102.552784, 5.291266,
        174.885971, 8.468946, 19.145136, -8.224454, 19.699024, -3.74922,
        18.643501, 8.227512, 35.243322, -3.435973, -37.09024, -71.542969,
        25.013607, 34.851612, 105.318756, 14.995463, 24.603189, 23.881275, -51.92528,
        104.195397, -83.753428, 78.96288, 22.937506, 25.48583,
        24.96676, 15.2
    ],
    'count': list(range(1, 46))  # Placeholder incremental counts for demonstration
}

df = pd.DataFrame(data)

# Adding circles to the map based on the data
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position="[lon, lat]",
    get_radius="count * 200000",  # Adjust size multiplier as needed
    get_color="[180, 0, 200, 140]",  # RGBA color of the circles
    pickable=True,
)

# Set the viewport location to show all the circles effectively
view_state = pdk.ViewState(latitude=20, longitude=0, zoom=1)

# Render the map
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
