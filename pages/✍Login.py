import streamlit as st
import datetime

st.title("Login")

title = st.text_input( 'Your Name')
title = st.text_input( 'Your Email')
title = st.text_input( 'Enter your password')

if st.button('Submit'):
    st.success('Successfully submited', icon="✅")
