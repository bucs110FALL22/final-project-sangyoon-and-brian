import pygame
from pygame.locals import *
import src.eventhandler
import src.button

button = src.button.Button()
pygame.init()
HEIGHT = 350
WIDTH = 700
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
headingfont = pygame.font.SysFont("Verdana", 40)
color_light = (170,170,170)
color_dark = (100,100,100)
color_white = (255,255,255)

class StageDisplay(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.text = headingfont.render("STAGE: " + '',  True, color_dark)
            self.rect = self.text.get_rect()
            self.posx = -100
            self.posy = 100
            self.display = False
            self.clear = False
 
      def move_display(self):
           
            self.text = headingfont.render("STAGE: " + '', True, color_dark)
            if self.posx < 720:
                  self.posx += 6
                  displaysurface.blit(self.text, (self.posx, self.posy))
            else:
                  self.display = False
                  self.posx = -100
                  self.posy = 100
 
 
      def stage_clear(self):
            self.text = headingfont.render("STAGE CLEAR!", True , color_dark)
            button.imgdisp = 0
             
            if self.posx < 720:
                  self.posx += 10
                  displaysurface.blit(self.text, (self.posx, self.posy))
            else:
                  self.clear = False
                  self.posx = -100
                  self.posy = 100