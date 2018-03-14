from character import Character
from random import randint

class Hero(Character):
    def attack(self, target):
        if randint(0, 100) < 20:
            super().attack(target, self.power * 2)
        else:
            super().attack(target)