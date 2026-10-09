@echo off
setlocal
cd /d "%~dp0"
py -3 -m pip install pyinstaller==6.16.0
if errorlevel 1 goto failed
py -3 -m unittest discover -s tests -v
if errorlevel 1 goto failed
py -3 -m PyInstaller --clean --noconfirm --onefile --windowed --name "Suspicious-Link-Inspector" app.py
if errorlevel 1 goto failed
echo.
echo EXE ready: dist\Suspicious-Link-Inspector.exe
pause
exit /b 0
:failed
echo Build failed. See details above.
pause
exit /b 1
