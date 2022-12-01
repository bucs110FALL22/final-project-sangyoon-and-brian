import Character

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