import streamlit as st
x = 0
if st.button('Click me'):
    x = x+10
    st.write(x)