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