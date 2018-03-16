class Potion:
    def __init__(self):
        self.name = "Super Tonic"
        self.price = 5
    
    def add_to_inventory(self):
        return Potion()
        
    def use(self, user):
        user.health += 10
        # remove from user's inventory function, use either del with index or remove()