import streamlit as st
import joblib
import numpy as np
import os

os.system("pip install -r requirements.txt")


# Load the trained model
model = joblib.load("LR_bank_churn_model.pkl")

# Define categorical mappings
gender_map = {'Male': 0, 'Female': 1}
education_level_map = {'High School': 0, 'HS Graduate': 1, 'Uneducated': 2, 'Unknown': 3, 'College': 4, 'College Graduate': 5, 'Doctorate': 6}
marital_status_map = {'Married': 0, 'Single': 1, 'Unknown': 2, 'Divorced': 3}
card_category_map = {'Blue': 0, 'Gold': 1, 'Silver': 2, 'Platinum': 3}
income_category_map = {'Less than 40k': 0, '40-60k': 1, '60-80k': 2, '80-120k': 3, 'Unknown': 4}

# Streamlit UI
st.title("Customer Churn Prediction")

st.header("Enter Customer Details")

# User Inputs

customer_age = st.number_input("Enter Customer Age", min_value=1, max_value=100)
gender = st.selectbox("Gender", list(gender_map.keys()))
dependent_count = st.number_input("Number of Dependents (e.g children, spouse, or other family members) (0-5)", min_value=0, max_value=10)
education_level = st.selectbox("Education Level", list(education_level_map.keys()))
marital_status = st.selectbox("Marital Status", list(marital_status_map.keys()))
income_category = st.selectbox("Income Category", list(income_category_map.keys()))
card_category = st.selectbox("Card Category", list(card_category_map.keys()))
months_on_book = st.number_input("Enter Account Total of Months Active", min_value=0, max_value=100)
total_relationship_count = st.number_input("Total number of accounts or financial products the customer has with the bank ", min_value=0, max_value=100)
months_inactive_12_mon = st.number_input("Enter number of Years account is Inactive", min_value=0, max_value=100)
contacts_count_12_mon = st.number_input("Enter Number of Accounts Inactive for Years", min_value=0, max_value=10)
credit_limit = st.number_input("Enter Maximum Credit Limit", min_value=1, max_value=100000000)
total_revolving_bal = st.number_input("Enter Total Revolving Balance in Account", min_value=0, max_value=100000000)
avg_open_to_buy = st.number_input("Enter Average amount of credit available to the customer on a revolving credit account", min_value=0, max_value=100000000)
total_amt_chng_q4_q1 = st.number_input("Enter change in total transaction amount from Quarter 4 to Quarter 1", min_value=0, max_value=100000000)
total_trans_amt = st.number_input("Enter Total Transaction Amount", min_value=0, max_value=100000000)
total_trans_ct = st.number_input("Enter Total Transaction Count", min_value=0, max_value=100000000)
total_ct_chng_q4_q1 = st.number_input("Enter change in total transaction Count from Quarter 4 to Quarter 1", min_value=0, max_value=100000000)
avg_utilization_ratio = st.number_input("Enter average ratio of credit card balance to credit limit over a period", min_value=0, max_value=100000000)


# Convert inputs to numerical values
gender_encoded = gender_map[gender]
education_encoded = education_level_map[education_level]
marital_status_encoded = marital_status_map[marital_status]
income_encoded = income_category_map[income_category]
card_encoded = card_category_map[card_category]



# Prepare data for prediction
user_input = np.array([[customer_age, gender_encoded, dependent_count, education_encoded, marital_status_encoded, income_encoded, card_encoded, months_on_book, total_relationship_count, months_inactive_12_mon, contacts_count_12_mon, credit_limit, total_revolving_bal, avg_open_to_buy, total_amt_chng_q4_q1 ,total_trans_amt, total_trans_ct, total_ct_chng_q4_q1, avg_utilization_ratio]])

# Predict button
if st.button("Predict Churn"):
    prediction = model.predict(user_input)
    if prediction[0] == 1:
        st.error("🔴 This customer is likely to churn.")
    else:
        st.success("🟢 This customer is not likely to churn.")
