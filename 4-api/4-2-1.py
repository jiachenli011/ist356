import streamlit as st
import requests
import pandas as pd

def extract_entities(text: str) -> dict:
    url = 'https://cent.ischool-iot.net/api/azure/entityrecognition'
    data = {'text': text}
    headers = { "X-API-KEY": '6dc7c26dca49955fbe1cb3ba'}
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    entities = response.json()
    return entities

text = st.text_area('Enter some text')
if text:
    result = extract_entities(text)
    st.write(result)

    entities = result['results']['documents'][0]['entities']
    df = pd.DataFrame(entities)
    st.dataframe(df)