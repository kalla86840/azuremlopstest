from azureml.core import Workspace, Model

subscription_id = "2735eac8-e053-4d04-ad5f-83d5f236217b"
resource_group = "mlopstest1"
workspace_name = "mlopstest1"
location = "westus2"

# Create the workspace if it doesn't exist
ws = Workspace.create(
    name=workspace_name,
    subscription_id=subscription_id,
    resource_group=resource_group,
    location=location,
    exist_ok=True,
    show_output=True
)

# Register the model
model = Model.register(
    workspace=ws,
    model_path="outputs/linear_model.pkl",
    model_name="linear_model"
)

print(f"✅ Registered model: {model.name}, version: {model.version}")
