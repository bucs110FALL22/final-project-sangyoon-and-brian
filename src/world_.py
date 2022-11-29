import pygame
import sys
from .settings import *
from .space import Space
from .player import Player
from .camera import *
from .ground import *


class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible = Camera()
        self.barrier = pygame.sprite.Group()
        self.load_map()

    def load_map(self):
        for row_index, row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Space((x,y),[self.visible,self.barrier])
                if col == 'p':
                    self.player = Player((x,y),[self.visible],self.barrier)

    def run(self):
        self.visible.cdraw(self.player)
        self.visible.update()