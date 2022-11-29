import pygame
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        self.print_status()

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("%s is dead." % self.name)

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("%s is dead." % self.name)

    def attack(self, enemy):
        double_power = self.power * 2
        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(double_power)
        self.print_status()

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

    def restore(self):
        self.health = 10
        print("%s's health is restored to %d!" % (self.name, self.health))
        self.print_status()

class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("%s is dead." % self.name)
            return True

class Zombie(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("%s is dead." % self.name)
            return True