import pygame
import player
HEIGHT = 350
WIDTH = 700
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
class MagicSkill(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.direction  = player.direction
            if self.direction == "RIGHT":
                  self.image = pygame.image.load("Lightning.png")
            else:
                  self.image = pygame.image.load("Lightning.png")           
            self.rect = self.image.get_rect(center = player.pos)
            self.rect.x = player.pos.x
            self.rect.y = player.pos.y - 40
             
      def lightning(self):
            player.magic_cooldown = 0
            
            if -10 < self.rect.x < 710:
                  if self.direction == "RIGHT":
                        self.image = pygame.image.load("Lightning.png")
                        displaysurface.blit(self.image, self.rect)
                  else:
                        self.image = pygame.image.load("Lightning.png")
                        displaysurface.blit(self.image, self.rect)
                         
                  if self.direction == "RIGHT":
                        self.rect.move_ip(12, 0)
                  else:
                        self.rect.move_ip(-12, 0)   
            else:
                  self.kill()
                  player.magic_cooldown = 1
                  player.attacking = False