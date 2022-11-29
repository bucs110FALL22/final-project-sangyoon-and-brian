import pygame
from .settings import *

class Plant(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("../assets/plant.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)