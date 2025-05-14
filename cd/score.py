import joblib
import json
import pandas as pd

def init():
    global model
    model = joblib.load("model.pkl")

def run(data):
    try:
        input_df = pd.DataFrame(json.loads(data)["data"])
        return {"result": model.predict(input_df).tolist()}
    except Exception as e:
        return {"error": str(e)}
