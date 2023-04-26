from repositories.DataRepository import DataRepository
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Custom endpoint
endpoint = '/api/v1'


@app.route('/')
def index():
    return redirect("/api/v1/bestemmingen_ok/527", code=302)


@app.route(endpoint + '/bestemmingen_ok/<id>')
def bestemming_ok(id):
    if request.method == 'GET':
        data = DataRepository.read_bestemming_ok(id)
        if data is not None:
            return jsonify(data), 200
        else:
            return jsonify(message='error'), 404


@app.route(endpoint + '/bestemmingen_nok/<id>')
def bestemming_nok(id):
    if request.method == 'GET':
        data = DataRepository.read_bestemming_nok(id)
        if data is not None:
            return jsonify(data), 200
        else:
            return jsonify(message='error'), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
