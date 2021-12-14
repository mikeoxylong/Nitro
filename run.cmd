@echo off
TITLE Nitro for Windows
>nul 2>nul assoc .py
if errorlevel 1 (
    echo Please install python
    PAUSE
)
echo Found python, checking for packages
py -m pip install keyboard
py -m pip install selenium
py -m pip install webdriver_manager
echo Installed packages, running...
py main.py
