from flask import Flask, request
import hashlib

app = Flask(__name__)

@app.route('/md5', methods=['POST'])
def md5():
    
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file'].read()

    md5_hash = hashlib.md5(file).hexdigest()

    return md5_hash

if __name__ == '__main__':
    app.run(debug=True)
