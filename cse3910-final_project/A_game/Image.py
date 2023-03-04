# Image.py
"""
Title: Image class
Author: Yousuf Mohammed
Author: Alex Kim
Date-Created: 2022-11-01
"""

# --- Imports --- #

from Sprite import MySprite
import pygame


# --- Classes --- #


class ImageSprite(MySprite):

    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOCAL = IMAGE_FILE
        self._SCREEN = pygame.image.load(self.__FILE_LOCAL).convert_alpha()
        self.__IMAGE = pygame.image.load(self.__FILE_LOCAL)
        self.__SCALE_X = 1
        self.__SCALE_Y = 1

    # <editor-fold desc="METHODS">

    # <editor-fold desc="MODIFIER">

    def setScale(self, SCALE_X, SCALE_Y=0):
        """
        Summary: Change the scale of the image
        Param SCALE_X: int
        Param SCALE_Y: int
        Return: None
        """
        self.__SCALE_X = SCALE_X
        self.__SCALE_Y = SCALE_Y
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SCREEN = pygame.transform.scale(self._SCREEN,
                                              (self.getScreenWidth() // SCALE_X, self.getScreenHeight() // SCALE_Y))

    def setImageHeight(self, HEIGHT):
        """
        Summary: Change the scale of the image
        Param HEIGHT: int
        Return: None
        """
        self._SCREEN = pygame.transform.scale(self._SCREEN, (self.getScreenWidth(), HEIGHT))

    def setImageWidth(self, WIDTH):
        """
        Summary: Change the scale of the image
        Param HEIGHT: int
        Return: None
        """
        self._SCREEN = pygame.transform.scale(self._SCREEN, (WIDTH, self.getScreenHeight()))

    def setSprite(self, SPRITE):
        self.__FILE_LOCAL = SPRITE
        self._SCREEN = pygame.image.load(self.__FILE_LOCAL).convert_alpha()
        self.setScale(self.__SCALE_X, self.__SCALE_Y)

    def rotateSprite(self, ROTATION):
        self.__IMAGE = pygame.image.load(self.__FILE_LOCAL).convert_alpha()
        self._SCREEN = pygame.transform.rotate(self.__IMAGE, ROTATION)
        self.setScale(2)

    # </editor-fold>

    # <editor-fold desc="ACCESSORS">

    def getImage(self):
        return self.__IMAGE

    # </editor-fold>

    # </editor-fold>
