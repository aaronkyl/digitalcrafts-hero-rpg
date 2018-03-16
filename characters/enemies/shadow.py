from characters.base import Character
from random import randint

class Shadow(Character):
    def __init__(self, power):
        super().__init__(1, power, bounty=5)
    
    def defend(self):
        """the shadow has a 10% chance of avoiding all damage"""
        if randint(0, 10) > 1:
            return True
        else:
            return False