from azureml.core import Workspace, Model

def register_model(model_path, model_name):
    ws = Workspace.from_config()
    model = Model.register(
        workspace=ws,
        model_path=model_path,
        model_name=model_name,
        description="Linear regression model"
    )
    print(f"✅ Model registered: {model.name}, version {model.version}")
    return model

# Example usage:
# register_model("outputs/linear_model.pkl", "linear-model")
