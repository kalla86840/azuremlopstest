from azureml.core import Workspace, Model
from ci.load_config import load_config

config = load_config()

ws = Workspace.get(
    name=config["workspace_name"],
    subscription_id=config["subscription_id"],
    resource_group=config["resource_group"]
)

model = Model.register(workspace=ws, model_path='outputs/model.pkl', model_name='car_price_model')
print("Model registered:", model.name)
