#!/bin/bash

echo "📦 Starting environment setup..."

# Show Python version
echo "🐍 Python version:"
python --version

# Install latest compatible Azure CLI version
echo "🔧 Installing Azure CLI version 2.71.0..."
pip install azure-cli==2.71.0

# Install Azure ML SDK with CLI support
echo "🔧 Installing Azure ML SDK with CLI support..."
pip install --upgrade azureml-sdk[cli]

# Install additional requirements
echo "🔧 Installing project dependencies..."
pip install -r requirements.txt

echo "✅ Environment setup complete."
