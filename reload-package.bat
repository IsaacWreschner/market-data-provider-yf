@echo off
echo [BUILD] Building the package...

REM Check if build module is installed
py -c "import build" 2>nul
if errorlevel 1 (
    echo [ERROR] Build module not found. Installing build...
    pip install build
    if errorlevel 1 (
        echo [ERROR] Failed to install build module
        pause
        exit /b 1
    )
)

python -m build
if errorlevel 1 (
    echo [ERROR] Build failed
    pause
    exit /b 1
)

:: Find the most recently modified .whl file
for /f "delims=" %%f in ('dir /b /a:-d /o-d dist\*.whl') do (
    set "WHEEL_FILE=dist\%%f"
    goto :found
)

echo [INSTALL] Installing %WHEEL_FILE%...
pip install --force-reinstall %WHEEL_FILE%
if errorlevel 1 (
    echo [ERROR] Installation failed
    pause
    exit /b 1
)

echo [SUCCESS] Package reloaded successfully!
pause

