import json
import numpy as np
import joblib

def init():
    global model
    model = joblib.load("model.pkl")

def run(data):
    try:
        data = json.loads(data)
        prediction = model.predict(np.array(data['features']).reshape(1, -1))
        return prediction.tolist()
    except Exception as e:
        return str(e)
