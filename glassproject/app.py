import streamlit as st
import pickle
import numpy as np


with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)


glass_types = {
    1: "Building Windows Float Processed",
    2: "Building Windows Non Float Processed",
    3: "Vehicle Windows Float Processed",
    4: "Vehicle Windows Non Float Processed",
    5: "Containers",
    6: "Tableware",
    7: "Headlamps"
}

st.title("Glass Type Classifier")


st.header("Enter Physical Properties")
RI = st.number_input("Refractive Index")
Na = st.number_input("Sodium")
Mg = st.number_input("Magnesium")
Al = st.number_input("Aluminum")
Si = st.number_input("Silicon")
K = st.number_input("Potassium")
Ca = st.number_input("Calcium")
Ba = st.number_input("Barium")
Fe = st.number_input("Iron")


if st.button("Predict Glass Type"):
    features = np.array([[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]])
    prediction = model.predict(features)[0]
    glass_name = glass_types.get(prediction, "Unknown")

    st.success(f"Predicted Glass Type: {glass_name}")
