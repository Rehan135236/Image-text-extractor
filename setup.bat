@echo off
echo ========================================
echo Image Text Extractor Setup
echo ========================================
echo.

echo Step 1: Installing Python packages...
pip install -r requirements.txt
echo.

echo Step 2: Checking Tesseract OCR...
echo.
echo Tesseract OCR is required for text extraction.
echo.
echo If not installed, download from:
echo https://github.com/UB-Mannheim/tesseract/wiki
echo.
echo During installation, make sure to:
echo - Check "Add to PATH" option
echo - Or note the installation path (usually C:\Program Files\Tesseract-OCR)
echo.

pause

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the application, execute:
echo python image_text_extractor.py
echo.
pause
