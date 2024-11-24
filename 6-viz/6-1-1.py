'''
## Challenge 6-1-1

Using the `data/mobile_user_behavior_dataset.csv` file, create a streamlit to show:

1. the data in a dataframe 
2. select a category: gender or operating system
3. select a measure: Data useage, battery drain, screen on time, or app useage time
4. show a bar plot of the average of 3. by 2.

'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mobile = pd.read_csv('./6-viz/data/mobile_user_behavior_dataset.csv')
st.dataframe(mobile)

category = st.selectbox('Select a category', 
                        ['Gender', 'Operating System'])

plot,series = plt.subplots()
sns.barplot(data = mobile, 
            x = category, 
            y = 'Data Usage (MB/day)',
            estimator = 'mean', 
            errorbar = None, 
            ax = series)
st.pyplot(plot)