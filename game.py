import os
from characters import *
from colorama import init, Fore, Style
from ui import UI
from random import choice, randint
from game_engine import combat

def main():
    player = Hero(20, 5)
    encounter = choice([Goblin(10, 2), Medic(10, 2), Shadow(2), Zombie(6, 1), "peaceful"])
    ui = UI()

    ui.clear()
    
    ui.title_screen()
    
    
    
    while player.alive():
        encounter = choice([Goblin(10, 2), Medic(10, 2), Shadow(2), Zombie(6, 1), "peaceful"])
        if encounter == "peaceful":
            if randint(0, 10) > 2:
                peaceful_turn_screen()
            else:
                chest = TreasureChest()
                treasure_chest_screen(chest.contains())
        else:
            combat(encounter, player)
    

if __name__ == "__main__":
    main()
