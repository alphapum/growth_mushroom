from flask import Flask, request, jsonify
import base64
from PIL import Image
import io
import os

app = Flask(__name__)

# โฟลเดอร์เก็บภาพที่แปลงจาก base64
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/decode_base64_to_image', methods=['POST'])
def decode_base64_to_image():
    try:
        data = request.json
        base64_str = data['base64']
        filename = data.get('filename', './79.jpg')

        # แปลง base64 เป็น binary
        image_data = base64.b64decode(base64_str)

        # บันทึกเป็นไฟล์ภาพ
        image_path = os.path.join(UPLOAD_FOLDER, filename)
        with open(image_path, 'wb') as f:
            f.write(image_data)

        return jsonify({'message': 'Image saved successfully', 'path': image_path})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/encode_image_to_base64', methods=['POST'])
def encode_image_to_base64():
    try:
        data = request.json
        image_path = data['image_path']

        # โหลดและแปลงภาพเป็น base64
        with open(image_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        return jsonify({'base64': encoded_string})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
