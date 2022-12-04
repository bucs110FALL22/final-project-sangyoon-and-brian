import pygame
from pygame.locals import *
import cursor


vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
ACC = 0.3
FRIC = -0.10
COUNT = 0
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player_R.png")
        self.rect = self.image.get_rect()
 
        
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = "RIGHT"
 
        
        self.jumping = False
        self.running = False
        self.move_frame = 0
 
        
        self.attacking = False
        self.cooldown = False
        self.immune = False
        self.special = False
        self.attack_frame = 0
        self.health = 5
        self.magic_cooldown = 1
        self.mana = 0
 
 
    def move(self):
          if cursor.wait == 1: return
           
          
          self.acc = vec(0,0.5)
 
          
          if abs(self.vel.x) > 0.3:
                self.running = True
          else:
                self.running = False
 
          
          pressed_keys = pygame.key.get_pressed()
 
          
          if pressed_keys[K_LEFT]:
                self.acc.x = -ACC
          if pressed_keys[K_RIGHT]:
                self.acc.x = ACC 
 
         
          self.acc.x += self.vel.x * FRIC
          self.vel += self.acc
          self.pos += self.vel + 0.5 * self.acc  
 
          
          if self.pos.x > WIDTH:
                self.pos.x = 0
          if self.pos.x < 0:
                self.pos.x = WIDTH
         
          self.rect.midbottom = self.pos            
 
    def gravity_check(self):
          hits = pygame.sprite.spritecollide(player ,ground_group, False)
          if self.vel.y > 0:
              if hits:
                  lowest = hits[0]
                  if self.pos.y < lowest.rect.bottom:
                      self.pos.y = lowest.rect.top + 1
                      self.vel.y = 0
                      self.jumping = False
 
 
    def update(self):
          if cursor.wait == 1: return
           
          if self.move_frame > 6:
                self.move_frame = 0
                return
 
          
          if self.jumping == False and self.running == True:  
                if self.vel.x > 0:
                      self.image = run_ani_R[self.move_frame]
                      self.direction = "RIGHT"
                else:
                      self.image = run_ani_L[self.move_frame]
                      self.direction = "LEFT"
                self.move_frame += 1
 
          
          if abs(self.vel.x) < 0.2 and self.move_frame != 0:
                self.move_frame = 0
                if self.direction == "RIGHT":
                      self.image = run_ani_R[self.move_frame]
                elif self.direction == "LEFT":
                      self.image = run_ani_L[self.move_frame]
 
    def attack(self):        
               
          if self.attack_frame > 10:
                self.attack_frame = 0
                self.attacking = False
 
          
          if self.direction == "RIGHT":
                 self.image = attack_ani_R[self.attack_frame]
          elif self.direction == "LEFT":
                 self.correction()
                 self.image = attack_ani_L[self.attack_frame] 
 
          
          self.attack_frame += 1
           
 
    def jump(self):
        self.rect.x += 1
 
        
        hits = pygame.sprite.spritecollide(self, ground_group, False)
         
        self.rect.x -= 1
 
        
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -12
 
    def correction(self):
         
          if self.attack_frame == 1:
                self.pos.x -= 20
          if self.attack_frame == 10:
                self.pos.x += 20
                 
    def player_hit(self):
        if self.cooldown == False:      
            self.cooldown = True 
            pygame.time.set_timer(hit_cooldown, 1000) 
 
            self.health = self.health - 1
            health.image = health_ani[self.health]
             
            if self.health <= 0:
                self.kill()
                pygame.display.update()