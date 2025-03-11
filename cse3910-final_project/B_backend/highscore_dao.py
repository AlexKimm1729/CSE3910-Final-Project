# highscore_dao.py
"""
Title: Highscore_dao
Author: Yousuf Mohammed
Author: Alex Kim
Date-Created: 2022-11-01
"""

# --- IMPORTS --- #
import sqlite3
from flask import jsonify
from datetime import *


# --- FUNCTIONS --- #
def insertHighscore(highscore):
    """
    Inserts a new highscore into the database
    """
    conn = sqlite3.connect('../B_backend/highscore.db')
    c = conn.cursor()
    highscoreData = (highscore['player_name'], highscore['score'], date.today().strftime("%b-%d-%Y"), highscore['password'])

    c.execute('INSERT INTO HIGHSCORES(player_name, score, datetime, password) VALUES (?, ?, ?, ?)', highscoreData)

    conn.commit()
    conn.close()


def updateHighscore(name, score):
    """
    Updates a highscore in the database
    """
    conn = sqlite3.connect('../B_backend/highscore.db')
    c = conn.cursor()

    info = [score, name]
    c.execute('''
        UPDATE HIGHSCORES 
        SET score = ? 
        WHERE player_name = ?
    ;''', info)

    conn.commit()
    conn.close()


def getHighscores():
    """
    Gets all highscores as well as the data related to the score
    """
    conn = sqlite3.connect('B_backend/highscore.db')
    c = conn.cursor()

    c.execute('SELECT * FROM HIGHSCORES')

    response = []
    for (player_id, player_name, score, dt, password) in c:
        response.append({'player_id': player_id, 'player_name': player_name, 'score': score, 'datetime': dt})

    conn.close()
    return jsonify(response)


# --- MAIN PROGRAM CODE --- #
if __name__ == "__main__":
    insertHighscore({
        'player_name': 'ALEX',
        'score': '1',
        'datetime': date.today().strftime("%b, %d, %Y")
    })
    #updateHighscore("ALEX", 20)
