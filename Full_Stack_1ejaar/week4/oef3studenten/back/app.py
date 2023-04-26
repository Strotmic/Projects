from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

dict_punten = {
    "Blancke":     [{"module": "Full-stack Web Dev", "punt": 16}, {"module": "Sensors & interfacing", "punt": 15}, {"module": "Datamanagement", "punt": 17}, {"module": "UI Design", "punt": 15}, {"module": "Project 1", "punt": 18}],
    "Boddin":     [{"module": "Full-stack Web Dev", "punt": 10}, {"module": "Sensors & interfacing", "punt": 7}, {"module": "Datamanagement", "punt": 10}, {"module": "UI Design", "punt": 1}, {"module": "Project 1", "punt": 9}],
    "Bogaert":    [{"module": "Full-stack Web Dev", "punt": 12}, {"module": "Sensors & interfacing", "punt": 13}, {"module": "Datamanagement", "punt": 14}, {"module": "UI Design", "punt": 15}, {"module": "Project 1", "punt": 11}],
    "Bossuyt":    [{"module": "Full-stack Web Dev", "punt": 14}, {"module": "Sensors & interfacing", "punt": 20}, {"module": "Datamanagement", "punt": 19}, {"module": "UI Design", "punt": 19}, {"module": "Project 1", "punt": 17}],
    "Brion":      [{"module": "Full-stack Web Dev", "punt": 13}, {"module": "Sensors & interfacing", "punt": 12}, {"module": "Datamanagement", "punt": 12}, {"module": "UI Design", "punt": 3}, {"module": "Project 1", "punt": 12}],
    "Brock":      [{"module": "Full-stack Web Dev", "punt": 17}, {"module": "Sensors & interfacing", "punt": 8}, {"module": "Datamanagement", "punt": 11}, {"module": "UI Design", "punt": 13}, {"module": "Project 1", "punt": 17}],
    "Bruggeman":  [{"module": "Full-stack Web Dev", "punt": 8}, {"module": "Sensors & interfacing", "punt": 11}, {"module": "Datamanagement", "punt": 10}, {"module": "UI Design", "punt": 20}, {"module": "Project 1", "punt": 13}],
    "Brutyn":     [{"module": "Full-stack Web Dev", "punt": 11}, {"module": "Sensors & interfacing", "punt": 15}, {"module": "Datamanagement", "punt": 12}, {"module": "UI Design", "punt": 11}, {"module": "Project 1", "punt": 7}],
    "Bulckaen":   [{"module": "Full-stack Web Dev", "punt": 6}, {"module": "Sensors & interfacing", "punt": 5}, {"module": "Datamanagement", "punt": 11}, {"module": "UI Design", "punt": 1}, {"module": "Project 1", "punt": 3}]
}


# start de Flask server met debug
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
