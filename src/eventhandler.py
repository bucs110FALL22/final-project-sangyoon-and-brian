import pygame
from pygame.locals import *
import src.button
from tkinter import filedialog
from tkinter import *
import src.background
import src.enemy
import src.item
import src.dungeon
import src.ground
import src.button
import src.stagedisplay
import sys

stage_display = src.stagedisplay.StageDisplay()
button = src.button.Button()
ground = src.ground.Ground()
background = src.background.Background()
Enemies = pygame.sprite.Group()
Items = pygame.sprite.Group()
dungeon = src.dungeon.Dungeon()
class EventHandler():
      def __init__(self):
            self.enemy_count = 0
            self.dead_enemy_count = 0
            self.battle = False
            self.enemy_generation = pygame.USEREVENT + 2
            self.stage = 1
            
 
            self.stage_enemies = []
            for x in range(1, 21):
                  self.stage_enemies.append(int((x ** 2 / 2) + 1))
             
      def stage_handler(self):
            
            self.root = Tk()
            self.root.geometry('200x170')
             
            button1 = Button(self.root, text = "Golem Dungeon", width = 18, height = 2,
                            command = self.world1)
            
              
            button1.place(x = 40, y = 15)
            
             
            self.root.mainloop()
       
      def world1(self):
            self.root.destroy()
            pygame.time.set_timer(self.enemy_generation, 2000)
            button.imgdisp = 1
            dungeon.hide = True
            self.battle = True
 
      
  
      def next_stage(self):
            button.imgdisp = 1
            self.stage += 1
            print("Stage: "  + str(self.stage))
            self.enemy_count = 0
            self.dead_enemy_count = 0
            pygame.time.set_timer(self.enemy_generation, 1500 - (50 * self.stage))      
 
      def update(self):
            if self.dead_enemy_count == self.stage_enemies[self.stage - 1]:
                  self.dead_enemy_count = 0
                  stage_display.clear = True
                  stage_display.stage_clear()
 
      def home(self):
           
            pygame.time.set_timer(self.enemy_generation, 0)
            self.battle = False
            self.enemy_count = 0
            self.dead_enemy_count = 0
            self.stage = 1
 
            
            for group in Enemies, Items:
                  for entity in group:
                        entity.kill()
             
            
            dungeon.hide = False
            background.bgimage = pygame.image.load("assets/Background.png")
            ground.image = pygame.image.load("assets/Ground.png")