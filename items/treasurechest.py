from random import randint, choice
from items.goldpouch import GoldPouch
from items.potion import Potion

class TreasureChest:
    def __init__(self):
        self.name = "Treasure Chest"
    
    def contains(self):
        return choice(GoldPouch(), Potion())