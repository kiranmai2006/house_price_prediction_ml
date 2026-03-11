import streamlit as st
import pickle
import numpy as np

# load the trained model
model = pickle.load(open("house_price_model.pkl","rb"))

st.title("🏠 House Price Prediction")

st.write("Enter house details to predict price")

area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
floors = st.number_input("Floors")
yearbuilt = st.number_input("Year Built")
garage = st.number_input("Garage")

if st.button("Predict Price"):

    features = np.array([[area, bedrooms, bathrooms, floors, yearbuilt, garage]])

    prediction = model.predict(features)

    st.success(f"Predicted Price: {prediction[0]}")