from azureml.core import Workspace

def create_workspace(subscription_id, resource_group, workspace_name, location):
    ws = Workspace.create(
        name=workspace_name,
        subscription_id=subscription_id,
        resource_group=resource_group,
        location=location,
        create_resource_group=False,
        exist_ok=True,
        show_output=True
    )
    ws.write_config()
    print(f"✅ Workspace '{workspace_name}' created and saved to config.")
    return ws

# Example usage:
# create_workspace("2735eac8-e053-4d04-ad5f-83d5f236217b", "DevOps_AzureML_Demo_rg2", "AzureML_Demo_ws1", "westus2")
