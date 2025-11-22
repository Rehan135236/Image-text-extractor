from flask import Flask, render_template, request, jsonify
from PIL import Image
import pytesseract
import os
import base64
from io import BytesIO

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_text():
    try:
        files = request.files.getlist('images')
        results = []
        
        for idx, file in enumerate(files, 1):
            if file:
                # Read image
                image = Image.open(file.stream)
                
                # Extract text
                text = pytesseract.image_to_string(image)
                
                results.append({
                    'filename': file.filename,
                    'text': text,
                    'index': idx
                })
        
        return jsonify({'success': True, 'results': results})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Run on all interfaces so mobile can access
    app.run(host='0.0.0.0', port=5000, debug=True)
