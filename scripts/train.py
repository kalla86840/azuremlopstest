import pandas as pd
import joblib
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from azureml.core import Run, Workspace, Model

run = Run.get_context()
ws = run.experiment.workspace

data = pd.read_csv('data/data.csv')
X = data.drop(columns=['target'])
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

run.log("mse", mse)
run.log("r2", r2)

os.makedirs('outputs', exist_ok=True)
model_path = 'outputs/linear_model.pkl'
joblib.dump(model, model_path)
run.upload_file(name='outputs/linear_model.pkl', path_or_stream=model_path)

model = Model.register(
    workspace=ws,
    model_path=model_path,
    model_name='linear-model',
    tags={"model_type": "LinearRegression"},
    description="A linear regression model for predicting target"
)

print(f"Registered model: {model.name}, version: {model.version}")
