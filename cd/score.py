
import joblib
import numpy as np
import json

def init():
    global model
    model = joblib.load('model.joblib')

def run(raw_data):
    try:
        data = np.array(json.loads(raw_data)['data'])
        predictions = model.predict(data)
        return predictions.tolist()
    except Exception as e:
        return str(e)
