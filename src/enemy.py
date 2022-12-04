import pygame
import random
import cursor
import player
import magicskill


WIDTH = 700

vec = pygame.math.Vector2

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()     
        self.pos = vec(0,0)
        self.vel = vec(0,0)
 
        self.direction = random.randint(0,1) 
        self.vel.x = random.randint(2,6) / 2  
        self.mana = random.randint(1, 3)      
 
        
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 235
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = 235
 
 
      def move(self):
        if cursor.wait == 1: return
         
         
        if self.pos.x >= (WIDTH-20):
              self.direction = 1
        elif self.pos.x <= 0:
              self.direction = 0
 
             
        if self.direction == 0:
            self.pos.x += self.vel.x
        if self.direction == 1:
            self.pos.x -= self.vel.x
             
        self.rect.topleft = self.pos 
                
      def update(self):
            
            hits = pygame.sprite.spritecollide(self, Playergroup, False)
 
            
            f_hits = pygame.sprite.spritecollide(self, MagicSkills, False)
 
            
            if hits and player.attacking == True or f_hits:
                  self.kill()
                  handler.dead_enemy_count += 1
                   
                  if player.mana < 100: player.mana += self.mana 
                  
                   
                  rand_num = numpy.random.uniform(0, 100)
                  item_no = 0
                  if rand_num >= 0 and rand_num <= 5:  
                        item_no = 1
                  
 
                  if item_no != 0:
                        
                        item = Item(item_no)
                        Items.add(item)
                       
                        item.posx = self.pos.x
                        item.posy = self.pos.y
                  
 
                        
            elif hits and player.attacking == False:
                  player.player_hit()
                   
      def render(self):
            
            displaysurface.blit(self.image, self.rect)