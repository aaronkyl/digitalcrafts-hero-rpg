from character import Character

class Hero(Character):
    def attack(self, target):
        target.health -= self.power
        print("You do {} damage to the {}.".format(self.power, type(target).__name__.lower()))
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
            
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))