from potion import Potion

class Store:
    def __init__(self):
        self.inventory = [
            Potion()
            ]
        print(self.inventory)