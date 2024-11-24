'''
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/funnyname/random?n=3' \
  -H 'accept: application/json'
'''

import requests
url = "https://cent.ischool-iot.net/api/funnyname/random"
querystring = {"n":"3"}
response = requests.get(url, params=querystring)
response.raise_for_status()
name = response.json()
for name in name:
    print(name['first'],name['last'])