import pygame
from pygame.locals import *
import sys
import cursor



HEIGHT = 350
WIDTH = 700
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
vec = pygame.math.Vector2
class Button(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.vec = vec(620, 300)
            self.imgdisp = 0
 
      def render(self, num):
            if (num == 0):
                  self.image = pygame.image.load("home_small.png")
            elif (num == 1):
                  if cursor.wait == 0:
                        self.image = pygame.image.load("pause_small.png")
                  else:
                        self.image = pygame.image.load("play_small.png")
                                     
            displaysurface.blit(self.image, self.vec)