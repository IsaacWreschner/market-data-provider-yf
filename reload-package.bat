@echo off
echo 📦 Building the package...
python -m build

for %%f in (dist\*.whl) do (
    set "WHEEL_FILE=%%f"
    goto :found
)
:found

echo 📥 Installing %WHEEL_FILE%...
pip install --force-reinstall %WHEEL_FILE%

echo ✅ Package reloaded successfully!
pause
