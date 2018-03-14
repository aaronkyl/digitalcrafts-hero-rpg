class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def attack(self, target):
        target.health -= self.power
        if type(self).__name__.lower() == 'hero':
            print("You do {} damage to the {}.".format(self.power, type(target).__name__.lower()))
        else:
            print("The {} does {} damage to you.".format(type(self).__name__.lower(), self.power))
            
    def print_status(self):
        if type(self).__name__.lower() == 'hero':
            print("You have {} health and {} power.".format(self.health, self.power))
        else:
            print("The {} has {} health and {} power.".format(type(self).__name__.lower(), self.health, self.power))