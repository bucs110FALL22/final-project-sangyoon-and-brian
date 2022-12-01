import pygame
from .settings import *
from .action import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,barrier):
        super().__init__(groups)
        
        self.Lcounter = 0
        self.Rcounter = 0
        self.Ucounter = 0
        self.Dcounter = 0

        self.leftSprites = [pygame.image.load("assets/L1.png"),pygame.image.load("assets/L2.png"),pygame.image.load("assets/L3.png"),pygame.image.load("assets/L4.png")]
        self.rightSprites = [pygame.image.load("assets/R1.png"),pygame.image.load("assets/R2.png"),pygame.image.load("assets/R3.png"),pygame.image.load("assets/R4.png")]
        self.upSprites = [pygame.image.load("assets/U1.png"),pygame.image.load("assets/U2.png"),pygame.image.load("assets/U3.png"),pygame.image.load("assets/U4.png")]
        self.downSprites = [pygame.image.load("assets/D1.png"),pygame.image.load("assets/D2.png"),pygame.image.load("assets/D3.png"),pygame.image.load("assets/D4.png")]

        self.image = pygame.image.load("assets/idleD.png")
        #pygame.image.load("assets/idleD.png")
        
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.walkspeed = 4
        self.sprintspeed = 6
       
        self.barrier = barrier

        #self.moveAnim = MoveAnims()

    def input(self):
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_d] - keys[pygame.K_a]
        dy = keys[pygame.K_s] - keys[pygame.K_w]
        self.direction = pygame.math.Vector2(dx, dy)
        if dx != 0 and dy != 0:
           self.direction /= 1.41421

    def currentMode(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] == 1:
            self.image = self.leftSprites[int(self.Lcounter)]
            self.Lcounter += 0.2
            if self.Lcounter >= len(self.leftSprites):
                self.Lcounter = 0
            self.image = self.leftSprites[int(self.Lcounter)]

        if keys[pygame.K_d] == 1:
            self.image = self.rightSprites[int(self.Rcounter)]
            self.Rcounter += 0.2
            if self.Rcounter >= len(self.rightSprites):
                self.Rcounter = 0
            self.image = self.rightSprites[int(self.Rcounter)]

        if keys[pygame.K_w] == 1:
            self.image = self.upSprites[int(self.Ucounter)]
            self.Ucounter += 0.2
            if self.Ucounter >= len(self.upSprites):
                self.Ucounter = 0
            self.image = self.upSprites[int(self.Ucounter)]

        if keys[pygame.K_s] == 1:
            self.image = self.downSprites[int(self.Dcounter)]
            self.Dcounter += 0.2
            if self.Dcounter >= len(self.downSprites):
                self.Dcounter = 0
            self.image = self.downSprites[int(self.Dcounter)]

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
            
        #self.rect.center += self.direction * speed

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.barrier:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.barrier:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

    def animations(self,sprites):
            self.counter += 1
            if self.counter >= len(sprites):
                self.counter = 0
                self.image = sprites[self.counter]

    def update(self):
        keys = pygame.key.get_pressed()
        self.currentMode()
        #self.moveAnim.update()
        '''
        if keys[pygame.K_a]:
            self.animations(self.leftSprites)

        elif keys[pygame.K_d]:
            self.animations(self.rightSprites)

        elif keys[pygame.K_w]:
            self.animations(self.upSprites)

        elif keys[pygame.K_s]:
            self.animations(self.downSprites)
        '''
        self.input()
        if keys[pygame.K_LSHIFT]:
            self.move(self.sprintspeed)
        else:
            self.move(self.walkspeed)

        #Action.update()