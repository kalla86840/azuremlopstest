from azureml.core import Workspace, Model, Environment, InferenceConfig
from azureml.core.webservice import AciWebservice

# Connect to workspace
ws = Workspace.get(
    name="AzureML_Demo_ws1",
    subscription_id="2735eac8-e053-4d04-ad5f-83d5f236217b",
    resource_group="DevOps_AzureML_Demo_rg2"
)

# Load the registered model
model = Model(ws, name="linear-model")

# Define environment
env = Environment.from_conda_specification(name="linear-env", file_path="environment/conda.yml")

# Define inference configuration
inference_config = InferenceConfig(
    entry_script="scripts/score.py",
    environment=env
)

# Define ACI deployment configuration
deployment_config = AciWebservice.deploy_configuration(
    cpu_cores=1,
    memory_gb=1,
    auth_enabled=True,
    tags={"endpoint": "linear-regression"},
    description="ACI endpoint for linear regression model"
)

# Deploy the model to ACI
service = Model.deploy(
    workspace=ws,
    name="linear-model-endpoint",
    models=[model],
    inference_config=inference_config,
    deployment_config=deployment_config,
    overwrite=True
)

service.wait_for_deployment(show_output=True)
print(f"✅ Endpoint created. URI: {service.scoring_uri}")
