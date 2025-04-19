import subprocess

def create_resource_group(subscription_id, resource_group, location):
    cmd = [
        "az", "group", "create",
        "--name", resource_group,
        "--location", location,
        "--subscription", subscription_id
    ]
    subprocess.run(cmd, check=True)
    print(f"✅ Resource group '{resource_group}' created in '{location}'.")

# Example usage:
# create_resource_group("2735eac8-e053-4d04-ad5f-83d5f236217b", "DevOps_AzureML_Demo_rg2", "westus2")
