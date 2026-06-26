# streamlit for frontend
import streamlit as st
import requests

st.title("Student Grade Predictor")

# taking number inputs for the independent variables
socio = st.number_input("Socioeconomic Score")

study = st.number_input("Study Hours")

sleep = st.number_input("Sleep Hours")

attendance = st.number_input("Attendance (%)")

if st.button("Predict"):

    data = {
        "socioeconomic_score": socio,
        "study_hours": study,
        "sleep_hours": sleep,
        "attendance": attendance
    }
# sending data to the Flask API
    response = requests.post(
        "http://127.0.0.1:5000/predict",
        json=data
    )

    result = response.json()

    st.success(
        f"Predicted Grade: {result['predicted_grade']}"
    )