import streamlit as st
import pandas as pd
import pydeck as pdk

# Set the title of the app
st.title('Tamr Gartner Bake-Off')

# Display a logo
logo_path = 'tamr.png'  
st.image(logo_path, caption='Tamr')


# dataset
data = {
    'country': ['United States', 'France', 'Germany'],
    'lat': [37.0902, 46.2276, 51.1657],  # Example latitudes
    'lon': [-95.7129, 2.2137, 10.4515],  # Example longitudes
    'count': [100, 50, 75]  # Example record counts
}

df = pd.DataFrame(data)

# Function to get the radius size based on record count
# Adjust this function based on your dataset's specific needs
def get_radius_size(record_count):
    base_size = 10000  # Base size for the circle
    return base_size * record_count

# Adding circles to the map
layer = pdk.Layer(
    'ScatterplotLayer',
    data=df,
    get_position='[lon, lat]',
    get_radius='count * 10000',  # Adjust the multiplier for circle size
    get_color=[180, 0, 200, 140],  # RGBA color of the circles
    pickable=True
)

# Set the viewport location
view_state = pdk.ViewState(latitude=20, longitude=0, zoom=1)

# Render the map
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
