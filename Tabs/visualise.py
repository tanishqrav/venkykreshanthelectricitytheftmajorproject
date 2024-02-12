import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn import tree
import streamlit as st
import pandas as pd

# Import necessary functions from web_functions
from web_functions import train_model
from web_functions import load_data

def app(df, X, y):
    """This function creates the visualization page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    #st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise Electricity Theft Detection")

    # Create a checkbox to show correlation heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")
        # Exclude the last two columns and the first column
        corr_df = df.iloc[:, 1:-2].corr()

        fig = plt.figure(figsize=(8, 6))
        ax = sns.heatmap(corr_df, annot=True)
        bottom, top = ax.get_ylim()
        ax.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot(fig)

    if st.checkbox("Electricity vs Fans"):
        sns.color_palette("rocket", as_cmap=True)
        ax = sns.scatterplot(x="Electricity:Facility [kW](Hourly)", y="Fans:Electricity [kW](Hourly)", data=df)
        st.pyplot()

    if st.checkbox("Show Confusion Matrix"):
        # Train model to get predictions
        model, score = train_model(X, y)
        predictions = model.predict(X)
        # Calculate confusion matrix
        cm = confusion_matrix(y, predictions)
        # Plot confusion matrix
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', xticklabels=['0', '1'], yticklabels=['0', '1'])
        plt.xlabel('Predicted labels')
        plt.ylabel('True labels')
        plt.title('Confusion Matrix')
        st.pyplot()

    if st.checkbox("Show Pie Chart"):
        st.subheader("Pie Chart")
        # Assuming 'y' contains categorical data for pie chart
        # Count unique values
        value_counts = y.value_counts()
        # Plot pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Distribution of Categories')
        st.pyplot()

