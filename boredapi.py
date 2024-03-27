import json

import requests

url = "http://www.boredapi.com/api/activity/?type=cooking"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data["activity"])
