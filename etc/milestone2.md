# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

class Mycharacter:
  def __init__(self,x,y,image_mycharacter,hp):
    self.location = (x,y)
    self.image = image_mycharacter

  def move (self,up,down,right,left):
    self.up = (x,y + up)
    self.down = (x,y - down)
    self.right = (x + right, y)
    self.left = (x - left, y)

    
## Class Interface 2

class Weapon:
  def __init__(self,image_weapon):
    self.image = image_weapon


  def damage(self,damage):
    self.damage = damage
    
## Class Interface 3

class Monster:
  def __init__(self,x,y,image_monster,hp):
    self.location = (x,y)
    self.image = image_monster

  def damage(self,damage):
    self.damage = damage