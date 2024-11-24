import requests
import pandas as pd
import streamlit as st

st.title('First API')

url = "https://jsonplaceholder.typicode.com/users/"
response = requests.get(url)
response.raise_for_status()
users = response.json()

users_df = pd.json_normalize(users)
st.dataframe(users_df)