#!/bin/bash

# Exit immediately if any command fails
set -e

# Build the wheel and sdist
echo "📦 Building the package..."
python -m build

# Find the latest wheel file in the dist folder
WHEEL_FILE=$(ls -t dist/*.whl | head -n 1)

# Install the wheel
echo "📥 Installing $WHEEL_FILE..."
pip install --force-reinstall "$WHEEL_FILE"

echo "✅ Package reloaded successfully!"
