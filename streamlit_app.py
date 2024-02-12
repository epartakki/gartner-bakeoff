import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache  # Use the cache decorator to load the data only once
def load_data():
    df = pd.read_csv("mandatory.csv")
    return df

df = load_data()

# Streamlit app layout
st.title("Poverty Rates Visualization")

# Selectors in the sidebar
country = st.sidebar.multiselect("Select Country", options=df['Country'].unique())
age_group = st.sidebar.radio("Select Age Group", options=['Child Poverty', 'Working-Age Poverty', 'Elderly Poverty'])

# Filter data based on selections
filtered_data = df[(df['Country'].isin(country)) & (df['Age Group'] == age_group)]

if not filtered_data.empty:
    # Visualization
    fig, ax = plt.subplots()
    
    if st.sidebar.checkbox("Show Poverty Rates"):
        sns.barplot(x='Country', y='Poverty Rate', data=filtered_data, ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    
    if st.sidebar.checkbox("Show Relative Income Levels"):
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Country', y='Relative Income Level', data=filtered_data)
        plt.xticks(rotation=45)
        st.pyplot(plt)
else:
    st.write("No data available for the selected criteria.")

