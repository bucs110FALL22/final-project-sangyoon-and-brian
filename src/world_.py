import pygame
from .settings import *
from .space import *
from .player import *
from .camera import *
from .green import *

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
                if col == 'g':
                    Plant((x,y),[self.visible])
                if col == 't':
                    Tree((x,y),[self.visible])
                if col == 'r':
                    Rock((x,y),[self.visible])
                if col == 'q':
                    Tent((x,y),[self.visible,self.barrier])
                if col == 'l':
                    Wood((x,y),[self.visible,self.barrier])

    def run(self):
        self.visible.cdraw(self.player)
        self.visible.update()