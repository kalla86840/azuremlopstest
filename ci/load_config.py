import json
import os

def load_config(config_path='ci/config.json'):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    with open(config_path, 'r') as f:
        config = json.load(f)

    return config

if __name__ == "__main__":
    config = load_config()
    print("Subscription ID:", config.get("subscription_id"))
    print("Resource Group:", config.get("resource_group"))
    print("Workspace Name:", config.get("workspace_name"))
