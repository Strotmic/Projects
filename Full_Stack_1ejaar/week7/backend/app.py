from repositories.DataRepository import DataRepository
from flask import Flask, jsonify, request
from flask_cors import CORS

# Start app
app = Flask(__name__)
CORS(app)

# Custom endpoint
endpoint = '/api/v1'

# ROUTES


@app.route(endpoint + '/treinen/', methods=['GET', 'POST'])
def get_treinen():
    if request.method == 'GET':
        x = DataRepository.read_treinen()
        return jsonify(data=x), 200
    elif request.method == 'POST':
        input = DataRepository.json_or_formdata(request)
        # vertrek, bestemmingID, spoor, vertragin, afgeschaft
        data = DataRepository.create_trein(
            input['vertrek'], input['bestemmingID'], input['spoor'], input['vertraging'], input['afgeschaft'])
        if data != None:
            return jsonify(treinid=data), 201
        else:
            return jsonify(message='error'), 500


@app.route(endpoint+'/treinen/<treinid>/', methods=['GET', 'PUT', 'DELETE'])
def get_trein(treinid):
    if request.method == 'GET':
        # data van de klant met klantid terugegven
        data = DataRepository.read_trein(treinid)
        if data != None:
            return jsonify(treinen=data), 200
        else:
            return jsonify(message='error'), 404

    elif request.method == 'PUT':
        input = DataRepository.json_or_formdata(request)
        # vertrek, bestemmingID, spoor, vertragin, afgeschaft
        data = DataRepository.update_trein(
            input['vertrek'], input['bestemmingID'], input['spoor'], input['vertraging'], input['afgeschaft'], treinid)
        if data != None:
            if data > 0:
                return jsonify(trein=treinid, message='Geupdate'), 200
            else:
                return jsonify(message='Niet geupdate'), 200
        else:
            return jsonify(message='error'), 500

    elif request.method == 'DELETE':
        data = DataRepository.delete_trein(treinid)
        return jsonify(data=data)


@app.route(endpoint + '/bestemmingen/', methods=['GET'])
def get_bestemmingen():
    if request.method == 'GET':
        x = DataRepository.read_bestemmingen()
        return jsonify(data=x), 200


@app.route(endpoint+'/treinen/bestemming/<bestemmingid>/', methods=['GET'])
def get_trein_met_bestemming(bestemmingid):
    if request.method == 'GET':
        data = DataRepository.read_treinen_met_bestemming(bestemmingid)
        if data != None:
            if len(data) > 0:
                return jsonify(data=data, message='Geupdate'), 200
            else:
                return jsonify(message='Niet geupdate'), 200
        else:
            return jsonify(message='error'), 404


@app.route(endpoint + '/treinen/<treinid>/vertraging/', methods=['PUT'])
def get_vertraging(treinid):
    input = DataRepository.json_or_formdata(request)
    data = DataRepository.update_trein_vertraging(treinid, input['vertraging'])
    if data != None:
        return jsonify(trein=data), 200
    else:
        return jsonify(message='error'), 404


# Start app
if __name__ == '__main__':
    app.run(debug=True)
