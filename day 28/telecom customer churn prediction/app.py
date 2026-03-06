import streamlit as st
import joblib
import numpy as np

# Load model & scaler
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("📊 Telecom Customer Churn Prediction")

st.write("Enter customer details below:")

tenure = st.slider("Tenure (Months)", 0, 72)
monthly = st.number_input("Monthly Charges", min_value=0.0)
total = st.number_input("Total Charges", min_value=0.0)

if st.button("Predict Churn"):

    # Create dummy input array (IMPORTANT)
    input_data = np.zeros((1, scaler.n_features_in_))

    # Put values in correct positions
    input_data[0][0] = tenure
    input_data[0][1] = monthly
    input_data[0][2] = total

    # Scale
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction[0] == 1:
        st.error(f"⚠ Customer Likely to Churn (Risk: {probability*100:.2f}%)")
    else:
        st.success(f"✅ Customer Not Likely to Churn (Risk: {probability*100:.2f}%)")