from azureml.core import Workspace
from ci.load_config import load_config

config = load_config()

ws = Workspace.create(
    name=config["workspace_name"],
    subscription_id=config["subscription_id"],
    resource_group=config["resource_group"],
    create_resource_group=True,
    location='eastus'
)
ws.write_config()
print("Workspace created and config written.")
