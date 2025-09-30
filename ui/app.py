# ui/app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Load final model
MODEL_PATH = "../models/final_model.pkl"
model = joblib.load(MODEL_PATH)

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

# App Title
st.title("❤️ Heart Disease Prediction App")

st.markdown("""
This app predicts whether a patient is likely to have **heart disease** 
based on their medical data.
""")

# User input form
st.header("Enter Patient Information")

age = st.number_input("Age", min_value=20, max_value=100, value=50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200, value=120)
chol = st.number_input("Cholesterol (chol)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved (thalach)", min_value=60, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=6.5, value=1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment (slope)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (thal)", [3, 6, 7])

# Convert categorical inputs
sex = 1 if sex == "Male" else 0

# Create dataframe for prediction
input_data = pd.DataFrame({
    "age": [age],
    "sex": [sex],
    "cp": [cp],
    "trestbps": [trestbps],
    "chol": [chol],
    "fbs": [fbs],
    "restecg": [restecg],
    "thalach": [thalach],
    "exang": [exang],
    "oldpeak": [oldpeak],
    "slope": [slope],
    "ca": [ca],
    "thal": [thal]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f" High risk of Heart Disease (Probability: {proba:.2f})")
    else:
        st.success(f" Low risk of Heart Disease (Probability: {proba:.2f})")
