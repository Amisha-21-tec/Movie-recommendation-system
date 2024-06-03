import streamlit as st

st.title("Contact Us")

title = st.text_input( 'Your Name')
title = st.text_input( 'Your Email')
title = st.text_input( 'Type message here')

if st.button('Submit'):
    st.success('Successfully submited', icon="✅")