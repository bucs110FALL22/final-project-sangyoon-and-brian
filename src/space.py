import pygame
from .settings import *

class Space(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("assets/plateau.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Rock(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("assets/rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Tent(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("assets/tent.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Wood(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("assets/log.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)