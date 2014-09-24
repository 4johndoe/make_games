#! /usr/bin/python

import math, so, pygame, random
from pygame.locals import *

# game_constants
SCREENRECT = Rect(0, 0, 640, 480)

def load_sound(filename):
    filename = os.path.join('data', filename)
    return pygame.mixer.Sound(filename)

def imgcolorkey(image, colorkey):
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

def load_image(filename, colorkey = None):
    filename = os.path.join('data', filename)
    image = pygame.image.load(filename).convert()
    return imgcolorkey(image, colorkey)

class SpriteSheet(self):
    """docstring for SpriteSheet"""
    def __init__(self, filename):
        self.sheet = load_image(filename)

    def imgat(self, rect, colorkey = None):
        rect = Rect(rect)
        image = pygame.Surface(rect.size).con