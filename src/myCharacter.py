class myCharacter(pygame.sprite.Sprite):
  def __init__(self,x,y,image_mycharacter):
    super().__init__(self)
    self.location = (x,y)
    self.image = image_mycharacter
    self.rect = self.image.get_rect()
  
  def move(self,up,down,right,left):
    self.up = (x,y + up)
    self.down = (x, y - down)
    self.right = (x + right, y)
    self.left = (x - right, y)

  def stats(hp,atk,def,spd,atkspd):
    self.hp = 50
    self.atk = 5
    self.def = 5
    self.spd = 7
    self.atkspd = 6
