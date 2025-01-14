import streamlit as st
import pickle
import pandas as pd

# Load the model
with open('xgboost_model.sav', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("E-commerce Customer Churn Prediction")

# Input form
st.header("Input Data")

# Features
tenure = st.number_input(
    "Tenure (months)", 
    value=15, 
    min_value=0, 
    max_value=61, 
    step=5,  # Step to ensure integer input
    help="Length of time the customer has used the service (0-61 months)."
)
warehouse_to_home = st.number_input(
    "Distance from Warehouse to Home (km)", 
    value=10.0, 
    min_value=5.0, 
    max_value=127.0, 
    help="Distance between the warehouse and the customer's home in kilometers (5-127 km)."
)
num_devices = st.number_input(
    "Number of Registered Devices", 
    value=4, 
    min_value=1, 
    max_value=6, 
    step=1,  # Step to ensure integer input
    help="Number of devices registered in the customer's account (1-6 devices)."
)
prefered_order_cat = st.selectbox(
    "Preferred Order Category", 
    ["Laptop & Accessory", "Mobile Phone", "Fashion", "Others", "Grocery"], 
    help="The most frequently chosen order category by the customer."
)
satisfaction_score = st.slider(
    "Satisfaction Score (1-5)", 
    min_value=1, 
    max_value=5, 
    value=3, 
    help="Customer's satisfaction score with the service (1-5)."
)
marital_status = st.selectbox(
    "Marital Status", 
    ["Single", "Married", "Divorced"], 
    help="Customer's marital status."
)
num_address = st.number_input(
    "Number of Registered Addresses", 
    value=2, 
    min_value=1, 
    max_value=22, 
    step=1,  # Step to ensure integer input
    help="Number of addresses registered on the customer's account (1-22 addresses)."
)
complain = st.selectbox(
    "Has Complained?", 
    [0, 1], 
    format_func=lambda x: "Yes" if x == 1 else "No", 
    help="Has the customer ever complained? (0: No, 1: Yes)."
)
days_since_last_order = st.number_input(
    "Days Since Last Order", 
    value=7, 
    min_value=0, 
    max_value=46, 
    step=1,  # Step to ensure integer input
    help="Number of days since the customer last ordered (0-46 days)."
)
cashback_amount = st.number_input(
    "Cashback Amount ($", 
    value=143.32, 
    min_value=0.0, 
    max_value=324.99, 
    help="Amount of cashback received by the customer in Dollars (0-324.99)."
)

# Create DataFrame with the exact column names used during training
input_data = pd.DataFrame({
    "Tenure": [tenure],
    "WarehouseToHome": [warehouse_to_home],
    "NumberOfDeviceRegistered": [num_devices],
    "PreferedOrderCat": [prefered_order_cat],
    "SatisfactionScore": [satisfaction_score],
    "MaritalStatus": [marital_status],
    "NumberOfAddress": [num_address],
    "Complain": [complain],
    "DaySinceLastOrder": [days_since_last_order],
    "CashbackAmount": [cashback_amount]
})

# Prediction button
if st.button("Predict"):
    # Make prediction directly
    prediction = model.predict(input_data)[0]
    churn_label = "Yes" if prediction == 1 else "No"

    # Styling for the result box
    if churn_label == "Yes":
        result_html = f"""
        <div style="background-color: #FF6F61; padding: 10px; border-radius: 10px; text-align: center; font-size: 20px; color: white;">
            <strong>Churn Prediction: {churn_label}</strong>
        </div>
        """
    else:
        result_html = f"""
        <div style="background-color: #4CAF50; padding: 10px; border-radius: 10px; text-align: center; font-size: 20px; color: white;">
            <strong>Churn Prediction: {churn_label}</strong>
        </div>
        """
    
    # Display result with styling
    st.markdown(result_html, unsafe_allow_html=True)
