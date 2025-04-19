import joblib
import numpy as np
import json
import os

def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR', '.'), 'linear_model.pkl')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        inputs = np.array(data)
        preds = model.predict(inputs)
        return {"result": preds.tolist()}
    except Exception as e:
        return {"error": str(e)}
