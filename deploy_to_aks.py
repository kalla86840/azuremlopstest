from azureml.core import Workspace, Model, Environment, InferenceConfig
from azureml.core.compute import AksCompute, ComputeTarget
from azureml.core.webservice import AksWebservice

# Load workspace with static values
ws = Workspace.get(
    name="AzureML_Demo_ws1",
    subscription_id="2735eac8-e053-4d04-ad5f-83d5f236217b",
    resource_group="DevOps_AzureML_Demo_rg2"
)

# Load registered model
model = Model(ws, name="linear-model")

# Create inference configuration
env = Environment.from_conda_specification(name="linear-env", file_path="environment/conda.yml")
inference_config = InferenceConfig(entry_script="scripts/score.py", environment=env)

# Create or attach to existing AKS cluster
aks_name = "prod-cluster"
if aks_name in ws.compute_targets:
    aks_target = ws.compute_targets[aks_name]
    if aks_target and type(aks_target) is AksCompute:
        print(f"✅ Using existing AKS cluster: {aks_name}")
else:
    prov_config = AksCompute.provisioning_configuration(location="westus2")
    aks_target = ComputeTarget.create(workspace=ws, name=aks_name, provisioning_configuration=prov_config)
    aks_target.wait_for_completion(show_output=True)

# Define deployment config with logging and monitoring
deployment_config = AksWebservice.deploy_configuration(
    cpu_cores=1,
    memory_gb=1,
    auth_enabled=True,
    enable_app_insights=True,
    collect_model_data=True
)

# Deploy the model
service = Model.deploy(
    workspace=ws,
    name="linear-model-service",
    models=[model],
    inference_config=inference_config,
    deployment_config=deployment_config,
    deployment_target=aks_target,
    overwrite=True
)

service.wait_for_deployment(show_output=True)
print(f"✅ Service deployed to AKS. Scoring URI: {service.scoring_uri}")
