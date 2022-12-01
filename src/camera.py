import pygame
from .world_ import *
from .player import *


class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.hWid = self.display_surface.get_size()[0]//2
        self.hHei = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()
    
    def cdraw(self,player):
        self.offset.x = player.rect.centerx - self.hWid
        self.offset.y = player.rect.centery - self.hHei
        for sprite in self.sprites():
            offsetPos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offsetPos)
