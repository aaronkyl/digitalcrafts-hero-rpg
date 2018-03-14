from character import Character

class Zombie(Character):
    def __init__(self):
        self.health = 6
        self.power = 1
    
    def alive(self):
        return True