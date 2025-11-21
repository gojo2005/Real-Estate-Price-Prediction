import streamlit as st
from predict_module import predict_price

st.title("🏠 House Price Prediction")

# Input fields
bedrooms = st.number_input("Bedrooms", 1, 10, 3)
bathrooms = st.number_input("Bathrooms", 1, 10, 2)
sqft_living = st.number_input("Living Area (sqft)", 100, 10000, 2000)
sqft_lot = st.number_input("Lot Area (sqft)", 100, 20000, 5000)
floors = st.number_input("Floors", 1, 3, 1)
yr_built = st.number_input("Year Built", 1900, 2025, 2000)
yr_renovated = st.number_input("Year Renovated", 0, 2025, 0)
has_basement = st.checkbox("Has Basement?")
city = st.selectbox("City", ["Seattle", "Bellevue", "Redmond"])
statezip = st.text_input("StateZip", "WA 98133")

if st.button("Predict Price"):
    input_data = {
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "sqft_living": sqft_living,
        "sqft_lot": sqft_lot,
        "floors": floors,
        "yr_built": yr_built,
        "yr_renovated": yr_renovated,
        "sqft_basement": 200 if has_basement else 0,
        "city": city,
        "statezip": statezip
    }
    price = predict_price(input_data)
    st.success(f"Estimated House Price: ${price:,.2f}")
