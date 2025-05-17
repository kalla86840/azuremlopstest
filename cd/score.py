import joblib
import numpy as np
import json

def init():
    global model
    model = joblib.load('linear_model.pkl')

def run(data):
    try:
        inputs = np.array(json.loads(data)['data'])
        result = model.predict(inputs).tolist()
        return result
    except Exception as e:
        return str(e)
