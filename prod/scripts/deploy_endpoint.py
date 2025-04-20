from azureml.core import Workspace, Model, Environment
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AciWebservice

# Automatically create or reuse the workspace
ws = Workspace.create(
    name="mlopstest1",
    subscription_id="2735eac8-e053-4d04-ad5f-83d5f236217b",
    resource_group="mlopstest1",
    location="westus2",
    exist_ok=True,
    show_output=True
)

model = Model(ws, "linear_model")

env = Environment.from_conda_specification(
    name="linear-env",
    file_path="environment/conda.yml"
)

inference_config = InferenceConfig(
    entry_script="scripts/score.py",
    environment=env
)

deployment_config = AciWebservice.deploy_configuration(
    cpu_cores=1,
    memory_gb=1,
    auth_enabled=True,
    tags={"stage": "prod"},
    description="ACI deployment for linear regression"
)

service = Model.deploy(
    workspace=ws,
    name="linear-endpoint",
    models=[model],
    inference_config=inference_config,
    deployment_config=deployment_config,
    overwrite=True
)

service.wait_for_deployment(show_output=True)
print(f"✅ Endpoint deployed at: {service.scoring_uri}")
