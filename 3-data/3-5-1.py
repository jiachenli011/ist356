'''
https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv
'''

import pandas as pd
import streamlit as st

url = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv'
df = pd.read_csv(url)

'''
Create a streamlit to allow the user to select one of the following:

- one of: Made_Own_Study_Guide, Did_Exam_Prep Assignment, Studied_In_Groups	
- after the selection is made display a dataframe that summarized the count of students and the average student score by the selection
'''

selected = st.selectbox('Select an option', ['Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups'])

grouped = df.groupby(selected).agg({'Student':'count', 'Score':'mean'})
st.dataframe(grouped)