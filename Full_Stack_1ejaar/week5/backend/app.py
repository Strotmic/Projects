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


@app.route(endpoint + '/klanten/', methods=['GET', 'POST'])
def get_klanten():
    if request.method == 'GET':
        # data van alle klanten opvragen aan de database
        data = DataRepository.read_klanten()
        # print(data)
        return jsonify(klanten=data), 200
    elif request.method == 'POST':
        input = DataRepository.json_or_formdata(request)
        data = DataRepository.create_klant(
            input['FNaam'], input['VNaam'], input['Straat'], input['Nummer'], input['Postcode'], input['Gemeente'])
        if data != None:
            return jsonify(klantID=data), 201
        else:
            return jsonify(message='error'), 500


@app.route(endpoint + "/klanten/<klantid>/", methods=['GET', 'PUT','DELETE'])
def klant(klantid):
    if request.method == 'GET':
        # data van de klant met klantid terugegven
        data = DataRepository.read_klant(klantid)
        if data != None:
            return jsonify(klanten=data), 200
        else:
            return jsonify(message='error'), 404
    elif request.method == 'PUT':
        input = DataRepository.json_or_formdata(request)
        data = DataRepository.update_klant(
            input['FNaam'], input['VNaam'], input['Straat'], input['Nummer'], input['Postcode'], input['Gemeente'], klantid)
        if data != None:
            if data>0:
                return jsonify(KlantID=klantid,message='Geupdate'), 200
            else:
                return jsonify(message='Niet geupdate'), 200
        else:
            return jsonify(message='error'), 500
    elif request.method == "DELETE":
        data= DataRepository.delete_klant(klantid)
        return jsonify(message=data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
