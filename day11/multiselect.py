import streamlit as st

st.header("st.multiselect")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue", "Teal"],
    ["Yellow", "Red", "Teal"],
)

st.write("You selected:", options)
