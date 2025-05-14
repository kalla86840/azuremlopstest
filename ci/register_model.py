from azureml.core import Workspace, Model

ws = Workspace.from_config()

model = Model.register(
    workspace=ws,
    model_path="model.pkl",
    model_name="linear_regression_model"
)

print(f"Model registered: {model.name}, version: {model.version}")
