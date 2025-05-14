from azureml.core import Workspace, Environment
from azureml.core.model import InferenceConfig, Model
from azureml.core.webservice import AciWebservice

ws = Workspace.from_config()
model = Model(ws, name='car_price_model')

env = Environment(name="deploy-env")
env.python.user_managed_dependencies = False
env.docker.enabled = True
env.python.conda_dependencies.add_pip_package("joblib")

inference_config = InferenceConfig(entry_script="cd/score.py", environment=env)
deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

service = Model.deploy(ws, "car-price-service", [model], inference_config, deployment_config)
service.wait_for_deployment(show_output=True)
print(service.scoring_uri)
