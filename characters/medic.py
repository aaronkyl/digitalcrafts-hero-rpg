from characters.base import Character
from random import randint

class Medic(Character):
    def __init__(self, health, power):
        super().__init__(health, power, bounty=10)
        
    def attacked_response(self):
        if randint(0, 100) < 20:
            self.health += 2
            print("The medic heals 2 health!")