#!/bin/bash

echo "📦 Installing required Python packages..."

# Show Python version
python --version

# Install from Dev and Prod requirements
pip install -r dev/requirements.txt
pip install -r prod/requirements.txt

# Confirm azureml-core install
pip show azureml-core || echo "❌ azureml-core not found after install"

echo "✅ Installation complete."
