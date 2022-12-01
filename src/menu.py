import pygame, sys, random
from pygame.locals import *
from .button import Button
from .world_ import World
from .settings import *


class Menu:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH,HEIGHT))
        self.title = pygame.display.set_caption(TITLE)
        self.world = World()
        self.fps = pygame.time.Clock()
        self.run = True
        self.startmenu = True
        self.gamepause = False
        self.playImg = pygame.image.load('assets/play.png').convert_alpha()
        self.playBut = Button(550,200,self.playImg,1)
        self.mquitImg = pygame.image.load('assets/quit.png').convert_alpha()
        self.mquitBut = Button(550,350,self.mquitImg,1)
        self.resumeImg = pygame.image.load('assets/resume.png').convert_alpha()
        self.resumeBut = Button(250,100,self.resumeImg,1)
        self.quitImg = self.mquitImg
        self.quitBut = Button(250,300,self.quitImg,1)

    def start(self):
        while self.run:
            if self.startmenu == True:
                self.display.fill('black')
                if self.playBut.draw(self.display):
                    self.startmenu = False
                if self.mquitBut.draw(self.display):
                    self.run = False

            if self.startmenu == False:
                self.display.fill((0,150,0))
                if self.gamepause == True:
                    self.display.fill(('black'))
                    if self.resumeBut.draw(self.display):
                        self.gamepause = False
                    if self.quitBut.draw(self.display):
                        self.run = False

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.gamepause = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.startmenu == True or self.gamepause == True:
                pass
            else:
                self.world.run()
            pygame.display.update()
            self.fps.tick(FPS)