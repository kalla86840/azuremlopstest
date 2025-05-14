from azureml.core import Workspace, Environment, Model
from azureml.core.webservice import AciWebservice
from azureml.core.model import InferenceConfig

ws = Workspace.from_config()
model = Model(ws, name="linear_regression_model")

env = Environment.from_conda_specification(name="lr-env", file_path="ci/environment.yml")
inference_config = InferenceConfig(entry_script="cd/score.py", environment=env)

deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

service = Model.deploy(
    workspace=ws,
    name="lr-endpoint",
    models=[model],
    inference_config=inference_config,
    deployment_config=deployment_config,
    overwrite=True
)
service.wait_for_deployment(show_output=True)
print(f"Deployed to: {service.scoring_uri}")
