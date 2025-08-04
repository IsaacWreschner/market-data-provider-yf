#!/bin/bash

# Exit immediately if any command fails
set -e

echo "📦 Building the package..."

# Check if build module is installed
if ! python -c "import build" 2>/dev/null; then
    echo "❌ Build module not found. Installing build..."
    pip install build
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install build module"
        exit 1
    fi
fi

# Build the wheel and sdist
python -m build
if [ $? -ne 0 ]; then
    echo "❌ Build failed"
    exit 1
fi

# Find the latest wheel file in the dist folder
WHEEL_FILE=$(ls -t dist/*.whl | head -n 1)

# Check if wheel file exists
if [ -z "$WHEEL_FILE" ]; then
    echo "❌ No wheel file found in dist directory"
    exit 1
fi

# Install the wheel
echo "📥 Installing $WHEEL_FILE..."
pip install --force-reinstall "$WHEEL_FILE"
if [ $? -ne 0 ]; then
    echo "❌ Installation failed"
    exit 1
fi

echo "✅ Package reloaded successfully!"
