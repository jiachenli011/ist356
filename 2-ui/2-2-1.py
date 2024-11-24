import streamlit as st

st.title('Area and permieter')
length = st.number_input("Enter Length:")
width = st.number_input("Enter Width:")
calculate = st.button('Calculate')
clear = st.button('Clear')

if calculate:
    if length and width:
        area = length * width
        perm = 2 * (length + width)
        st.write(f"Area: {area}")
        st.write(f"Perimeter: {perm}")
    else:
        st.error(f"missing length or width")

if clear:
    length = None
    width = None