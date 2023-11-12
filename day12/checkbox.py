import streamlit as st

st.header("Question for Kana")

st.write("What should we have for dinner tomorrow?")

salmon_don = st.checkbox("Salmon don")
chinese_pack = st.checkbox("Chinese pack")
white_stew = st.checkbox("White stew")

if salmon_don:
    st.write("Need to get some salmon")

if chinese_pack:
    st.write("Okay, which one would you like?")

if white_stew:
    st.write("Because it's getting cold, right?")
