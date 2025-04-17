from azureml.core import Workspace, Model, Environment
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AciWebservice

ws = Workspace.from_config()

model = Model.register(
    workspace=ws,
    model_path='outputs/linear_model.pkl',
    model_name='linear-model',
    tags={"type": "linear_regression"},
    description="Simple Linear Regression model"
)

env = Environment.from_conda_specification(name="linear-env", file_path="environment/conda.yml")
inference_config = InferenceConfig(entry_script="scripts/score.py", environment=env)

deployment_config = AciWebservice.deploy_configuration(
    cpu_cores=1,
    memory_gb=0.5,
    auth_enabled=False,
    description="Low-cost linear regression deployment"
)

service = Model.deploy(
    workspace=ws,
    name="linear-regression-endpoint",
    models=[model],
    inference_config=inference_config,
    deployment_config=deployment_config,
    overwrite=True
)

service.wait_for_deployment(show_output=True)
print(f"Endpoint URI: {service.scoring_uri}")
