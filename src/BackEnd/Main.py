from flask import Flask, jsonify, request
from flask_cors import CORS
from Language.Parser import *
from Env.Env import *
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def obtener_productos():
    return jsonify({'response': 'success'})

@app.route('/parse', methods=['POST'])
def parse():
    try:
        response = parser.parse(request.json["command"])[0]
        if not type(response) == dict:
            return jsonify({'response': f'{response} [{request.json["line"]}:1]'})
        return jsonify({'response': f'{response["commentary"]}'})
    except:
        return jsonify({'response': f' -> Error: Comando sin reconocer. [{request.json["line"]}:1]'})

@app.route('/isLogged', methods=['GET'])
def isLogged():
    if currentLogged['User']:
        return jsonify({'isLogged': True})
    return jsonify({'isLogged': False})

if __name__ == '__main__':
    # os.system('clear')
    app.run(debug = True, port = 5000)