#!/bin/bash
set -e
echo "Creating workspace..."
python ../ci/create_workspace.py
echo "Installing requirements..."
pip install -r ../ci/requirements.txt
echo "Training model..."
python ../ci/train.py
echo "Evaluating model..."
python ../ci/model_eval.py
echo "Registering model..."
python ../ci/register_model.py
echo "Deploying model..."
pip install -r requirements.txt
python deploy.py
