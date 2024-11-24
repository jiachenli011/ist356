'''
https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv

Let's build an interactive pivot table in streamlit!

- create a row and column selection widgets allowing the user to select one of the following columns:  
`'Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade'`
- create a measure column selestion widget which allows the user to select one of these columns:  
`'Completion_Time','Student_Score'`
- build the pivot table dataframe from the inputs. use the average for the `aggfunc`
- display the pivot table!

'''

import streamlit as st
import pandas as pd

url = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv'
df = pd.read_csv(url)

# create a row and column selection widgets allowing the user to select one of the following columns:  
# 'Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade'`
selections = ['Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade']
row_slection = st.selectbox('Select a row', selections)

if row_slection in selections:
   selections.remove(row_slection)
coloum_selection = st.selectbox('Select a column', selections)
#if row_slections and coloum_selection:
 #   st.warning('Please select a different row or a column')
 #   st.stop()
measure_selection = st.selectbox('Select a measure', ['Completion_Time','Student_Score'])
df_pivot =  df.pivot_table(index=row_slection, columns=coloum_selection, values=measure_selection, aggfunc='mean')
st.dataframe(df_pivot)