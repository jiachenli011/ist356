'''
## Challenge 3-2-1

Read this file into a pandas dataframe:

[https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log]
- What is the delimiter?
- is there a header? Which row?
- Do you need to skip lines?

Display only data where the time taken > 500 (msec) and the sc-status is 200

as a streamlit
'''

import streamlit as st
import pandas as pd

file = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log", skiprows=3, header=0, sep=" ")
st.dataframe(file)



