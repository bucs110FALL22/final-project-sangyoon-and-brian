import pygame
from pygame.locals import *


HEIGHT = 350
WIDTH = 700
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))


color_light = (170,170,170)
color_dark = (100,100,100)
color_white = (255,255,255) 
   
headingfont = pygame.font.SysFont("Verdana", 40)
regularfont = pygame.font.SysFont('Corbel',25)
smallerfont = pygame.font.SysFont('Corbel',16) 
text = regularfont.render('LOAD' , True , color_light)

class StatusBar(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((90, 66))
            self.rect = self.surf.get_rect(center = (500, 10))
            
             
      def update_draw(self):
           
            text1 = smallerfont.render("STAGE: " + str(handler.stage) , True , color_white)
            text3 = smallerfont.render("MANA: " + str(player.mana) , True , color_white)
            
            
 
           
            displaysurface.blit(text1, (585, 7))
            displaysurface.blit(text3, (585, 37))