import streamlit as st 
from streamlit_gsheets import GSheetsConnection 
import pandas as pd 

# Display Title and Description 
st.title("Vendor Management Portal") 
st.markdown("Enter the details of the new vendor below.") 

# Establishing a Google Sheets connection 
conn = st.experimental_connection("gsheets", type=GsheetsConnection) 

# Fetch existing vendors data 
existing_data = conn.read(worksheet="Vendors", usecols=list(range(6)), ttl=5)
existing_data = existing_data.dropna(how="all")


 # List of Business Types and Products 
BUSINESS_TYPES = [ 
    "Manufacturer", 
    "Distributor", 
    "Wholesaler", 
    "Retailer", 
    "Service Provider",
 ]
PRODUCTS = [ 
    "Electronics" 
    "Apparel", 
    "Groceries", 
    "Software", 
    "Other" 
]
            
            
            
# Onboarding New Vendor Form 
with st.form(key="vendor_form"): 
    company_name = st.text_input(label="Company Name*") 
    business_type = st.selectbox("Business Type*", options=BUSINESS_TYPES, index=None) 
    products = st.multiselect("Products offered", options=PRODUCTS) 
    years_in_business = st.slider("Years in Business", 0, 50, 5) 
    onboarding_datè = st.date_input(label="Onboarding Date") 
    additional_info = st.text_area(label="Additional Notes") 
    
# Mark mandatory fields 
st.markdown("**required*") 
submit_button = st.form_submit_button(label="Submit Vendor Details")