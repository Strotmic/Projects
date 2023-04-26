from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)

#communicatie toelaten met API
CORS(app)

dictStock = {   100: {'naam': 'T-shirt', 'prijs': 18},
                101: {'naam': 'Pull', 'prijs': 22},
                102: {'naam': 'Koffietas', 'prijs': 11}
            }


@app.route('/')
def hello_world():
    return 'Ga naar de API url', 200

@app.route('/api/v1/products/', methods=['GET'])
def producten():
    return jsonify(dictStock),200

@app.route('/api/v1/payment/', methods=['POST'])
def betaling():
    try:
        data = request.form
        aantal = int(data['aantal'])
        product_id = int(data['product'])
        if 0<aantal<100 and product_id in dictStock.keys():
            prijs = dictStock[product_id]['prijs'] *aantal
            return jsonify(status='success'),200
        else:
            return jsonify(status='warning', message='waarden niet correct'),400
    except Exception as c:
        return jsonify(status='error',error=c),500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
