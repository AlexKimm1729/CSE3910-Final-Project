# Window.py
"""
Title: Window class
Author: Yousuf Mohammed
Author: Alex Kim
Date-Created: 2022-11-01
"""

# --- Imports --- #

import pygame

# --- Classes --- #


class Window:
    """
    Summary: Create the window that will load pygame
    """

    def __init__(self, TITLE, WIDTH, HEIGHT, FPS):
        self.__TITLE = TITLE  # text that appears in the title bar
        self.__FPS = FPS
        self.__WIDTH = WIDTH  # width of window
        self.__HEIGHT = HEIGHT  # height of window
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT)  # screen dimensions
        self.__BACKGROUND_COLOR = (78, 192, 202, 255)
        self.__FRAME = pygame.time.Clock()  # clock object that measures fps
        self.__SCREEN = pygame.display.set_mode(self.__SCREEN_DIM)  # SCREEN object. Every item in your program will overlay on top of the SCREEN object.
        self.__SCREEN.fill(self.__BACKGROUND_COLOR)  # Fills the screen with a layer of color
        pygame.display.set_caption(self.__TITLE)  # sets the title of the window to the TITLE value. (it doesn't return anything)

    # <editor-fold desc="METHODS">

    # <editor-fold desc="MODIFIER">

    def updateFrame(self):
        """
        Summary: Update the Window object based on the fps
        Return: None
        """
        self.__FRAME.tick(self.__FPS)  # Waits for the appropriate time based on the fps
        pygame.display.flip()  # Updates the computer display with the new frame

    def clearScreen(self):
        """
        Summary: Fill the screen with the background color
        Return: None
        """
        self.__SCREEN.fill(self.__BACKGROUND_COLOR)

    def setColor(self, COLOR):
        """
        Summary: Updates The background color
        Param COLOR: tuple (int)
        Return: None
        """
        self.__BACKGROUND_COLOR = COLOR

    # </editor-fold>

    # <editor-fold desc="ACCESSORS">

    def getScreen(self):
        return self.__SCREEN

    def getWindowWidth(self):
        return self.__WIDTH

    def getWindowHeight(self):
        return self.__HEIGHT

    # </editor-fold>

    # </editor-fold>
