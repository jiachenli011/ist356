import pandas as pd
import streamlit as st

base = "https://github.com/mafudge/datasets/tree/master/minimart"

customers = pd.read_csv(base + '/customers.csv')

st.dataframe(customers)
months = ["jan","feb","mar","apr"]
months_df = []
for month in months:
    month_df = pd.read_csv(base + f"/purchases-{months}.csv")
    month_df["month"] = month
    months_df.append(month_df)

purchases = pd.concat(months_df)
combined = pd.merge(customers,purchases,on="customer_id",how = "left")
st.write("Combined data")
selected_month = st.selectbox("Select a month",months)
filtered = combined[combined["month"] == selected_month]
no_purchase = filtered[filtered["order_id"].isna()]
st.dataframe(no_purchase) 