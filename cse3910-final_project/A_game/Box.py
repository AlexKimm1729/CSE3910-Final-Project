# Box.py
"""
Title: Box class
Author: Yousuf Mohammed
Author: Alex Kim
Date-Created: 2022-11-01
"""


# --- IMPORTS --- #
from Sprite import MySprite
import pygame


# --- CLASSES --- #
class Box(MySprite):
    """
    Creates a box for pygame
    """

    def __init__(self):
        """
        Creates a default box for pygame
        """
        MySprite.__init__(self)
        self.setWidth(1)
        self.setHeight(1)
        self.__DIM = (self.getWidth(), self.getHeight())
        self._SCREEN = pygame.Surface(self.__DIM, pygame.SRCALPHA, 32)
        self._SCREEN.fill(self._COLOR)
        self._COLLIDING = False

    # <editor-fold desc="MODIFIER">
    # INPUTS
    def setWidth(self, WIDTH):
        """
        change width
        param WIDTH: int
        return: none
        """
        MySprite.setWidth(self, WIDTH)
        self.__DIM = (self.getWidth(), self.getHeight())
        self._SCREEN = pygame.Surface(self.__DIM, pygame.SRCALPHA, 32)
        self._SCREEN.fill(self._COLOR)

    def setHeight(self, HEIGHT):
        """
        change height
        param HEIGHT: int
        return: none
        """
        MySprite.setHeight(self, HEIGHT)
        self.__DIM = (self.getWidth(), self.getHeight())
        self._SCREEN = pygame.Surface(self.__DIM, pygame.SRCALPHA, 32)
        self._SCREEN.fill(self._COLOR)

    def setColor(self, COLOR):
        """
        change color
        param COLOR: int
        return: none
        """
        MySprite.setColor(self, COLOR)
        self._SCREEN.fill(self._COLOR)

    # PROCESSING
    def notColliding(self):
        """
        box is not colliding
        """
        self._COLLIDING = False

    def isColliding(self):
        """
        box is colliding
        """
        self._COLLIDING = True
    # </editor-fold>

    # <editor-fold desc="ACCESSORS">
    # OUTPUTS
    def getColliding(self):
        return self._COLLIDING
    # </editor-fold>
