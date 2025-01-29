import streamlit as st
import joblib
import numpy as np
import os
import pickle

# with open("credit_card_model.pkl", "rb") as file:
#     model = pickle.load(file)
# print("Model loaded successfully!")

# print(os.path.exists("credit_card_model.pkl"))

# Load the trained model
model = joblib.load("credit_card_model.pkl")

# Title of the web app
st.title("Credit Card Fraud Detection")

st.code("Created By Olagidi Joshua, Matthews Victoria, Okafor Lisa, Salami Lateefat, Ubaka Amazing-Grace, Oyekanmi Eniola")

# Input fields for the features
st.header("Enter the transaction details")

# Create input fields for each feature
input_data = []
features = [
    "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10",
    "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19",
    "V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "Amount"
]

for feature in features:
    value = st.number_input(f"{feature}", format="%.6f")
    input_data.append(value)

# Convert input data to numpy array
input_array = np.array(input_data).reshape(1, -1)

# Predict button
if st.button("Predict"):
    # Make prediction
    prediction = model.predict(input_array)

    # Display the result
    if prediction[0] == 0:
        st.success("Normal Transaction")
    else:
        st.error("Fraud Transaction")
    st.balloons()


# Instructions or additional information
st.markdown("""
### Instructions:
- Enter the values for each feature (V1 to V28 and Amount).
- Click the "Predict" button to see if the transaction is normal or fraudulent.
""")