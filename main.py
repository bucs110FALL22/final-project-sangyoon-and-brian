import pygame
from pygame.locals import *
import src.background
import src.button
import src.cursor
import src.dungeon
import src.enemy
import src.eventhandler
import src.ground
import src.item
import src.player
import src.healthbar
import src.magicskill
import src.stagedisplay
import src.statusbar
import sys
from tkinter import filedialog
from tkinter import *
import numpy
import random
pygame.init()
run_ani_R = [pygame.image.load("assets/Player_R.png"), pygame.image.load("assets/Player_Run1_R.png"),
             pygame.image.load("assets/Player_Run2_R.png"),pygame.image.load("assets/Player_Run3_R.png"),
             pygame.image.load("assets/Player_Run4_R.png"),pygame.image.load("assets/Player_Run5_R.png"),
             pygame.image.load("assets/Player_R.png")]
 

run_ani_L = [pygame.image.load("assets/Player_L.png"), pygame.image.load("assets/Player_Run1_L.png"),
             pygame.image.load("assets/Player_Run2_L.png"),pygame.image.load("assets/Player_Run3_L.png"),
             pygame.image.load("assets/Player_Run4_L.png"),pygame.image.load("assets/Player_Run5_L.png"),
             pygame.image.load("assets/Player_L.png")]
 

attack_ani_R = [pygame.image.load("assets/Player_R.png"), pygame.image.load("assets/Attack_R1.png"),
                pygame.image.load("assets/Attack_R2.png"),pygame.image.load("assets/Attack_R2.png"),
                pygame.image.load("assets/Attack_R3.png"),pygame.image.load("assets/Attack_R3.png"),
                pygame.image.load("assets/Attack_R4.png"),pygame.image.load("assets/Attack_R4.png"),
                pygame.image.load("assets/Attack_R5.png"),pygame.image.load("assets/Attack_R5.png"),
                pygame.image.load("assets/Player_R.png")]
 

attack_ani_L = [pygame.image.load("assets/Player_L.png"), pygame.image.load("assets/Attack_L1.png"),
                pygame.image.load("assets/Attack_L2.png"),pygame.image.load("assets/Attack_L2.png"),
                pygame.image.load("assets/Attack_L3.png"),pygame.image.load("assets/Attack_L3.png"),
                pygame.image.load("assets/Attack_L4.png"),pygame.image.load("assets/Attack_L4.png"),
                pygame.image.load("assets/Attack_L5.png"),pygame.image.load("assets/Attack_L5.png"),
                pygame.image.load("assets/Player_L.png")]
health_ani = [pygame.image.load("assets/heart0.png"), pygame.image.load("assets/heart.png"),
              pygame.image.load("assets/heart2.png"), pygame.image.load("assets/heart3.png"),
              pygame.image.load("assets/heart4.png"), pygame.image.load("assets/heart5.png")] 

#def main():
    #pygame.init()
    #Create an instance on your controller object
    
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
#if __name__ == '__main__':
    #main()

vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
ACC = 0.3
FRIC = -0.10
COUNT = 0
FPS = 60

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
enemy = src.enemy.Enemy()
Enemies = pygame.sprite.Group()

player = src.player.Player()
Playergroup = pygame.sprite.Group()
Playergroup.add(player)
 
background = src.background.Background()
button = src.button.Button()
ground = src.ground.Ground()
cursor = src.cursor.Cursor()
 
ground_group = pygame.sprite.Group()
ground_group.add(ground)
 
dungeon = src.dungeon.Dungeon()
handler = src.eventhandler.EventHandler()
health = src.healthbar.HealthBar()
stage_display = src.stagedisplay.StageDisplay()
status_bar = src.statusbar.StatusBar()
MagicSkills = pygame.sprite.Group()
Items = pygame.sprite.Group()
 
hit_cooldown = pygame.USEREVENT + 1



while True:
      player.gravity_check()
      mouse = pygame.mouse.get_pos()
  
      
      for event in pygame.event.get():
          if event.type == hit_cooldown:
              player.cooldown = False
         
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
          if event.type == handler.enemy_generation and     cursor.wait == 0:
              if handler.enemy_count <         handler.stage_enemies[handler.stage - 1]:
                    enemy = src.enemy.Enemy()
                    Enemies.add(enemy)
                    handler.enemy_count += 1
         
       
          if event.type == pygame.MOUSEBUTTONDOWN:
                if 620 <= mouse[0] <= 660 and 300 <= mouse[1] <= 350:
                      if button.imgdisp == 1:
                            cursor.pause()
                      elif button.imgdisp == 0:
                            handler.home()
 
   
          if event.type == pygame.KEYDOWN and cursor.wait == 0:
              if event.key == pygame.K_x and player.magic_cooldown == 1:
                    if player.mana >= 6:
                          player.mana -= 6
                          player.attacking = True
                          lightning = src.magicskill.MagicSkill()
                          MagicSkills.add(lightning)
              if event.key == pygame.K_n:
                    if handler.battle == True and len(Enemies) == 0:
                          handler.next_stage()
                          stage_display = src.stagedisplay.StageDisplay()
                          stage_display.display = True
              if event.key == pygame.K_c and 450 < player.rect.x < 550:
                  handler.stage_handler()
              if event.key == pygame.K_SPACE:
                  player.jump()
              if event.key == pygame.K_z:
                  if player.attacking == False:
                      player.attack()
                      player.attacking = True     
 
 
    
      player.update()
      if player.attacking == True:
            player.attack() 
      player.move()                

  
    
 
          
      
      
             
      background.render()
      ground.render()
      button.render(button.imgdisp)
      cursor.hover()
 
 
    
      if stage_display.display == True:
            stage_display.move_display()
      if stage_display.clear == True:
            stage_display.stage_clear()
 
    
      dungeon.update()
      if player.health > 0:
          displaysurface.blit(player.image, player.rect)
      health.render()
 
  
      displaysurface.blit(status_bar.surf, (580, 5))
      status_bar.update_draw()
      handler.update()
 
     
      for i in Items:
            i.render()
            i.update() 
    
      for ball in MagicSkills:
            ball.lightning()
     
      for enemy in Enemies:
            enemy.update()
            enemy.move()
            enemy.render()

      hits = pygame.sprite.spritecollide(enemy, Playergroup, False)
 
            
      f_hits = pygame.sprite.spritecollide(enemy, MagicSkills, False)
 
            
      if hits and player.attacking == True or f_hits:
                  enemy.kill()
                  handler.dead_enemy_count += 1
        
                  if player.mana < 100: 
                    player.mana += random.randint(1, 3)
      elif hits == True:

                     
                  player.cooldown = True 
                  pygame.time.set_timer(hit_cooldown, 2000) 
 
                  player.health = player.health - 1
                  health.image = health_ani[player.health]
             
                  if player.health <= 0:
                    player.kill()
                    pygame.display.update()
        
      pygame.display.update()







