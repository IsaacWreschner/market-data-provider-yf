@echo off
echo 📦 Building the package...

REM Check if build module is installed
py -c "import build" 2>nul
if errorlevel 1 (
    echo ❌ Build module not found. Installing build...
    pip install build
    if errorlevel 1 (
        echo ❌ Failed to install build module
        pause
        exit /b 1
    )
)

python -m build
if errorlevel 1 (
    echo ❌ Build failed
    pause
    exit /b 1
)

for %%f in (dist\*.whl) do (
    set "WHEEL_FILE=%%f"
    goto :found
)
:found

echo 📥 Installing %WHEEL_FILE%...
pip install --force-reinstall %WHEEL_FILE%
if errorlevel 1 (
    echo ❌ Installation failed
    pause
    exit /b 1
)

echo ✅ Package reloaded successfully!
pause
