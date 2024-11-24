''' Geocode
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/google/geocode?location=Syracuse%EF%BC%8CNY' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 6dc7c26dca49955fbe1cb3ba'
'''

''' Weather
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/weather/current?units=imperial&lon=-78&lat=43' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 6dc7c26dca49955fbe1cb3ba'
'''

import requests
import streamlit as st

st.title('Weather ☁️')
location = st.text_input('Enter a location')
if st.button:
    url = 'https://cent.ischool-iot.net/api/google/geocode'
    querystring = {"location": location}
    headers = { "X-API-KEY": '6dc7c26dca49955fbe1cb3ba'}
    response = requests.get(url, params=querystring, headers=headers)
    response.raise_for_status()
    geocode = response.json()
    lon = geocode['results'][0]['geometry']['location']['lng']
    lat = geocode['results'][0]['geometry']['location']['lat']

    url = 'https://cent.ischool-iot.net/api/weather/current'
    querystring = {"units": "imperial", "lon": lon, "lat": lat}
    headers = { "X-API-KEY": '6dc7c26dca49955fbe1cb3ba'}
    response = requests.get(url, params=querystring, headers=headers)
    response.raise_for_status()
    weather = response.json()
    temp = weather['current']['temperature_2m']
    st.write(f'The current temperature in {location} is {temp}°F')
