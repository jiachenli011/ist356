import pandas as pd
import streamlit as st

from check_functions import clean_currency

# load the checks dataset into a dataframe
url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv"
df = pd.read_csv(url)

#clean the `total amount of check` and `gratuity` columns
df['total_amount_of_cleaned'] = df['total amount of check'].apply(clean_currency)
df['gratuity_cleaned'] = df['gratuity'].apply(clean_currency)

# calculate the `price_per_item`  as total amount of check / total items on check
df['price_per_item'] = df['total_amount_of_cleaned'] / df['total items on check']

# calculate the `price_per_person` as total amont of check / party size
df['price_per_person'] = df['total_amount_of_cleaned'] / df['party size']

# calculate the `items_per_person` as total items on check / party size
df['items_per_person'] = df['total items on check'] / df['party size']

# calculate the `tip_percentage` as the total amount of gratuity / check 
df['tip_percentage'] = df['gratuity_cleaned'] / df['total_amount_of_cleaned'] 

# display the dataframe
st.dataframe(df)

# describe the dataframe
st.dataframe(df.describe())

'''
    - import streamlit, pandas and your clean_currency function
    - load the checks dataset into a dataframe: 
    - clean the `total amount of check` and `gratuity` columns
    - calculate the `price_per_item`  as total amount of check / total items on check
    - calcualte the `price_per_person` as total amont of check / party size
    - calcualte the `items_per_person` as total items on check / party size
    - calcualte the `tip_percentage` as the total amount of check / gratuity
    - display dataframe
    - describe dataframe
'''
