import pygame
from pygame.locals import *
import sys


class Cursor(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("cursor.png")
            self.rect = self.image.get_rect()
            self.wait = 0
 
      def pause(self):
            if self.wait == 1:
                  self.wait = 0
            else:
                  self.wait = 1
 
      def hover(self):
          if 620 <= mouse[0] <= 660 and 300 <= mouse[1] <= 345:
                pygame.mouse.set_visible(False)
                cursor.rect.center = pygame.mouse.get_pos()  
                displaysurface.blit(cursor.image, cursor.rect)
          else:
                pygame.mouse.set_visible(True)