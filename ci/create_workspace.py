from azureml.core import Workspace
from azureml.core.authentication import InteractiveLoginAuthentication

interactive_auth = InteractiveLoginAuthentication()

ws = Workspace.create(
    name="mymodelworkpace",
    subscription_id="2735eac8-e053-4d04-ad5f-83d5f236217b",
    resource_group="mylnmodel",
    location="eastus",
    create_resource_group=True,
    exist_ok=True,
    auth=interactive_auth
)

ws.write_config()
print(f"Workspace 'mymodelworkpace' in resource group 'mylnmodel' is ready.")
