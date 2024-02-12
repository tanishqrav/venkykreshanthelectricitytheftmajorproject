"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Electricity Theft Detection")
    st.image("images/Electricity.png")



    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Electricity theft can be tricky to spot, as in most cases you will need to have access to the meter to be able to spot the signs that it has been tampered with. These signs include loose or unusual wiring, sparks coming from the meter or burn marks or scorches on the meter.
        </p>
    """, unsafe_allow_html=True)
