@echo off
echo ========================================
echo     Mobile Text Extractor Web App
echo ========================================
echo.
echo Starting web server...
echo.
echo IMPORTANT: To access from your phone:
echo 1. Make sure your phone and PC are on the same WiFi
echo 2. Look for the IP address below
echo 3. Open your phone browser and visit: http://[IP_ADDRESS]:5000
echo.
echo For example: http://192.168.1.100:5000
echo.
echo ========================================
echo Your Local IP Address:
ipconfig | findstr /i "IPv4"
echo ========================================
echo.
echo Starting server...
echo.
python mobile_web_app.py
pause
