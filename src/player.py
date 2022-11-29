import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,barrier):
        super().__init__(groups)

        self.counter = 0

        self.leftSprites = []
        self.leftSprites.append(pygame.image.load("../assets/L1.png"))
        self.leftSprites.append(pygame.image.load("../assets/L2.png"))
        self.leftSprites.append(pygame.image.load("../assets/L3.png"))
        self.leftSprites.append(pygame.image.load("../assets/L4.png"))

        self.rightSprites = []
        self.rightSprites.append(pygame.image.load("../assets/R1.png"))
        self.rightSprites.append(pygame.image.load("../assets/R2.png"))
        self.rightSprites.append(pygame.image.load("../assets/R3.png"))
        self.rightSprites.append(pygame.image.load("../assets/R4.png"))
        
        self.upSprites = []
        self.upSprites.append(pygame.image.load("../assets/U1.png"))
        self.upSprites.append(pygame.image.load("../assets/U2.png"))
        self.upSprites.append(pygame.image.load("../assets/U3.png"))
        self.upSprites.append(pygame.image.load("../assets/U4.png"))

        self.downSprites = []
        self.downSprites.append(pygame.image.load("../assets/D1.png"))
        self.downSprites.append(pygame.image.load("../assets/D2.png"))
        self.downSprites.append(pygame.image.load("../assets/D3.png"))
        self.downSprites.append(pygame.image.load("../assets/D4.png"))

        self.image = pygame.image.load("../assets/idleD.png")
        
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.walkspeed = 4
        self.sprintspeed = 6
       
        self.barrier = barrier

    def input(self):
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_d] - keys[pygame.K_a]
        dy = keys[pygame.K_s] - keys[pygame.K_w]
        self.direction = pygame.math.Vector2(dx, dy)
        if dx != 0 and dy != 0:
           self.direction /= 1.41421

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

        if keys[pygame.K_a]:
            self.animations(self.leftSprites)

        elif keys[pygame.K_d]:
            self.animations(self.rightSprites)

        elif keys[pygame.K_w]:
            self.animations(self.upSprites)

        elif keys[pygame.K_s]:
            self.animations(self.downSprites)

        self.input()
        if keys[pygame.K_LSHIFT]:
            self.move(self.sprintspeed)
        else:
            self.move(self.walkspeed)