from colorama import init, Fore, Style

class Character:
    def __init__(self, health, power, bounty=0):
        self.health = health
        self.power = power
        self.bounty = 0
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def attacked_response(self):
        pass
    
    def defend(self):
        return False
    
    def defended(self):
        print("The {} blocked!".format(type(self).__name__.lower()))
        pass
        
    def attack(self, target, attack_power=None):
        defended = target.defend()
        if not defended:
            if attack_power == None:
                attack_power = self.power
                target.health -= attack_power
            else:
                target.health -= attack_power
            
            self.print_attack_results(target, attack_power)
            
            target.attacked_response()
        else:
            target.defended()
    
    def print_attack_results(self, target, attack_power):
        if type(self).__name__.lower() == 'hero':
            print("You do" + Fore.CYAN + Style.BRIGHT + " {} damage".format(attack_power) + Style.RESET_ALL + " to the {}.".format(type(target).__name__.lower()))
        else:
            print("The {} does".format(type(self).__name__.lower()) + Fore.RED + " {} damage".format(attack_power) + Style.RESET_ALL + " to you.")
            
    def print_status(self):
        if type(self).__name__.lower() == 'hero':
            print("You have {} health and {} power.".format(self.health, self.power))
        else:
            print("The {} has {} health and {} power.".format(type(self).__name__.lower(), self.health, self.power))