from characters.base import Character

class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power, bounty=2)