import streamlit as st
import requests

def get_text_completion(query: str) -> dict:
    url = 'https://cent.ischool-iot.net/api/openai/generate'
    data = {'query': query}
    headers = { "X-API-KEY": '6dc7c26dca49955fbe1cb3ba'}
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    result = response.json()
    return result


st.title("Fisrt GPT")
text = st.text_area('Enter some text')
if text:
    with st.spinner('Generating text...'):
        result = get_text_completion(text)
        st.write(result)