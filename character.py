class Character:
    def __init__(self):
        self.health = 0
        self.power = 0
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False