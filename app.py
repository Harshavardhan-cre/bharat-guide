from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

user_state = {
    "current_doc": None,
    "step": 0,
    "answers": {}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/filter', methods=['POST'])
def filter_schemes():
    data = request.json
    # Dummy response for now
    schemes = [
        {"name": "PM Awas Yojana", "desc": "Affordable housing for all."},
        {"name": "PM Ujjwala Yojana", "desc": "Free LPG connections to women from BPL households."}
    ]
    return jsonify(schemes)

@app.route('/downloads/<path:filename>')
def download(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
