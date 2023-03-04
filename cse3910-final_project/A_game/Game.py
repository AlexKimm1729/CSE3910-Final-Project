# Game.py
"""
Title: Game class
Author: Yousuf Mohammed
Author: Alex Kim
Date-Created: 2022-11-01
"""

# --- IMPORTS --- #
import random
from Window import Window
from Box import Box
from Image import ImageSprite
from Loader import Sound, getInfo, sortInfo
from B_backend.highscore_dao import updateHighscore, insertHighscore
from datetime import *
from Text import *


# --- CLASSES --- #
class Game:
    """
    The main game engine
    """

    def __init__(self):
        """
        All the settings required for the game
        """

        # <editor-fold desc="SETTINGS">
        self._WINDOW = Window('Bird Flappy', 450, 700, 60)

        self.__PIPE_GAP = 150
        self.__FIRST_RUN = True
        self.__MAXIMUM_BIRD_SPEED = 8
        self.__IMAGE_LOADER = 0
        self.__FRAME_COUNTER = 0
        self.__JUMP_SPEED = -6
        self.__JUMP_DECELERATION = 0.1
        self.__JUMP_LOOP = 3

        self.__ALPHA = 0
        self.__ALPHA_INCREMENT = 5
        self.__CHECK_DONE = False

        self.__ALPHA_2 = 0
        self.__ALPHA_INCREMENT_2 = 13
        self.__CHECK_DONE_2 = False

        self.__ALPHA_3 = 255
        self.__CHECK_DONE_3 = False

        self.__ALPHA_4 = 0

        self.key_count = 0
        self.key_count_2 = 0
        # </editor-fold>

        # <editor-fold desc="PHYSICS">
        self.__TIMES = 0
        self.__GRAVITY = 0.35
        self.__MAX_SPEED = 12
        # self.__BIRD_MASS =
        # self.__FORCE_WING =
        # </editor-fold>

        # <editor-fold desc="BACKGROUND">
        # Land One
        self._LAND_SPRITE_1 = ImageSprite('media/land.png')
        self._LAND_SPRITE_1.setImageWidth(450)
        self._LAND_SPRITE_1.setImageHeight(200)
        self._LAND_SPRITE_1.setPosition(0, (self._WINDOW.getWindowHeight() - self._LAND_SPRITE_1.getScreenHeight()))
        self._LAND_SPRITE_1.setSpeed(-3)

        # Land Two
        self._LAND_SPRITE_2 = ImageSprite('media/land.png')
        self._LAND_SPRITE_2.setImageWidth(450)
        self._LAND_SPRITE_2.setImageHeight(200)
        self._LAND_SPRITE_2.setPosition(self._LAND_SPRITE_1.getScreenWidth(),
                                        (self._WINDOW.getWindowHeight() - self._LAND_SPRITE_2.getScreenHeight()))
        self._LAND_SPRITE_2.setSpeed(-3)

        # Sky One
        self._SKY_SPRITE_1 = ImageSprite('media/sky.png')
        self._SKY_SPRITE_1.setImageWidth(450)
        self._SKY_SPRITE_1.setImageHeight(200)
        self._SKY_SPRITE_1.setPosition(0, (
                    self._WINDOW.getWindowHeight() - self._SKY_SPRITE_1.getScreenHeight() - self._LAND_SPRITE_1.getScreenHeight()))
        self._SKY_SPRITE_1.setSpeed(-1)

        # Sky Two
        self._SKY_SPRITE_2 = ImageSprite('media/sky.png')
        self._SKY_SPRITE_2.setImageWidth(450)
        self._SKY_SPRITE_2.setImageHeight(200)
        self._SKY_SPRITE_2.setPosition(self._SKY_SPRITE_1.getScreenWidth(), (
                    self._WINDOW.getWindowHeight() - self._SKY_SPRITE_2.getScreenHeight() - self._LAND_SPRITE_1.getScreenHeight()))
        self._SKY_SPRITE_2.setSpeed(-1)
        # </editor-fold>

        # <editor-fold desc="SCORE">
        self.SCORE_POINTS = 0
        self.__DISPLAY_SCORE = ImageSprite(f'media/font_big_{self.SCORE_POINTS}.png')
        self.__DISPLAY_SCORE.setPosition(1000, 20)

        self.SCORE_POINTS_2 = 0
        self.__DISPLAY_SCORE_2 = ImageSprite(f'media/font_big_{self.SCORE_POINTS_2}.png')
        self.__DISPLAY_SCORE_2.setPosition(1000, 20)

        self.SCORE_POINTS_3 = 0
        self.__DISPLAY_SCORE_3 = ImageSprite(f'media/font_big_{self.SCORE_POINTS_3}.png')
        self.__DISPLAY_SCORE_3.setPosition(1000, 20)

        self.__DISPLAY_SCORE_END = ImageSprite(f'media/font_small_{self.SCORE_POINTS}.png')
        self.__DISPLAY_SCORE_END.setPosition(313, 210)

        self.__DISPLAY_SCORE_END_2 = ImageSprite(f'media/font_small_{self.SCORE_POINTS_2}.png')
        self.__DISPLAY_SCORE_END_2.setPosition(300, 210)

        self.__DISPLAY_SCORE_END_3 = ImageSprite(f'media/font_small_{self.SCORE_POINTS_3}.png')
        self.__DISPLAY_SCORE_END_3.setPosition(290, 210)

        self.__OLD_HIGHSCORE = [0]
        self.__OLD_HIGHSCORE_2 = [0, 0, 0]
        self.__PLAYER_NAME = ''

        self.__HIGHSCORE = ImageSprite(f'media/font_small_{self.__OLD_HIGHSCORE_2[2]}.png')
        self.__HIGHSCORE.setPosition(313, 260)

        self.__HIGHSCORE_2 = ImageSprite(f'media/font_small_{self.__OLD_HIGHSCORE_2[1]}.png')
        self.__HIGHSCORE_2.setPosition(300, 260)

        self.__HIGHSCORE_3 = ImageSprite(f'media/font_small_{self.__OLD_HIGHSCORE_2[0]}.png')
        self.__HIGHSCORE_3.setPosition(290, 260)

        self.__HIGHSCORE.getScreen().set_alpha(0)
        self.__HIGHSCORE_2.getScreen().set_alpha(0)
        self.__HIGHSCORE_3.getScreen().set_alpha(0)

        # <editor-fold desc="MEDALS">
        self.__BRONZE = ImageSprite('media/bronze_medal.png')
        self.__BRONZE.setScale(7.5)
        self.__BRONZE.setPosition(125, 218)

        self.__SILVER = ImageSprite('media/silver_medal.png')
        self.__SILVER.setScale(7.5)
        self.__SILVER.setPosition(125, 218)

        self.__GOLD = ImageSprite('media/gold_medal.png')
        self.__GOLD.setScale(7.5)
        self.__GOLD.setPosition(125, 218)

        self.__PLATINUM = ImageSprite('media/platinum_medal.png')
        self.__PLATINUM.setScale(7.5)
        self.__PLATINUM.setPosition(125, 218)

        self.__BRONZE.getScreen().set_alpha(0)
        self.__SILVER.getScreen().set_alpha(0)
        self.__GOLD.getScreen().set_alpha(0)
        self.__PLATINUM.getScreen().set_alpha(0)
        # </editor-fold>
        # </editor-fold>

        # <editor-fold desc="INTERACTIVE SPRITES">
        self.__BIRD = ImageSprite('media/bird1.png')
        self.__BIRD_ANGLE = 0
        self.__BIRD_ANGLE_ACCELERATION = 0.07
        self.__BIRD_ANGLE_SPEED = 1
        self.__BIRD.setScale(2)
        self.__BIRD.setPosition((self._WINDOW.getWindowWidth() // 2) - (self.__BIRD.getScreenWidth() // 2),
                                (self._WINDOW.getWindowHeight() // 2) - (self.__BIRD.getScreenHeight() // 2) - (
                                            self._LAND_SPRITE_1.getScreenHeight() // 2))
        self.__BIRD.setSpeed(self.__JUMP_SPEED)

        self.__PIPES = [[], []]
        for i in range(2):  # DOWN PIPES
            PIPE = ImageSprite('media/pipe.png')
            PIPE.setSpeed(-3)
            PIPE_DOWN_CAP = ImageSprite('media/pipe-down.png')
            PIPE_DOWN_CAP.setPosition(PIPE.getX(), PIPE.getY() + PIPE.getScreenHeight())
            self.__PIPES[0].append([PIPE, PIPE_DOWN_CAP])
        for i in range(2):  # UP PIPES
            PIPE = ImageSprite('media/pipe.png')
            PIPE.setSpeed(-3)
            PIPE_UP_CAP = ImageSprite('media/pipe-up.png')
            PIPE_UP_CAP.setPosition(PIPE.getX(), PIPE.getY() - PIPE.getScreenHeight())
            self.__PIPES[1].append([PIPE, PIPE_UP_CAP])
        # </editor-fold>

        # <editor-fold desc="START SCREEN">
        self._START_SCREEN = ImageSprite('media/splash.png')
        self._START_SCREEN.setScale(0.85)
        self._START_SCREEN.setPosition(
            (self._WINDOW.getWindowWidth() // 2) - (self._START_SCREEN.getScreenWidth() // 2),
            (self._WINDOW.getWindowHeight() // 2) - (self._START_SCREEN.getScreenHeight() // 2) - (
                        self._LAND_SPRITE_1.getScreenHeight() // 2))
        self._START_SCREEN.getScreen().set_alpha(0)

        self._TITLE = ImageSprite('media/title.png')
        self._TITLE.setScale(3)
        self._TITLE.setPosition((self._WINDOW.getWindowWidth() // 2) - (self._TITLE.getScreenWidth() // 2), 120)

        self.LOG_IN_BG = ImageSprite('media/log_in_bg.png')
        self.LOG_IN_BG.setScale(0.65)
        self.LOG_IN_BG.setPosition((self._WINDOW.getWindowWidth() // 2) - (self.LOG_IN_BG.getScreenWidth() // 2), 185)

        self.__FONT = pygame.font.SysFont('Sandstorm', 40)

        self.color = pygame.Color('white')
        self.__USER_IP = ''
        self.__USER_NAME = pygame.Rect(80, 230, 140, 40)
        self.__USER_NAME_ACTIVE = False
        self.__USER_NAME_BORDER = pygame.Rect(80, 230, 140, 40)

        self.color2 = pygame.Color('white')
        self.__USER_IP_2 = ''
        self.__PASS_WORD = pygame.Rect(80, 300, 140, 40)
        self.__PASS_WORD_ACTIVE = False
        self.__PASS_WORD_BORDER = pygame.Rect(80, 300, 140, 40)

        self.__LOG_IN_BUTTON = ImageSprite('media/replay.png')
        self.__LOG_IN_BUTTON.setScale(0.85)
        self.__LOG_IN_BUTTON.setPosition(240, 245)

        self.LOG_IN_TEXT = Text("USERNAME")
        self.LOG_IN_TEXT.setPosition(80, 210)

        self.PASSWORD_TEXT = Text('PASSWORD')
        self.PASSWORD_TEXT.setPosition(80, 280)
        # </editor-fold>

        # <editor-fold desc="END SCREEN">
        self._END_SCREEN = ImageSprite('media/scoreboard.png')
        self._END_SCREEN.setScale(0.85)
        self._END_SCREEN.setPosition((self._WINDOW.getWindowWidth() // 2) - (self._END_SCREEN.getScreenWidth() // 2),
                                     (self._WINDOW.getWindowHeight() // 2) - (
                                                 self._END_SCREEN.getScreenHeight() // 2) - (
                                                 self._LAND_SPRITE_1.getScreenHeight() // 2))
        self._END_SCREEN.getScreen().set_alpha(0)

        self._REPLAY = ImageSprite('media/replay.png')
        self._REPLAY.setScale(0.85)
        self._REPLAY.setPosition((self._WINDOW.getWindowWidth() // 2) - (self._REPLAY.getScreenWidth() // 2), 350)
        self._REPLAY.getScreen().set_alpha(0)

        # </editor-fold>

        # <editor-fold desc="COLLISION SPRITES">
        self.__TOP_COLLISION = Box()
        self.__BOTTOM_COLLISION = Box()
        self.__LEFT_COLLISION = Box()
        self.__RIGHT_COLLISION = Box()

        self.__TOP_BIRD = Box()
        self.__BOTTOM_BIRD = Box()
        self.__LEFT_BIRD = Box()
        self.__RIGHT_BIRD = Box()
        # </editor-fold>

        # <editor-fold desc="INDICATION VARIABLES">
        self.__POINT_1 = False
        self.__POINT_2 = False
        self.__FIRST_RUN = True
        self.__FIRST_RUN_PIPE = True
        self.__JUMP = False
        self.COLLISION = False
        self.__END_RUN = False

        self.border_color = 'black'
        self.border_color_2 = 'black'
        # </editor-fold>

        Sound.SWOOSH_SOUND.play()

    def run(self):
        """
        Runs the main game
        """

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and not self.__FIRST_RUN:
                    if event.key == pygame.K_SPACE and not self.COLLISION and self.__BIRD.getY() > 0 or event.type == pygame.MOUSEBUTTONDOWN and not self.COLLISION and self.__BIRD.getY() > 0 and event.type == pygame.KEYDOWN and not self.__FIRST_RUN:
                        self.__BIRD_ANGLE_SPEED = 1
                        while self.__BIRD_ANGLE < 35:
                            self.__BIRD_ANGLE += 2
                        self.__JUMP = True
                        self.jump()
                        Sound.FLAPPING_SOUND.play()
                if pygame.MOUSEBUTTONDOWN and not self.__FIRST_RUN and event.type == pygame.MOUSEBUTTONDOWN and not self.COLLISION and self.__BIRD.getY() > 0:
                    self.__BIRD_ANGLE_SPEED = 1
                    while self.__BIRD_ANGLE < 35:
                        self.__BIRD_ANGLE += 2
                    self.__JUMP = True
                    self.jump()
                    Sound.FLAPPING_SOUND.play()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.__FIRST_RUN = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.COLLISION:
                        if self.__ALPHA == 255:
                            self.__REPLAY_HIT_BOX = pygame.Rect(
                                ((self._WINDOW.getWindowWidth() // 2) + 5) - (self._REPLAY.getScreenWidth() // 2), 350,
                                125, 70)
                            if self.__REPLAY_HIT_BOX.collidepoint(event.pos):
                                self.reset()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if self.__FIRST_RUN:
                if self.__FIRST_RUN_PIPE:
                    self.setPipes()
                    self.__FIRST_RUN_PIPE = False
                self.moveBackground()
                self.__FRAME_COUNTER += 1
                self.changeBirdAnimation()

                if self._START_SCREEN.getScreen().get_alpha() < 255:
                    self.__ALPHA_4 += self.__ALPHA_INCREMENT_2
                    self._START_SCREEN.getScreen().set_alpha(self.__ALPHA_4)
                else:
                    self.__ALPHA_4 = 255

                self._WINDOW.clearScreen()
                self.blitRun()
                self._WINDOW.updateFrame()
            else:
                self.__DISPLAY_SCORE.setPosition(
                    ((self._WINDOW.getWindowWidth() // 2) + 25) - self.__DISPLAY_SCORE.getScreenWidth(), 20)

                self.moveBackground()
                self.movePipes()
                self.gravity(self.__GRAVITY, self.__MAX_SPEED)

                self.__FRAME_COUNTER += 1
                self.changeBirdAnimation()
                self.trackScore()
                self.collision()

                if self.COLLISION:
                    points = (self.SCORE_POINTS_3 * 100) + (self.SCORE_POINTS_2 * 10) + self.SCORE_POINTS
                    info = getInfo(self.__PLAYER_NAME)

                    self.__OLD_HIGHSCORE = info[0][0]
                    print(self.__OLD_HIGHSCORE)
                    if points > self.__OLD_HIGHSCORE:
                        updateHighscore(self.__PLAYER_NAME, points)
                        sortInfo()

                    if not self.__CHECK_DONE:
                        self.__DISPLAY_SCORE_END.setSprite(f'media/font_small_{self.SCORE_POINTS}.png')
                        self.__DISPLAY_SCORE_END_2.setSprite(f'media/font_small_{self.SCORE_POINTS_2}.png')
                        self.__DISPLAY_SCORE_END_3.setSprite(f'media/font_small_{self.SCORE_POINTS_3}.png')
                        self.__DISPLAY_SCORE_END.getScreen().set_alpha(0)
                        self.__DISPLAY_SCORE_END_2.getScreen().set_alpha(0)
                        self.__DISPLAY_SCORE_END_3.getScreen().set_alpha(0)
                        self.__HIGHSCORE.getScreen().set_alpha(0)
                        self.__HIGHSCORE_2.getScreen().set_alpha(0)
                        self.__HIGHSCORE_3.getScreen().set_alpha(0)
                        self.__CHECK_DONE = True

                    if self.__ALPHA < 255:
                        self.__ALPHA += self.__ALPHA_INCREMENT
                        self._END_SCREEN.getScreen().set_alpha(self.__ALPHA)
                        self._REPLAY.getScreen().set_alpha(self.__ALPHA)
                        self.__DISPLAY_SCORE_END.getScreen().set_alpha(self.__ALPHA)
                        self.__DISPLAY_SCORE_END_2.getScreen().set_alpha(self.__ALPHA)
                        self.__DISPLAY_SCORE_END_3.getScreen().set_alpha(self.__ALPHA)
                        self.__HIGHSCORE.getScreen().set_alpha(self.__ALPHA)
                        self.__HIGHSCORE_2.getScreen().set_alpha(self.__ALPHA)
                        self.__HIGHSCORE_3.getScreen().set_alpha(self.__ALPHA)
                    else:
                        self.__ALPHA = 255
                        self.__CHECK_DONE_2 = True
                    if self.__CHECK_DONE_2:
                        if self.__ALPHA_2 < 255:
                            self.__ALPHA_2 += self.__ALPHA_INCREMENT_2
                            self.__BRONZE.getScreen().set_alpha(self.__ALPHA_2)
                            self.__SILVER.getScreen().set_alpha(self.__ALPHA_2)
                            self.__GOLD.getScreen().set_alpha(self.__ALPHA_2)
                            self.__PLATINUM.getScreen().set_alpha(self.__ALPHA_2)
                        else:
                            self.__ALPHA = 255

                self._WINDOW.clearScreen()
                self.blitRun()
                self._WINDOW.updateFrame()

    def startScreen(self):
        """
        Runs the start screen for log in and running the game
        """
        self.__START = False
        self.__LOG_IN = False
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.__LOG_IN_BUTTON_HIT_BOX = pygame.Rect(240, 245, 125, 70)
                    if self.__LOG_IN_BUTTON_HIT_BOX.collidepoint(event.pos):
                        NAME = self.__USER_IP
                        self.__PLAYER_NAME = NAME

                        PASSWORD = self.__USER_IP_2
                        info = getInfo(NAME)

                        if info[0][0] == 0:
                            insertHighscore({
                                'player_name': NAME,
                                'score': '0',
                                'datetime': date.today().strftime("%b, %d, %Y"),
                                'password': PASSWORD
                            })
                            self.__START = True
                        elif info[0][0] != 0 and PASSWORD != info[3][0]:
                            self.border_color = 'red'
                            self.border_color_2 = 'red'
                        elif info[0][0] != 0 and PASSWORD == info[3][0]:
                            self.__OLD_HIGHSCORE = info[0]
                            self.__OLD_HIGHSCORE_2 = info[1]
                            self.__PLAYER_NAME = info[2][0]
                            self.__START = True

                    if self.__USER_NAME.collidepoint(event.pos):
                        self.__USER_NAME_ACTIVE = True
                    else:
                        self.__USER_NAME_ACTIVE = False

                    if self.__PASS_WORD.collidepoint(event.pos):
                        self.__PASS_WORD_ACTIVE = True
                    else:
                        self.__PASS_WORD_ACTIVE = False
                if event.type == pygame.KEYDOWN:
                    if self.__USER_NAME_ACTIVE:
                        if event.key == pygame.K_BACKSPACE:
                            self.__USER_IP = self.__USER_IP[:-1]
                            self.key_count -= 1
                        elif self.key_count <= 7:
                            self.__USER_IP += event.unicode
                            self.key_count += 1

                    if self.__PASS_WORD_ACTIVE:
                        if event.key == pygame.K_BACKSPACE:
                            self.__USER_IP_2 = self.__USER_IP_2[:-1]
                            self.key_count_2 -= 1
                        elif self.key_count_2 <= 7:
                            self.__USER_IP_2 += event.unicode
                            self.key_count_2 += 1

            if self.__START:
                if self.__ALPHA_3 > 0:
                    self.__ALPHA_3 -= self.__ALPHA_INCREMENT_2
                    self._TITLE.getScreen().set_alpha(self.__ALPHA_3)
                else:
                    self.__ALPHA_3 = 255
                    self.run()

            if self.__USER_NAME_ACTIVE:
                self.color = pygame.Color('grey')
            else:
                self.color = pygame.Color('white')

            if self.__PASS_WORD_ACTIVE:
                self.color2 = pygame.Color('grey')
            else:
                self.color2 = pygame.Color('white')

            self.moveBackground()
            self.__FRAME_COUNTER += 1
            self.changeBirdAnimation()

            self._WINDOW.clearScreen()
            self.blitStart()
            self._WINDOW.updateFrame()

    # <editor-fold desc="FUNCTIONS">
    def changeBirdAnimation(self):
        """
        Changes the birds animations
        """
        if self.__FRAME_COUNTER >= 7:
            if self.__IMAGE_LOADER == 0:
                self.__BIRD.setSprite("media/bird1.png")
                self.__BIRD.rotateSprite(self.__BIRD_ANGLE)
                self.__IMAGE_LOADER += 1
                self.__FRAME_COUNTER = 0
            elif self.__IMAGE_LOADER == 1:
                self.__BIRD.setSprite("media/bird2.png")
                self.__BIRD.rotateSprite(self.__BIRD_ANGLE)
                self.__IMAGE_LOADER += 1
                self.__FRAME_COUNTER = 0
            elif self.__IMAGE_LOADER == 2:
                self.__BIRD.setSprite("media/bird3.png")
                self.__BIRD.rotateSprite(self.__BIRD_ANGLE)
                self.__IMAGE_LOADER += 1
                self.__FRAME_COUNTER = 0
            elif self.__IMAGE_LOADER == 3:
                self.__BIRD.setSprite("media/bird2.png")
                self.__BIRD.rotateSprite(self.__BIRD_ANGLE)
                self.__IMAGE_LOADER = 0
                self.__FRAME_COUNTER = 0

    def gravity(self, GRAVITY, MAX_SPEED):
        """
        Creates gravity for the bird
        param GRAVITY: float
        param MAX_SPEED: int
        """
        if self.__BIRD.getSpeed() < MAX_SPEED and self.__BIRD.getY() < self._LAND_SPRITE_1.getY() - self.__BIRD.getScreenHeight():
            self.__BIRD.setSpeed(self.__BIRD.getSpeed() + GRAVITY)
        if self.__BIRD.getY() < self._LAND_SPRITE_1.getY() - self.__BIRD.getScreenHeight():
            self.__BIRD.marqueY()
        if self.__BIRD_ANGLE > -80:
            self.__BIRD_ANGLE_SPEED += self.__BIRD_ANGLE_ACCELERATION
            self.__BIRD_ANGLE -= self.__BIRD_ANGLE_SPEED
            self.__BIRD.rotateSprite(self.__BIRD_ANGLE)

    def jump(self):
        """
        Allows the bird to jump
        """
        if self.__JUMP:
            self.__BIRD.setSpeed(self.__JUMP_SPEED)
            for i in range(self.__JUMP_LOOP):
                self.__BIRD.setSpeed(self.__BIRD.getSpeed() + self.__GRAVITY)
                self.__BIRD.marqueY()
                self.blitRun()
                if i == 1:
                    self.__JUMP = False

    def setPipes(self):
        """
        Sets up the pipes
        """
        for i in range(2):
            if i == 0:
                RANDOM_PIPE_HEIGHT = random.randrange(10, 300)
                self.__PIPES[0][i][0].setPosition(1000, 0)
                self.__PIPES[0][i][0].setImageHeight(RANDOM_PIPE_HEIGHT)
                self.__PIPES[1][i][0].setImageHeight(
                    self._WINDOW.getWindowHeight() - self._LAND_SPRITE_1.getScreenHeight() - self.__PIPES[0][i][
                        0].getScreenHeight() - self.__PIPE_GAP)
                self.__PIPES[1][i][0].setPosition(self.__PIPES[0][i][0].getX(),
                                                  self._WINDOW.getWindowHeight() - self.__PIPES[1][i][
                                                      0].getScreenHeight() - self._LAND_SPRITE_1.getScreenHeight())
            else:
                RANDOM_PIPE_HEIGHT = random.randrange(10, 280)
                self.__PIPES[0][i][0].setPosition(self.__PIPES[0][i - 1][0].getX() + 250, 0)
                self.__PIPES[0][i][0].setImageHeight(RANDOM_PIPE_HEIGHT)
                self.__PIPES[1][i][0].setImageHeight(
                    self._WINDOW.getWindowHeight() - self._LAND_SPRITE_1.getScreenHeight() - self.__PIPES[0][i][
                        0].getScreenHeight() - self.__PIPE_GAP)
                self.__PIPES[1][i][0].setPosition(self.__PIPES[0][i][0].getX(),
                                                  self._WINDOW.getWindowHeight() - self.__PIPES[1][i][
                                                      0].getScreenHeight() - self._LAND_SPRITE_1.getScreenHeight())

    def movePipes(self):
        """
        Moves Pipes
        """
        for i in range(2):
            self.__PIPES[0][i][0].marqueX()
            self.__PIPES[0][i][1].setPosition(self.__PIPES[0][i][0].getX(),
                                              self.__PIPES[0][i][0].getY() + self.__PIPES[0][i][0].getScreenHeight())
            self.__PIPES[1][i][0].marqueX()
            self.__PIPES[1][i][1].setPosition(self.__PIPES[1][i][0].getX(), self.__PIPES[1][i][0].getY())
            if i == 0:
                self.wrapPipe(self.__PIPES[0][i + 1][0].getX() + 250, i)
            else:
                self.wrapPipe(self.__PIPES[0][i - 1][0].getX() + 250, i)

    def wrapPipe(self, MAX_WIDTH, PIPE_NUM, MIN_WIDTH=0):
        """
        Summary: Move the pipe to opposite side and randomizes them
        Param MAX_WIDTH: int
        Param MIN_WIDTH: int
        Param PIPE_NUM: int
        Return: None
        """
        if self.__PIPES[0][PIPE_NUM][0].getX() < MIN_WIDTH - self.__PIPES[0][PIPE_NUM][0].getScreenWidth():
            self.__PIPES[0][PIPE_NUM][0].setX(MAX_WIDTH)
            self.__PIPES[1][PIPE_NUM][0].setX(MAX_WIDTH)
            RANDOM_PIPE_HEIGHT = random.randrange(10, 280)
            self.__PIPES[0][PIPE_NUM][0].setImageHeight(RANDOM_PIPE_HEIGHT)
            self.__PIPES[1][PIPE_NUM][0].setImageHeight(
                self._WINDOW.getWindowHeight() - self._LAND_SPRITE_1.getScreenHeight() - self.__PIPES[0][PIPE_NUM][
                    0].getScreenHeight() - self.__PIPE_GAP)
            self.__PIPES[1][PIPE_NUM][0].setPosition(self.__PIPES[0][PIPE_NUM][0].getX(),
                                                     self._WINDOW.getWindowHeight() - self.__PIPES[1][PIPE_NUM][
                                                         0].getScreenHeight() - self._LAND_SPRITE_1.getScreenHeight())
            if PIPE_NUM == 0:
                self.__POINT_1 = False
            else:
                self.__POINT_2 = False

    def moveBackground(self):
        """
        Summary: Moves background sprites
        Return: None
        """
        self._LAND_SPRITE_1.marqueX()
        self._LAND_SPRITE_1.wrapX(447)
        self._LAND_SPRITE_2.marqueX()
        self._LAND_SPRITE_2.wrapX(447)
        self._SKY_SPRITE_1.marqueX()
        self._SKY_SPRITE_1.wrapX(448)
        self._SKY_SPRITE_2.marqueX()
        self._SKY_SPRITE_2.wrapX(448)

    def collision(self):
        """
        Checks if bird collides with objects
        """
        if not self.COLLISION:
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        if self.__BIRD.isCollision(self.__PIPES[i][j][k].getScreen(),
                                                   self.__PIPES[i][j][k].getPos()) or not self.__BIRD.getY() <= (
                                self._LAND_SPRITE_1.getY() - self.__BIRD.getScreenHeight()):
                            self.COLLISION = True
                            Sound.HIT_SOUND.play()
                            self.pauseSprites()

    def pauseSprites(self):
        """
        Pauses the sprites necessary for game over
        """
        self.__END_RUN = True
        self._LAND_SPRITE_1.setSpeed(0)
        self.__JUMP_SPEED = 0
        self._LAND_SPRITE_2.setSpeed(0)
        self._SKY_SPRITE_1.setSpeed(0)
        self._SKY_SPRITE_2.setSpeed(0)
        self.__BIRD.setSpeed(0)
        for i in range(2):
            self.__PIPES[0][i][0].setSpeed(0)
            self.__PIPES[1][i][0].setSpeed(0)

    def checkScore(self):
        """
        Checks if the score has hit 2 digits or 3 digits
        """
        if self.SCORE_POINTS == 10:
            self.SCORE_POINTS = 0
            self.SCORE_POINTS_2 += 1
            self.__DISPLAY_SCORE_2.setPosition(
                ((self._WINDOW.getWindowWidth() // 2) - self.__DISPLAY_SCORE.getScreenWidth()), 20)
            self.__DISPLAY_SCORE_2.setSprite(f'media/font_big_{self.SCORE_POINTS_2}.png')
        if self.SCORE_POINTS_2 == 10:
            self.SCORE_POINTS_2 = 0
            self.SCORE_POINTS_3 += 1
            self.__DISPLAY_SCORE_3.setPosition(
                (((self._WINDOW.getWindowWidth() // 2) - 25) - self.__DISPLAY_SCORE.getScreenWidth()), 20)
            self.__DISPLAY_SCORE_3.setSprite(f'media/font_big_{self.SCORE_POINTS_3}.png')

    def trackScore(self):
        """
        Adds 1 to the score each time the bird passes the pipes
        """
        if self.__PIPES[0][0][0].getX() < self._WINDOW.getWindowWidth() // 2 and not self.__POINT_1:
            self.SCORE_POINTS += 1
            self.checkScore()
            self.__DISPLAY_SCORE.setSprite(f'media/font_big_{self.SCORE_POINTS}.png')
            self.__POINT_1 = True
            Sound.POINT_SOUND.play()
        elif self.__PIPES[0][1][0].getX() < self._WINDOW.getWindowWidth() // 2 and not self.__POINT_2:
            self.SCORE_POINTS += 1
            self.checkScore()
            self.__DISPLAY_SCORE.setSprite(f'media/font_big_{self.SCORE_POINTS}.png')
            self.__POINT_2 = True
            Sound.POINT_SOUND.play()

    def reset(self):
        """
        Another game reset with some settings left out
        """
        # <editor-fold desc="SETTINGS">
        self._WINDOW = Window('Bird Flappy', 450, 700, 60)

        self.__PIPE_GAP = 150
        self.__FIRST_RUN = True
        self.__MAXIMUM_BIRD_SPEED = 8
        self.__IMAGE_LOADER = 0
        self.__FRAME_COUNTER = 0
        self.__JUMP_SPEED = -6
        self.__JUMP_DECELERATION = 0.1
        self.__JUMP_LOOP = 3

        self.__ALPHA = 0
        self.__ALPHA_INCREMENT = 5
        self.__CHECK_DONE = False

        self.__ALPHA_2 = 0
        self.__ALPHA_INCREMENT_2 = 13
        self.__CHECK_DONE_2 = False

        self.__ALPHA_3 = 255
        self.__CHECK_DONE_3 = False

        self.__ALPHA_4 = 0

        self.key_count = 0
        self.key_count_2 = 0
        # </editor-fold>

        # <editor-fold desc="PHYSICS">
        self.__TIMES = 0
        self.__GRAVITY = 0.35
        self.__MAX_SPEED = 12
        # self.__BIRD_MASS =
        # self.__FORCE_WING =
        # </editor-fold>

        # <editor-fold desc="BACKGROUND">
        # Land One
        self._LAND_SPRITE_1 = ImageSprite('media/land.png')
        self._LAND_SPRITE_1.setImageWidth(450)
        self._LAND_SPRITE_1.setImageHeight(200)
        self._LAND_SPRITE_1.setPosition(0, (self._WINDOW.getWindowHeight() - self._LAND_SPRITE_1.getScreenHeight()))
        self._LAND_SPRITE_1.setSpeed(-3)

        # Land Two
        self._LAND_SPRITE_2 = ImageSprite('media/land.png')
        self._LAND_SPRITE_2.setImageWidth(450)
        self._LAND_SPRITE_2.setImageHeight(200)
        self._LAND_SPRITE_2.setPosition(self._LAND_SPRITE_1.getScreenWidth(),
                                        (self._WINDOW.getWindowHeight() - self._LAND_SPRITE_2.getScreenHeight()))
        self._LAND_SPRITE_2.setSpeed(-3)

        # Sky One
        self._SKY_SPRITE_1 = ImageSprite('media/sky.png')
        self._SKY_SPRITE_1.setImageWidth(450)
        self._SKY_SPRITE_1.setImageHeight(200)
        self._SKY_SPRITE_1.setPosition(0, (
                self._WINDOW.getWindowHeight() - self._SKY_SPRITE_1.getScreenHeight() - self._LAND_SPRITE_1.getScreenHeight()))
        self._SKY_SPRITE_1.setSpeed(-1)

        # Sky Two
        self._SKY_SPRITE_2 = ImageSprite('media/sky.png')
        self._SKY_SPRITE_2.setImageWidth(450)
        self._SKY_SPRITE_2.setImageHeight(200)
        self._SKY_SPRITE_2.setPosition(self._SKY_SPRITE_1.getScreenWidth(), (
                self._WINDOW.getWindowHeight() - self._SKY_SPRITE_2.getScreenHeight() - self._LAND_SPRITE_1.getScreenHeight()))
        self._SKY_SPRITE_2.setSpeed(-1)
        # </editor-fold>

        # <editor-fold desc="SCORE">
        # <editor-fold desc="SCORE">
        self.SCORE_POINTS = 0
        self.__DISPLAY_SCORE = ImageSprite(f'media/font_big_{self.SCORE_POINTS}.png')
        self.__DISPLAY_SCORE.setPosition(1000, 20)

        self.SCORE_POINTS_2 = 0
        self.__DISPLAY_SCORE_2 = ImageSprite(f'media/font_big_{self.SCORE_POINTS_2}.png')
        self.__DISPLAY_SCORE_2.setPosition(1000, 20)

        self.SCORE_POINTS_3 = 0
        self.__DISPLAY_SCORE_3 = ImageSprite(f'media/font_big_{self.SCORE_POINTS_3}.png')
        self.__DISPLAY_SCORE_3.setPosition(1000, 20)

        self.__DISPLAY_SCORE_END = ImageSprite(f'media/font_small_{self.SCORE_POINTS}.png')
        self.__DISPLAY_SCORE_END.setPosition(313, 210)

        self.__DISPLAY_SCORE_END_2 = ImageSprite(f'media/font_small_{self.SCORE_POINTS_2}.png')
        self.__DISPLAY_SCORE_END_2.setPosition(300, 210)

        self.__DISPLAY_SCORE_END_3 = ImageSprite(f'media/font_small_{self.SCORE_POINTS_3}.png')
        self.__DISPLAY_SCORE_END_3.setPosition(290, 210)
        # </editor-fold>

        self.__HIGHSCORE = ImageSprite(f'media/font_small_{self.__OLD_HIGHSCORE_2[2]}.png')
        self.__HIGHSCORE.setPosition(313, 260)

        self.__HIGHSCORE_2 = ImageSprite(f'media/font_small_{self.__OLD_HIGHSCORE_2[1]}.png')
        self.__HIGHSCORE_2.setPosition(300, 260)

        self.__HIGHSCORE_3 = ImageSprite(f'media/font_small_{self.__OLD_HIGHSCORE_2[0]}.png')
        self.__HIGHSCORE_3.setPosition(290, 260)

        self.__HIGHSCORE.getScreen().set_alpha(0)
        self.__HIGHSCORE_2.getScreen().set_alpha(0)
        self.__HIGHSCORE_3.getScreen().set_alpha(0)

        # <editor-fold desc="MEDALS">
        self.__BRONZE = ImageSprite('media/bronze_medal.png')
        self.__BRONZE.setScale(7.5)
        self.__BRONZE.setPosition(125, 218)

        self.__SILVER = ImageSprite('media/silver_medal.png')
        self.__SILVER.setScale(7.5)
        self.__SILVER.setPosition(125, 218)

        self.__GOLD = ImageSprite('media/gold_medal.png')
        self.__GOLD.setScale(7.5)
        self.__GOLD.setPosition(125, 218)

        self.__PLATINUM = ImageSprite('media/platinum_medal.png')
        self.__PLATINUM.setScale(7.5)
        self.__PLATINUM.setPosition(125, 218)

        self.__BRONZE.getScreen().set_alpha(0)
        self.__SILVER.getScreen().set_alpha(0)
        self.__GOLD.getScreen().set_alpha(0)
        self.__PLATINUM.getScreen().set_alpha(0)
        # </editor-fold>
        # </editor-fold>

        # <editor-fold desc="INTERACTIVE SPRITES">
        self.__BIRD = ImageSprite('media/bird1.png')
        self.__BIRD_ANGLE = 0
        self.__BIRD_ANGLE_ACCELERATION = 0.07
        self.__BIRD_ANGLE_SPEED = 1
        self.__BIRD.setScale(2)
        self.__BIRD.setPosition((self._WINDOW.getWindowWidth() // 2) - (self.__BIRD.getScreenWidth() // 2),
                                (self._WINDOW.getWindowHeight() // 2) - (self.__BIRD.getScreenHeight() // 2) - (
                                        self._LAND_SPRITE_1.getScreenHeight() // 2))
        self.__BIRD.setSpeed(self.__JUMP_SPEED)

        self.__PIPES = [[], []]
        for i in range(2):  # DOWN PIPES
            PIPE = ImageSprite('media/pipe.png')
            PIPE.setSpeed(-3)
            PIPE_DOWN_CAP = ImageSprite('media/pipe-down.png')
            PIPE_DOWN_CAP.setPosition(PIPE.getX(), PIPE.getY() + PIPE.getScreenHeight())
            self.__PIPES[0].append([PIPE, PIPE_DOWN_CAP])
        for i in range(2):  # UP PIPES
            PIPE = ImageSprite('media/pipe.png')
            PIPE.setSpeed(-3)
            PIPE_UP_CAP = ImageSprite('media/pipe-up.png')
            PIPE_UP_CAP.setPosition(PIPE.getX(), PIPE.getY() - PIPE.getScreenHeight())
            self.__PIPES[1].append([PIPE, PIPE_UP_CAP])
        # </editor-fold>

        # <editor-fold desc="START SCREEN">
        self._START_SCREEN = ImageSprite('media/splash.png')
        self._START_SCREEN.setScale(0.85)
        self._START_SCREEN.setPosition(
            (self._WINDOW.getWindowWidth() // 2) - (self._START_SCREEN.getScreenWidth() // 2),
            (self._WINDOW.getWindowHeight() // 2) - (self._START_SCREEN.getScreenHeight() // 2) - (
                    self._LAND_SPRITE_1.getScreenHeight() // 2))
        self._START_SCREEN.getScreen().set_alpha(0)

        self._TITLE = ImageSprite('media/title.png')
        self._TITLE.setScale(3)
        self._TITLE.setPosition((self._WINDOW.getWindowWidth() // 2) - (self._TITLE.getScreenWidth() // 2), 120)

        self.LOG_IN_BG = ImageSprite('media/log_in_bg.png')
        self.LOG_IN_BG.setScale(0.65)
        self.LOG_IN_BG.setPosition((self._WINDOW.getWindowWidth() // 2) - (self.LOG_IN_BG.getScreenWidth() // 2), 185)

        self.__FONT = pygame.font.SysFont('Sandstorm', 40)

        self.color = pygame.Color('white')
        self.__USER_IP = ''
        self.__USER_NAME = pygame.Rect(80, 230, 140, 40)
        self.__USER_NAME_ACTIVE = False
        self.__USER_NAME_BORDER = pygame.Rect(80, 230, 140, 40)

        self.color2 = pygame.Color('white')
        self.__USER_IP_2 = ''
        self.__PASS_WORD = pygame.Rect(80, 300, 140, 40)
        self.__PASS_WORD_ACTIVE = False
        self.__PASS_WORD_BORDER = pygame.Rect(80, 300, 140, 40)

        self.__LOG_IN_BUTTON = ImageSprite('media/replay.png')
        self.__LOG_IN_BUTTON.setScale(0.85)
        self.__LOG_IN_BUTTON.setPosition(240, 245)
        # </editor-fold>

        # <editor-fold desc="END SCREEN">
        self._END_SCREEN = ImageSprite('media/scoreboard.png')
        self._END_SCREEN.setScale(0.85)
        self._END_SCREEN.setPosition((self._WINDOW.getWindowWidth() // 2) - (self._END_SCREEN.getScreenWidth() // 2),
                                     (self._WINDOW.getWindowHeight() // 2) - (
                                             self._END_SCREEN.getScreenHeight() // 2) - (
                                             self._LAND_SPRITE_1.getScreenHeight() // 2))
        self._END_SCREEN.getScreen().set_alpha(0)

        self._REPLAY = ImageSprite('media/replay.png')
        self._REPLAY.setScale(0.85)
        self._REPLAY.setPosition((self._WINDOW.getWindowWidth() // 2) - (self._REPLAY.getScreenWidth() // 2), 350)
        self._REPLAY.getScreen().set_alpha(0)

        # </editor-fold>

        # <editor-fold desc="COLLISION SPRITES">
        self.__TOP_COLLISION = Box()
        self.__BOTTOM_COLLISION = Box()
        self.__LEFT_COLLISION = Box()
        self.__RIGHT_COLLISION = Box()

        self.__TOP_BIRD = Box()
        self.__BOTTOM_BIRD = Box()
        self.__LEFT_BIRD = Box()
        self.__RIGHT_BIRD = Box()
        # </editor-fold>

        # <editor-fold desc="INDICATION VARIABLES">
        self.__POINT_1 = False
        self.__POINT_2 = False
        self.__FIRST_RUN = True
        self.__FIRST_RUN_PIPE = True
        self.__JUMP = False
        self.COLLISION = False
        self.__END_RUN = False
        # </editor-fold>

    def blitRun(self):
        """
        Summary: Places all the game objects onto the window
        """
        # <editor-fold desc="MAIN">
        self._WINDOW.getScreen().blit(self._SKY_SPRITE_1.getScreen(), self._SKY_SPRITE_1.getPos())
        self._WINDOW.getScreen().blit(self._SKY_SPRITE_2.getScreen(), self._SKY_SPRITE_2.getPos())
        if self.__FIRST_RUN:
            self._WINDOW.getScreen().blit(self._START_SCREEN.getScreen(), self._START_SCREEN.getPos())
        self._WINDOW.getScreen().blit(self.__BIRD.getScreen(), self.__BIRD.getPos())
        self._WINDOW.getScreen().blit(self._LAND_SPRITE_1.getScreen(), self._LAND_SPRITE_1.getPos())
        self._WINDOW.getScreen().blit(self._LAND_SPRITE_2.getScreen(), self._LAND_SPRITE_2.getPos())
        if not self.__FIRST_RUN:
            for i in range(2):  # PLACES ALL PIPES
                self._WINDOW.getScreen().blit(self.__PIPES[0][i][0].getScreen(), self.__PIPES[0][i][0].getPos())
                self._WINDOW.getScreen().blit(self.__PIPES[0][i][1].getScreen(), self.__PIPES[0][i][1].getPos())
                self._WINDOW.getScreen().blit(self.__PIPES[1][i][0].getScreen(), self.__PIPES[1][i][0].getPos())
                self._WINDOW.getScreen().blit(self.__PIPES[1][i][1].getScreen(), self.__PIPES[1][i][1].getPos())
        self._WINDOW.getScreen().blit(self.__DISPLAY_SCORE.getScreen(), self.__DISPLAY_SCORE.getPos())
        self._WINDOW.getScreen().blit(self.__DISPLAY_SCORE_2.getScreen(), self.__DISPLAY_SCORE_2.getPos())
        self._WINDOW.getScreen().blit(self.__DISPLAY_SCORE_3.getScreen(), self.__DISPLAY_SCORE_3.getPos())
        # </editor-fold>

        if self.__END_RUN:
            info = getInfo(self.__PLAYER_NAME)
            print(info)
            self.__OLD_HIGHSCORE_2 = info[1]
            self.__HIGHSCORE = ImageSprite(f'media/font_small_{self.__OLD_HIGHSCORE_2[2]}.png')
            self.__HIGHSCORE.setPosition(313, 260)

            self.__HIGHSCORE_2 = ImageSprite(f'media/font_small_{self.__OLD_HIGHSCORE_2[1]}.png')
            self.__HIGHSCORE_2.setPosition(300, 260)

            self.__HIGHSCORE_3 = ImageSprite(f'media/font_small_{self.__OLD_HIGHSCORE_2[0]}.png')
            self.__HIGHSCORE_3.setPosition(290, 260)

            self._WINDOW.getScreen().blit(self._END_SCREEN.getScreen(), self._END_SCREEN.getPos())
            self._WINDOW.getScreen().blit(self._REPLAY.getScreen(), self._REPLAY.getPos())

            self._WINDOW.getScreen().blit(self.__DISPLAY_SCORE_END.getScreen(), self.__DISPLAY_SCORE_END.getPos())
            if self.SCORE_POINTS_2 != 0:
                self._WINDOW.getScreen().blit(self.__DISPLAY_SCORE_END_2.getScreen(),
                                              self.__DISPLAY_SCORE_END_2.getPos())
            if self.SCORE_POINTS_3 != 0:
                self._WINDOW.getScreen().blit(self.__DISPLAY_SCORE_END_3.getScreen(),
                                              self.__DISPLAY_SCORE_END_3.getPos())

            self._WINDOW.getScreen().blit(self.__HIGHSCORE.getScreen(), self.__HIGHSCORE.getPos())
            if self.__OLD_HIGHSCORE_2[1] != 0:
                self._WINDOW.getScreen().blit(self.__HIGHSCORE_2.getScreen(), self.__HIGHSCORE_2.getPos())
            if self.__OLD_HIGHSCORE_2[0] != 0:
                self._WINDOW.getScreen().blit(self.__HIGHSCORE_3.getScreen(), self.__HIGHSCORE_3.getPos())

            if 1 <= self.SCORE_POINTS_2 < 2:
                self._WINDOW.getScreen().blit(self.__BRONZE.getScreen(), self.__BRONZE.getPos())
            elif 2 <= self.SCORE_POINTS_2 < 3:
                self._WINDOW.getScreen().blit(self.__SILVER.getScreen(), self.__SILVER.getPos())
            elif 3 <= self.SCORE_POINTS_2 < 4:
                self._WINDOW.getScreen().blit(self.__GOLD.getScreen(), self.__GOLD.getPos())
            elif 4 <= self.SCORE_POINTS_2:
                self._WINDOW.getScreen().blit(self.__PLATINUM.getScreen(), self.__PLATINUM.getPos())

    def blitStart(self):
        """
        blits all necessary sprites in the start screen
        """
        self._WINDOW.getScreen().blit(self._SKY_SPRITE_1.getScreen(), self._SKY_SPRITE_1.getPos())
        self._WINDOW.getScreen().blit(self._SKY_SPRITE_2.getScreen(), self._SKY_SPRITE_2.getPos())
        self._WINDOW.getScreen().blit(self.__BIRD.getScreen(), self.__BIRD.getPos())
        self._WINDOW.getScreen().blit(self._LAND_SPRITE_1.getScreen(), self._LAND_SPRITE_1.getPos())
        self._WINDOW.getScreen().blit(self._LAND_SPRITE_2.getScreen(), self._LAND_SPRITE_2.getPos())
        self._WINDOW.getScreen().blit(self._TITLE.getScreen(), self._TITLE.getPos())
        self._WINDOW.getScreen().blit(self.LOG_IN_BG.getScreen(), self.LOG_IN_BG.getPos())
        self._WINDOW.getScreen().blit(self.__LOG_IN_BUTTON.getScreen(), self.__LOG_IN_BUTTON.getPos())
        self._WINDOW.getScreen().blit(self.LOG_IN_TEXT.getScreen(), self.LOG_IN_TEXT.getPos())
        self._WINDOW.getScreen().blit(self.PASSWORD_TEXT.getScreen(), self.PASSWORD_TEXT.getPos())
        pygame.draw.rect(self._WINDOW.getScreen(), self.color, self.__USER_NAME)
        pygame.draw.rect(self._WINDOW.getScreen(), self.color2, self.__PASS_WORD)
        pygame.draw.rect(self._WINDOW.getScreen(), self.border_color, self.__PASS_WORD_BORDER, 2)
        pygame.draw.rect(self._WINDOW.getScreen(), self.border_color_2, self.__USER_NAME_BORDER, 2)

        surf = self.__FONT.render(self.__USER_IP, True, 'black')
        surf_2 = self.__FONT.render(self.__USER_IP_2, True, 'black')

        self._WINDOW.getScreen().blit(surf, (self.__USER_NAME.x + 5, self.__USER_NAME.y + 5))
        self._WINDOW.getScreen().blit(surf_2, (self.__PASS_WORD.x + 5, self.__PASS_WORD.y + 5))
    # </editor-fold>


# --- MAIN PROGRAM CODE --- #
if __name__ == "__main__":
    pygame.init()
    GAME = Game()
    GAME.startScreen()
