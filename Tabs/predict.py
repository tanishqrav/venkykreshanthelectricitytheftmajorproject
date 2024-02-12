"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict
from web_functions import load_data

def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Theft Detection")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
               Electricity Theft Detection.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    Bp= st.slider("Electricity:Facility [kW](Hourly)", float(df["Electricity:Facility [kW](Hourly)"].min()), float(df["Electricity:Facility [kW](Hourly)"].max()))
    Al = st.slider("Fans:Electricity [kW](Hourly)", float(df["Fans:Electricity [kW](Hourly)"].min()), float(df["Fans:Electricity [kW](Hourly)"].max()))
    Su = st.slider("Cooling:Electricity [kW](Hourly)", float(df["Cooling:Electricity [kW](Hourly)"].min()), float(df["Cooling:Electricity [kW](Hourly)"].max()))
    Bu = st.slider("Heating:Electricity [kW](Hourly)", float(df["Heating:Electricity [kW](Hourly)"].min()), float(df["Heating:Electricity [kW](Hourly)"].max()))
    Sc = st.slider("InteriorLights:Electricity [kW](Hourly)", float(df["InteriorLights:Electricity [kW](Hourly)"].min()), float(df["InteriorLights:Electricity [kW](Hourly)"].max()))
    Sod = st.slider("InteriorEquipment:Electricity [kW](Hourly)", float(df["InteriorEquipment:Electricity [kW](Hourly)"].min()), float(df["InteriorEquipment:Electricity [kW](Hourly)"].max()))
    Pot = st.slider("Gas:Facility [kW](Hourly)", float(df["Gas:Facility [kW](Hourly)"].min()), float(df["Gas:Facility [kW](Hourly)"].max()))
    Hemo = st.slider("Heating:Gas [kW](Hourly)", float(df["Heating:Gas [kW](Hourly)"].min()), float(df["Heating:Gas [kW](Hourly)"].max()))
    Wbcc = st.slider("InteriorEquipment:Gas [kW](Hourly)", float(df["InteriorEquipment:Gas [kW](Hourly)"].min()), float(df["InteriorEquipment:Gas [kW](Hourly)"].max()))
    Rbcc = st.slider("Water Heater:WaterSystems:Gas [kW](Hourly)", float(df["Water Heater:WaterSystems:Gas [kW](Hourly)"].min()), float(df["Water Heater:WaterSystems:Gas [kW](Hourly)"].max()))

    
    # Create a list to store all the features
    features = [Bp,Al,Su,Bu,Sc,Sod,Pot,Hemo,Wbcc,Rbcc]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score 
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 'Normal'):
            st.success("No Theft Detected")
            st.balloons()
        else:
            st.error("Theft Detected")
            st.snow()

        # Print teh score of the model 
        #st.text_area("Accuracy: ",value=f'This model has an accuracy of {score*100}',height=100)
