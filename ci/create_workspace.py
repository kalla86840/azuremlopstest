from azureml.core import Workspace

ws = Workspace.create(
    name='mlops-workspace',
    subscription_id='2735eac8-e053-4d04-ad5f-83d5f236217b',
    resource_group='mlops-rg',
    create_resource_group=True,
    location='eastus'
)
ws.write_config()
