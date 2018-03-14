class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def attack(self, target, attack_power=None):
        if attack_power == None:
            attack_power = self.power
            target.health -= attack_power
        else:
            target.health -= attack_power
        if type(self).__name__.lower() == 'hero':
            print("You do {} damage to the {}.".format(attack_power, type(target).__name__.lower()))
        else:
            print("The {} does {} damage to you.".format(type(self).__name__.lower(), attack_power))
            
    def print_status(self):
        if type(self).__name__.lower() == 'hero':
            print("You have {} health and {} power.".format(self.health, self.power))
        else:
            print("The {} has {} health and {} power.".format(type(self).__name__.lower(), self.health, self.power))