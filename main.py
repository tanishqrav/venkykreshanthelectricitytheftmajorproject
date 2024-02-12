"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data
    
# Import pages
from Tabs import home, data, predict, visualise

# Configure the app
st.set_page_config(
    page_title = 'Electricity Theft Detection',
    page_icon = 'random',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "Dataset": data,
    "Detection": predict,
    "Visualisation": visualise
    
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Detection", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Dataset"):
    Tabs[page].app(df)
else:
    Tabs[page].app()