class Hero:
    def __init__(self):
        self.health = 10
        self.power = 5
        
    def attack(self, target):
        target.health -= self.power
        print("You do {} damage to the {}.".format(self.power, type(target).__name__.lower()))