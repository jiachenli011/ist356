import pandas as pd
import streamlit as st

def grade(participation: float) -> str:
    if participation == 0.0:
        return "AB"
    
    if participation <= 0.5:
        return "np"
    
    return "+"

# extract roster
roster_url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/roster.csv"
roster_df = pd.read_csv(roster_url)

# extract poll data
polls = []
dates = ["2024-01-08", "2024-01-15", "2024-01-22","2024-01-29"]
for date in dates:
    # read in each poll
    poll = f"https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/poll-responses-{date}.csv"
    poll_df = pd.read_csv(poll)
    # add lineage
    poll_df["date"] = date
    # add poll to list
    polls.append(poll_df)

# combine all polls
poll_df = pd.concat(polls,ignore_index=True)
st.dataframe(poll_df)
st.dataframe(roster_df)

# Transformation
combined_df = pd.merge(roster_df,poll_df,how='left',left_on='netid',right_on='student_id')

# poll counts by each date
poll_counts = combined_df.pivot_table(index='date',values='poll_num',aggfunc='max')

# count of student response by date
student_responses = combined_df.pivot_table(
    index='netid',columns="date",values='answer',aggfunc='count')
student_responses = student_responses.fillna(0) # replace NaN with 0

# change student polls responses to percentages
for col in student_responses:
    student_responses[col] = student_responses[col] / poll_counts.loc[col,"poll_num"]

# convert percentages to grades
for col in student_responses.columns:
    student_responses[col] = student_responses[col].apply(grade)


summary = student_responses.copy()
summary['sessions'] = len(summary.columns)
summary['AB'] = summary.apply(lambda row: row.value_counts().get('AB',0), axis=1)
summary['np'] = summary.apply(lambda row: row.value_counts().get('np',0), axis=1)
summary['Pct'] = (summary['AB'] + summary['np']) / summary['sessions']

summary_with_names = pd.merge(roster_df,summary,left_on='netid',right_index=True)

st.title("Student Polls Report")
st.dataframe(summary_with_names)
st.download_button("Download CSV",data=summary_with_names.to_csv(), file_name="polls.csv")

#st.dataframe(summary_with_names)
#st.dataframe(combined_df)
#st.dataframe(student_responses)
#st.dataframe(poll_counts)

