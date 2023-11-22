import streamlit as st

st.set_page_config(layout="wide")

st.title("良い夫婦の日")

with st.expander("From our wedding day ..."):
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/wedding1.jpeg",
        width=340,
    )
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/wedding2.jpeg",
        width=340,
    )

with st.expander("... and our honeymoon ..."):
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/honeymoon1.jpeg",
        width=340,
    )
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/honeymoon2.jpeg",
        width=340,
    )

with st.expander("... to our trips ..."):
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/trip1.jpeg",
        width=340,
    )
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/trip2.jpeg",
        width=340,
    )
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/trip3.jpeg",
        width=340,
    )

with st.expander("... and the birth of our daughter ..."):
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/emma1.jpeg",
        width=340,
    )
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/emma2.jpeg",
        width=340,
    )
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/emma3.jpeg",
        width=340,
    )

with st.expander("... (and everything inbetween) ..."):
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/night_in1.jpeg",
        width=340,
    )
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/drive1.jpeg",
        width=340,
    )
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/pregnant.jpeg",
        width=340,
    )

with st.expander("... thank you for always being there."):
    st.image(
        "/Users/richardcollins/Streamlit-30-day-challenge/day19/there.jpeg",
        width=340,
    )
st.write(
        "I love you :)"
    )