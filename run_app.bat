@echo off
title Crop Disease Prediction - Streamlit App
echo.
echo  ============================================================
echo   Crop Disease Prediction Using Machine Learning
echo  ============================================================
echo.
echo  Starting Streamlit with Python 3.11 (TensorFlow 2.21.0)...
echo  Please wait while the Machine Learning model loads into memory...
echo.

cd /d "%~dp0"

:: Open browser after a short delay (3 seconds) to let Streamlit start
start "" /B cmd /C "timeout /t 3 /nobreak >nul && start http://localhost:8501"

:: Run the Streamlit app using absolute path to app.py
C:\Users\ELCOT\Documents\python311\python.exe -m streamlit run "C:\Users\ELCOT\Documents\Crop_Disease_Prediction_Project\app.py" --server.port=8501 --server.headless=true --browser.gatherUsageStats=false

pause
