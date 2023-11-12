import streamlit as st

st.header("st.selectbox")

option = st.selectbox("What is your favorite color?", ("Blue", "Red", "Green", "Teal"))

st.write("Your favorite color is ", option)
