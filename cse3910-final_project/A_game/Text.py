# Text.py
"""
Title: Text class
Author: Yousuf Mohammed
Author: Alex Kim
Date-Created: 2022-11-01
"""

# --- Imports --- #

from Sprite import MySprite
import pygame

# --- Classes --- #


class Text(MySprite):
    """
    Summary: All text functions
    """

    def __init__(self, TEXT):
        MySprite.__init__(self)
        self.__TEXT = TEXT
        self.__FONT_FAMILY = "Sandstorm"
        self.__FONT_SIZE = 25
        self.__FONT = pygame.font.SysFont(self.__FONT_FAMILY, self.__FONT_SIZE)
        self._SCREEN = self.__FONT.render(self.__TEXT, True, 'black')

    # <editor-fold desc="METHODS">

    # <editor-fold desc="MODIFIER">
    
    def setSize(self, SIZE):
        """
        Summary: Change the size of the text
        :param SIZE: int
        :return: None
        """
        self.__FONT_SIZE = SIZE
        self.__FONT = pygame.font.SysFont(self.__FONT_FAMILY, self.__FONT_SIZE)
        self._SCREEN = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def setText(self, NEW_TEXT):
        """
        Change the text
        :param NEW_TEXT: int
        :return: None
        """
        self.__TEXT = NEW_TEXT
        self._SCREEN = self.__FONT.render(self.__TEXT, True, self._COLOR)

    # </editor-fold>

    # </editor-fold>
