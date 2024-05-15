import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
with open('new_file', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit interface
st.title("Wine Quality Prediction")

# User input for feature values
st.header("Enter Wine Features")
fixed_acidity = st.number_input("Fixed Acidity", min_value=4.0, max_value=16.0, value=8.31, step=0.01)
volatile_acidity = st.number_input("Volatile Acidity", min_value=0.08, max_value=1.58, value=0.53, step=0.01)
citric_acid = st.number_input("Citric Acid", min_value=0.0, max_value=1.0, value=0.27, step=0.01)
residual_sugar = st.number_input("Residual Sugar", min_value=0.6, max_value=15.5, value=2.54, step=0.01)
chlorides = st.number_input("Chlorides", min_value=0.01, max_value=0.61, value=0.087, step=0.001)
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=1.0, max_value=72.0, value=15.87, step=0.1)
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=6.0, max_value=289.0, value=46.47, step=0.1)
density = st.number_input("Density", min_value=0.990, max_value=1.003, value=0.9967, step=0.0001)
pH = st.number_input("pH", min_value=2.72, max_value=4.01, value=3.31, step=0.01)
sulphates = st.number_input("Sulphates", min_value=0.33, max_value=2.0, value=0.66, step=0.01)
alcohol = st.number_input("Alcohol", min_value=8.4, max_value=14.9, value=10.42, step=0.01)

# Predict button
if st.button("Predict"):
    # Make prediction
    features = {
        'fixed acidity': fixed_acidity,
        'volatile acidity': volatile_acidity,
        'citric acid': citric_acid,
        'residual sugar': residual_sugar,
        'chlorides': chlorides,
        'free sulfur dioxide': free_sulfur_dioxide,
        'total sulfur dioxide': total_sulfur_dioxide,
        'density': density,
        'pH': pH,
        'sulphates': sulphates,
        'alcohol': alcohol
    }

    input_df = pd.DataFrame([features])

    prediction_proba = model.predict_proba(input_df)[0]

    # Display prediction probabilities for both classes
    st.header("Prediction Probabilities")
    st.write(f"Probability of wine being of low quality: {prediction_proba[0]:.2f}")
    st.write(f"Probability of wine being of high quality: {prediction_proba[1]:.2f}")
