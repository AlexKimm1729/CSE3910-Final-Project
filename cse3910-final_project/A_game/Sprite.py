# Sprite.py
"""
Title: MySprite class
Author: Yousuf Mohammed
Author: Alex Kim
Date-Created: 2022-11-01
"""

# --- Imports --- #

from Loader import Color
import pygame

# --- Classes --- #


class MySprite:
    """
    Summary: Abstract sprite class
    """

    def __init__(self):
        self.__X = 0
        self.Y = 0
        self.__POS = (self.__X, self.Y)
        self.__SPEED = 1
        self._COLOR = Color.WHITE
        self._SCREEN = pygame.Surface((1, 1))  # empty Surface of 1 pixel
        self.__WIDTH = 1
        self.__HEIGHT = 1
        self.__DIR_X = 1
        self.__DIR_Y = 1

    # <editor-fold desc="METHODS">

    # <editor-fold desc="MODIFIER">

    def setX(self, X):
        """
        Change the x
        :param X: int
        :return: None
        """
        self.__X = X
        self.__POS = (self.__X, self.Y)

    def setY(self, Y):
        """
        Change the Y
        :param Y: int
        :return: None
        """
        self.Y = Y
        self.__POS = (self.__X, self.Y)

    def setPosition(self, X, Y):
        """
        Change the X and Y
        :param X: int
        :param Y: int
        :return: None
        """
        self.__X = X
        self.Y = Y
        self.__POS = (self.__X, self.Y)

    def setSpeed(self, SPEED):
        """
        Change the speed
        :param SPEED: int
        :return: None
        """
        self.__SPEED = SPEED

    def setColor(self, COLOR):
        """
        :param COLOR: tuple (int)
        :return: None
        """
        self._COLOR = COLOR

    def setWidth(self, WIDTH):
        """
        Change the width
        :param WIDTH: int
        :return: None
        """
        self.__WIDTH = WIDTH

    def setHeight(self, HEIGHT):
        """
        Change the height
        :param HEIGHT: int
        :return: None
        """
        self.__HEIGHT = HEIGHT

    def marqueX(self):
        """
        Moves sprite from left to right across the screen
        :return: None
        """
        self.__X += self.__SPEED
        self.__POS = (self.__X, self.Y)

    def marqueY(self):
        """
        Moves sprite from left to right across the screen
        :return: None
        """
        self.Y += self.__SPEED
        self.__POS = (self.__X, self.Y)

    def wrapX(self, MAX_WIDTH, MIN_WIDTH=0):
        """
        Move the sprite to opposite side of the left/right edges
        :param MAX_WIDTH: int
        :param MIN_WIDTH: int
        :return: None
        """
        if self.__X < MIN_WIDTH - self.getScreenWidth():
            self.__X = MAX_WIDTH
        self.__POS = (self.__X, self.Y)

    def isCollision(self, SCREEN, POS):
        """
        Testing the current sprite position is overlapping the given sprites position
        :param SCREEN: object (Surface)
        :param POS: tuple (int)
        :return: bool
        """
        width = SCREEN.get_width()
        height = SCREEN.get_height()
        X = POS[0]
        Y = POS[1]
        if self.__X - width <= X <= self.__X + self.getScreenWidth():
            if self.Y - height <= Y <= self.Y + self.getScreenHeight():
                return True
        else:
            return False

    def checkBoundaries(self, maxWidth, maxHeight, minWidth=0, minHeight=0):
        if self.__X > maxWidth - self.getScreenWidth():
            self.__X = maxWidth - self.getScreenWidth()
        elif self.__X < minWidth:
            self.__X = minWidth
        if self.Y > maxHeight - self.getScreenHeight():
            self.Y = maxHeight - self.getScreenHeight()
        elif self.Y < minHeight:
            self.Y = minHeight

        self.__POS = (self.__X, self.Y)

    # </editor-fold>

    # <editor-fold desc="ACCESSORS">

    def getX(self):
        return self.__X

    def getY(self):
        return self.Y

    def getPos(self):
        return self.__POS

    def getScreen(self):
        return self._SCREEN

    def getSpeed(self):
        return self.__SPEED

    def getScreenWidth(self):
        return self._SCREEN.get_width()

    def getScreenHeight(self):
        return self._SCREEN.get_height()

    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT

    # </editor-fold>

    # </editor-fold>
