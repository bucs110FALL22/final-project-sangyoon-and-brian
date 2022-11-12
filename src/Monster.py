class Monster:
  def __init__(self,x,y,image_monster):
    self.location = (x,y)
    self.image = image_monster

  def damage(self,atk):
    self.atk = atk
