import streamlit as st
import requests



def openai_complete(prompt: str) -> str:
    params = { "temperature" : 0 }
    url = 'https://cent.ischool-iot.net/api/openai/generate'
    data = {'query': prompt}
    headers = { "X-API-KEY": '6dc7c26dca49955fbe1cb3ba'}
    response = requests.post(url, data=data, headers=headers, params=params)
    response.raise_for_status()
    result = response.json()
    return result

def spellcheck(text):
    prompt = "Please sspell cjec the following text: \n"
    prompt = text + "\n"
    prompt += "for each misspelled word, please provide a correction"
    prompt += "return these as a list of dictionary in JSON format\n"
    response = openai_complete(prompt)
    return response

st.title("Spell Check")
text = st.text_area('Enter some text to spell check')
response = spellcheck(text)
st.write(response)