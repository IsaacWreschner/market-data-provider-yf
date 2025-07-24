@echo off
echo 📦 Building the package...
python -m build

:: Find the most recently modified .whl file
for /f "delims=" %%f in ('dir /b /a:-d /o-d dist\*.whl') do (
    set "WHEEL_FILE=dist\%%f"
    goto :found
)

:found
echo 📥 Installing %WHEEL_FILE%...
pip install --force-reinstall "%WHEEL_FILE%"

echo ✅ Package reloaded successfully!
pause