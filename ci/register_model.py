from azureml.core import Workspace, Model
ws = Workspace.from_config()
model = Model.register(workspace=ws, model_path='outputs/model.pkl', model_name='car_price_model')
print("Model registered:", model.name)
