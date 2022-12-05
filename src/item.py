import pygame
from pygame.locals import *
import sys
import src.healthbar
import src.player
import src.healthbar

health = src.healthbar.HealthBar()

HEIGHT = 350
WIDTH = 700
player = src.player.Player()

Playergroup = pygame.sprite.Group()
Playergroup.add(player)
health_ani = [pygame.image.load("assets/heart0.png"), pygame.image.load("assets/heart.png"),
              pygame.image.load("assets/heart2.png"), pygame.image.load("assets/heart3.png"),
              pygame.image.load("assets/heart4.png"), pygame.image.load("assets/heart5.png")]
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
class Item(pygame.sprite.Sprite):
      def __init__(self, itemtype):
            super().__init__()
            if itemtype == 1: self.image = pygame.image.load("assets/heart.png")
            self.rect = self.image.get_rect()
            self.type = itemtype
            self.posx = 0
            self.posy = 0
             
      def render(self):
            self.rect.x = self.posx
            self.rect.y = self.posy
            displaysurface.blit(self.image, self.rect)
 
      def update(self):
            hits = pygame.sprite.spritecollide(self, Playergroup, False)
            
            if hits:
                  if player.health < 5 and self.type == 1:
                        player.health += 1
                        health.image = health_ani[player.health]
                        self.kill()