from azureml.core import Workspace

def create_workspace(subscription_id, resource_group, workspace_name, location):
    ws = Workspace.create(
        name=workspace_name,
        subscription_id="2735eac8-e053-4d04-ad5f-83d5f236217b",
        resource_group=resource_group,
        location="westus2",
        exist_ok=True,
        show_output=True
    )
    ws.write_config()
    print(f"✅ Workspace '{workspace_name}' created and saved to config.")
    return ws
