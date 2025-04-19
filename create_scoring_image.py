from azureml.core import Workspace, Environment, Model, InferenceConfig
from azureml.core.model import ModelPackage

def create_scoring_image(model_name):
    ws = Workspace.from_config()

    model = Model(ws, name=model_name)
    env = Environment.from_conda_specification(name="linear-env", file_path="environment/conda.yml")
    inference_config = InferenceConfig(entry_script="scripts/score.py", environment=env)

    package = Model.package(
        workspace=ws,
        models=[model],
        inference_config=inference_config,
        generate_dockerfile=True
    )

    package.wait_for_creation(show_output=True)
    print(f"✅ Docker image URI: {package.location}")
    return package

# Example usage:
# create_scoring_image("linear-model")
