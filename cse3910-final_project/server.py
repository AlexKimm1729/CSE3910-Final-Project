# server.py
"""
Title: Flask server
Author: Yousuf Mohammed
Author: Alex Kim
Date-Created: 2022-11-01
"""

# --- IMPORTS --- #
from flask import *
import json
from B_backend.highscore_dao import *


# --- FLASK APP --- #
app = Flask(__name__)


@app.route('/insertHighscore', methods=['POST'])
def insert_highscore():
    """
    Inserts a new player highscore into the server
    """
    request_payload = json.loads(request.form['data'])
    player_id = insertHighscore(request_payload)
    response = jsonify({'player_id': player_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getHighscores', methods=['GET'])
def get_highscores():
    """
    gets all highscores from the server
    """
    response = getHighscores()
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/', methods=['GET', 'POST'])
def highscore():
    """
    Creates the main website server
    """
    return render_template('highscore.html')


# --- MAIN PROGRAM CODE --- #
if __name__ == "__main__":
    app.run(port=51000)
