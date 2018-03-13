from character import Character

class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2
        
    def attack(self, target):
        target.health -= self.power
        print("The {} does {} damage to you.".format(type(self).__name__.lower(), self.power))
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def print_status(self):
        print("The {} has {} health and {} power.".format(type(self).__name__.lower(), self.health, self.power))