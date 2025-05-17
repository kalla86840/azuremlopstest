import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ci.utils import load_config
from azureml.core import Workspace, Environment, Model
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core.model import InferenceConfig

config = load_config()

ws = Workspace.get(name=config['workspace_name'],
                   subscription_id=config['subscription_id'],
                   resource_group=config['resource_group'])

model = Model(ws, 'linear_model')

env = Environment(name='inference-env')
env.python.conda_dependencies.add_pip_package('scikit-learn')
env.python.conda_dependencies.add_pip_package('joblib')

inference_config = InferenceConfig(entry_script='cd/score.py', environment=env)

deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

service = Model.deploy(workspace=ws,
                       name='linear-model-service',
                       models=[model],
                       inference_config=inference_config,
                       deployment_config=deployment_config)
service.wait_for_deployment(show_output=True)
print(service.scoring_uri)
