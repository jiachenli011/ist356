import streamlit as st

amount = st.number_input("Amount:")
col1,col2 = st.columns(2)
btn_add = col1.button('Add to Total')
btn_clear = col2.button('Clear')

if 'total' not in st.session_state:
    st.session_state.total = 0.0
if 'amount' not in st.session_state:
    st.session_state.amount = 0.0

if btn_add:
    st.session_state.total += amount
    st.write(f"TOTAL: {st.session_state.total}")

if btn_clear:
    st.session_state.total = 0.0
    st.session_state.amount = None
    st.rerun
