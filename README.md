# 📸 Image Text Extractor

A powerful cross-platform OCR (Optical Character Recognition) application that extracts text from images. Available as a **Desktop App**, **Mobile Web App**, and **Android APK**.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Android%20%7C%20Web-lightgrey.svg)

## ✨ Features

- 📁 **Batch Processing** - Extract text from 50, 100, 200+ images at once
- 🎨 **Beautiful Modern UI** - Clean, intuitive interface with gradient design
- 📱 **Multi-Platform** - Desktop, Mobile Web, and Android APK
- 📋 **Copy to Clipboard** - One-click copy functionality
- 💾 **Export to File** - Save extracted text as .txt files
- 🚀 **Fast & Accurate** - Powered by Tesseract OCR engine
- 🌐 **No Internet Required** - Works completely offline (desktop version)

## 🛠️ Tech Stack

### Desktop Application
- **Python 3.8+**
- **Tkinter** - GUI framework
- **Pillow (PIL)** - Image processing
- **Tesseract OCR** - Text extraction engine
- **pytesseract** - Python wrapper for Tesseract

### Mobile Web Application
- **Flask** - Web framework
- **HTML5/CSS3/JavaScript** - Frontend
- **Responsive Design** - Mobile-first approach
- **RESTful API** - Backend architecture

### Android Application
- **Python for Android (p4a)**
- **Kivy** - Cross-platform GUI framework
- **Buildozer** - Android packaging tool
- **PIL/Pillow** - Image processing

## 📦 Installation

### Desktop App (Windows)

1. Clone the repository:
```bash
git clone https://github.com/Rehan135236/image-text-extractor.git
cd image-text-extractor
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Tesseract OCR:
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Install and add to PATH

4. Run the application:
```bash
python image_text_extractor.py
```

Or simply double-click `run.bat`

### Mobile Web App

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the web server:
```bash
python mobile_web_app.py
```

3. Access from your phone browser:
   - Find your PC's IP address
   - Visit: `http://YOUR_IP:5000`

Or simply double-click `RUN_MOBILE_APP.bat`

### Android APK

Build using Google Colab:
1. Open `BUILD_APK_COLAB.ipynb` in Google Colab
2. Upload `main.py` and `buildozer.spec`
3. Run all cells
4. Download the generated APK
5. Install on your Android device

## 🚀 Usage

### Desktop App
1. Launch the application
2. Click **"📁 Select Images"** button
3. Choose single or multiple images (Ctrl+Click for multiple)
4. Text is automatically extracted
5. Click **"📋 Copy Text"** to copy or **"💾 Save File"** to export

### Mobile Web App
1. Open browser on your phone
2. Navigate to the server URL
3. Tap or drag & drop images
4. Click **"📸 Extract Text"**
5. Copy or download the extracted text


### Desktop Application
- Modern Windows desktop interface
- Batch processing with progress tracking
- Clean text output with file separators

### Mobile Web App
- Responsive gradient design
- Touch-optimized controls
- Drag & drop support

## 🏗️ Project Structure

```
image-text-extractor/
├── image_text_extractor.py    # Desktop app (Tkinter)
├── mobile_web_app.py           # Mobile web app (Flask)
├── main.py                     # Android app (Kivy)
├── buildozer.spec              # Android build config
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # Mobile web interface
├── run.bat                     # Desktop launcher
├── RUN_MOBILE_APP.bat          # Web app launcher
└── BUILD_APK_COLAB.ipynb       # Colab build notebook

```

## 🔧 Configuration

### Tesseract Path
Update the Tesseract path in the code if needed:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Web App Port
Change the port in `mobile_web_app.py`:

```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

## 🌟 Key Highlights

- ⚡ **Fast Processing** - Handles hundreds of images efficiently
- 🎯 **High Accuracy** - Industry-standard Tesseract OCR
- 💻 **Cross-Platform** - Windows, Web, and Android
- 🎨 **Modern UI** - Beautiful, user-friendly design
- 📦 **Easy Deployment** - Multiple distribution options

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - OCR Engine
- [Kivy](https://kivy.org/) - Mobile framework
- [Flask](https://flask.palletsprojects.com/) - Web framework

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ using Python**

