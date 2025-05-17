import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ci.utils import load_config
from azureml.core import Workspace, Model
import joblib

config = load_config()

ws = Workspace.get(name=config['workspace_name'],
                   subscription_id=config['subscription_id'],
                   resource_group=config['resource_group'])

model = joblib.load('outputs/linear_model.pkl')
model_path = 'outputs/linear_model.pkl'
registered_model = Model.register(workspace=ws,
                                   model_path=model_path,
                                   model_name='linear_model')
print(f'Model registered: {registered_model.name}')
