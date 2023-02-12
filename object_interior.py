import pygame
from data import *


class Objectinterior(pygame.Rect):
    def __init__(self, x, y, weight,height,image):
        super().__init__(x,y,weight,height)
        self.IMAGE = image

class Wall(Objectinterior):
    def __init__(self,x,y,image,weight = 20 ,height = 50):
        super().__init__(x,y,weight,height)
        self.IMAGE = image

