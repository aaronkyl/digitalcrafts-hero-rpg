class Potion:
    def __init__(self):
        self.name = "Super Tonic"
        self.price = 5
        
    def use(self, user):
        user.health += 10
        # remove from user's inventory function, use either del with index or remove()