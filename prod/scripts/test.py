import requests
import json

scoring_uri = "<YOUR_ENDPOINT_URL>"
api_key = "<YOUR_API_KEY>"

data = {
    "data": [[5.1, 3.5, 1.4, 0.2]]
}

headers = {
    "Content-Type": "application/json",
}
if api_key:
    headers["Authorization"] = f"Bearer {api_key}"

response = requests.post(scoring_uri, json=data, headers=headers)
print("Response:", response.json())
