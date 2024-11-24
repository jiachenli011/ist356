import pandas as pd
import numpy as np
import streamlit as st

link = "http://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv"
customers = pd.read_csv(link)

choice = st.radio("Select Gender: ",["M","F"])
cols = st.multiselect("Select column:", customers.columnsx)

gender_index = customers["Gender"]==choice

st.dataframe(customers[gender_index][cols])
