import pygame


HEIGHT = 350
WIDTH = 700
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("assets/Background.png")
            self.rectBGimg = self.bgimage.get_rect()        
            self.bgY = 0
            self.bgX = 0
 
      def render(self):
            displaysurface.blit(self.bgimage, (self.bgX, self.bgY))      