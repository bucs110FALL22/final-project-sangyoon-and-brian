import Character
class Monster(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("%s is dead." % self.name)
            return True