from azureml.core import Workspace, Model

ws = Workspace.from_config()
model = Model.register(
    workspace=ws,
    model_path="outputs/linear_model.pkl",
    model_name="linear_model"
)

print(f"✅ Registered model: {model.name}, version: {model.version}")
