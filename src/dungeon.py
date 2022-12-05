import pygame


HEIGHT = 350
WIDTH = 700
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

class Dungeon(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.hide = False
            self.image = pygame.image.load("assets/Dungeon.png")
 
      def update(self):
            if self.hide == False:
                  displaysurface.blit(self.image, (400, 80))