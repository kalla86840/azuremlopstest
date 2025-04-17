import requests
import json

scoring_uri = "https://linear-regression-endpoint.<region>.azurecontainer.io/score"
headers = {"Content-Type": "application/json"}

input_payload = {
    "data": [
        [5.1, 3.5, 1.4, 0.2],
        [6.2, 2.8, 4.8, 1.8]
    ]
}

response = requests.post(scoring_uri, data=json.dumps(input_payload), headers=headers)
print("Status Code:", response.status_code)
print("Prediction Response:", response.json())
