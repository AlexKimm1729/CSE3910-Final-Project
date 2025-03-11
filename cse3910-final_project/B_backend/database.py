# database.py
"""
Title: database creation
Author: Yousuf Mohammed
Author: Alex Kim
Date-Created: 2022-11-01
"""


# --- FUNCTIONS --- #
def createDatabase():
    """
    Creates the highscore database needed for the game
    """
    import sqlite3

    db = sqlite3.connect('highscore.db')
    data = db.cursor()

    data.execute(
        'CREATE TABLE IF NOT EXISTS HIGHSCORES (player_id INTEGER PRIMARY KEY AUTOINCREMENT, player_name VARCHAR(100) NOT NULL, score INT, datetime DATETIME NOT NULL, password VARCHAR(100) NOT NULL);')


# --- MAIN PROGRAM CODE --- #
if __name__ == "__main__":
    createDatabase()
