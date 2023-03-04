# Loader.py
"""
Title: Loader
Author: Yousuf Mohammed
Author: Alex Kim
Date-Created: 2022-11-01
"""


class Color:
    GREY = (50,50,50)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    MAGENTA = (255,0,255)


class Sound:
    import pygame
    pygame.mixer.init()

    SWOOSH_SOUND = pygame.mixer.Sound("audio/sfx_swoosh.wav")
    SWOOSH_SOUND.set_volume(0.5)

    FLAPPING_SOUND = pygame.mixer.Sound("audio/sfx_wing.wav")
    FLAPPING_SOUND.set_volume(0.5)

    POINT_SOUND = pygame.mixer.Sound("audio/sfx_point.wav")
    POINT_SOUND.set_volume(0.5)

    HIT_SOUND = pygame.mixer.Sound("audio/sfx_hit.wav")
    HIT_SOUND.set_volume(0.2)


def getInfo(name):
    import sqlite3

    NAME = [name]
    conn = sqlite3.connect('../B_backend/highscore.db')
    c = conn.cursor()
    old_highscore = c.execute('''
        SELECT score
        FROM HIGHSCORES 
        WHERE player_name = ?
        ;''', NAME).fetchone()
    password = c.execute('''
        SELECT password
        FROM HIGHSCORES 
        WHERE player_name = ?
        ;''', NAME).fetchone()

    if old_highscore == None:
        old_highscore = [0,]
        old_highscore_1 = [0,0,0]

    old_highscore_1 = [int(d) for d in str(old_highscore[0])]
    while len(old_highscore_1) != 3:
        old_highscore_1.insert(0, 0)
    return old_highscore, old_highscore_1, NAME, password

def sortInfo():
    import sqlite3

    conn = sqlite3.connect('../B_backend/highscore.db')
    c = conn.cursor()
    data = c.execute('''
        SELECT *
        FROM HIGHSCORES 
        ORDER BY score
        ;''').fetchall()

    data.sort(key=lambda x: x[2], reverse=True)

    list = []
    for i in range(len(data)):
        list.append((data[i][1], data[i][2], data[i][3], data[i][4], i+1))
        c.execute('''
            UPDATE HIGHSCORES 
            SET 
                player_name = ?,
                score = ?,
                datetime = ?,
                password = ?
            WHERE player_id = ?
            ;''', (list[i]))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    sortInfo()

