from characters.base import Character
from random import randint

class Hero(Character):
    def __init__(self, health, power):
        self.purse = 0
        self.inventory = []
        super().__init__(health, power)
    
    def attack(self, target):
        if randint(0, 100) < 20:
            super().attack(target, self.power * 2)
        else:
            super().attack(target)
            
    def buy(self, item):
        pass
    
    def sell(self, item):
        pass
    
    def use(self, item):
        pass