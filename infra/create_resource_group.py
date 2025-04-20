import subprocess

def create_resource_group(subscription_id, resource_group, location):
    subprocess.run([
        "az", "group", "create",
        "--name", resource_group,
        "--location", location,
        "--subscription", subscription_id
    ], check=True)
    print(f"✅ Resource group '{resource_group}' created.")
