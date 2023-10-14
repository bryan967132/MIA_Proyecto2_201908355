from flask import Flask, jsonify, request
from flask_cors import CORS
from Language.Parser import *
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def obtener_productos():
    return jsonify({'response': 'success'})

@app.route('/parse', methods=['POST'])
def mkdisk():
    parser.parse(request.json['command'])
    return jsonify({'response': 'mkdisk success'})

if __name__ == '__main__':
    os.system('clear')
    app.run(debug = True, port = 5000)