import streamlit as st
st.title("LifePulse-AI")
st.write("WELCOME TO LIFEPULSE-AI")
mood = st.slider("How was your day? (1-5)", 1, 5)
st.write("You rated your day:", mood)