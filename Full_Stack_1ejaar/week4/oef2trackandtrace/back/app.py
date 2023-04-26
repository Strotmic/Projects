from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

dict_postpakketten = {
    "s007": {
        "naam": "Laprudence",
        "postcode": 9000,
        "afgifte": "2023-01-01",
        "sorteercentrum": "2023-01-02",
        "onderweg": None,
        "bezorgd": None
    },
    "s008": {
        "naam": "Waeyaert",
        "postcode": 8500,
        "afgifte": "2022-11-11",
        "sorteercentrum": "2022-11-15",
        "onderweg": "2022-11-16",
        "bezorgd": "2022-11-17"
    },
    "s009": {
        "naam": "Laprudence",
        "postcode": 9000,
        "afgifte": "2022-02-02",
        "sorteercentrum": None,
        "onderweg": None,
        "bezorgd": None
    },
    "s010": {
        "naam": "Roobrouck",
        "postcode": 8500,
        "afgifte": "2022-01-05",
        "sorteercentrum": "2022-01-06",
        "onderweg": "2022-01-06",
        "bezorgd": None
    }
}


@app.route('/')
def hello_world():
    return 'Gebruik de api om de data op te vragen'


@app.route('/api/v1/trace/', methods=['GET','POST'])
def track_alles():
    if request.method =='POST':
            data = request.form
            pakketnr = data['trace-nr']
            naam = data['name-recipient']
            postcode = data['postcode-recipient']

            print(f'pakket {pakketnr} met zender {naam} en postcode {postcode}')

            dict_postpakketten.update({pakketnr:{'naam':naam,'postcode':postcode}})

    return jsonify(dict_postpakketten),200

@app.route('/api/v1/trace/<string:code>/', methods=['GET','POST'])
def track_by_code(code):
    try:
        if request.method == 'GET':
            if code in dict_postpakketten.keys():
                print(f'de gevonden code is {code}')
                pakket_info = dict_postpakketten[code]
                return jsonify(detail=pakket_info, trackcode=code),200
            else:
                return jsonify(status='error'), 404
        
    except Exception as e:
        print(e)
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
