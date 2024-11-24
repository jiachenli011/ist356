import pandas as pd
import requests
import streamlit as st

link = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(link)
employees = response.json()

df_list = []
for key in employees.keys():
    df = pd.DataFrame(employees["accounting"])
    df["department"] = key
    df_list.append(df)

combined_df = pd.concat(df_list)

st.dataframe(combined_df)