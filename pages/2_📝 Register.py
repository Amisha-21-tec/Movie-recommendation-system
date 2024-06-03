import streamlit as st
import datetime

st.title("Register")

title = st.text_input( 'Your Name')
title = st.text_input( 'Your Email')

genre = st.radio("Gender",('Male', 'Female', 'Other'))
if genre == 'Male':
    st.write("")
else:
    st.write("")

d = st.date_input(
    "Enter your birth date",
    datetime.date(2000, 1, 1))

title = st.text_input( 'Enter password')
title = st.text_input( 'confirm password')

if st.button('Submit'):
    st.success('Successfully submited', icon="✅")

