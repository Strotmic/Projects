from repositories.DataRepository import DataRepository
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Custom endpoint
endpoint = '/api/v1'


@app.route('/')
def index():
    return "Please go to API path", 403
    # return redirect("/api/v1/klanten", code=302)

@app.route(endpoint + '/klanten/', methods=['GET'])
def get_klanten():
    if request.method == 'GET':
        # data van alle klanten opvragen aan de database
        data = DataRepository.read_klanten()
        # print(data)
    return jsonify(klanten=data), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
