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
    ui.clear()
    ui.start_screen()
    ui.clear()
    
    while player.alive():
        ui.main_screen()
        encounter = choice([Goblin(10, 2), Medic(10, 2), Shadow(2), Zombie(6, 1), "peaceful"])
        if encounter == "peaceful":
            if randint(0, 10) > 2:
                ui.peaceful_turn_screen()
                ui.clear()
            else:
                chest = TreasureChest()
                treasure = chest.contains()
                ui.treasure_chest_screen(treasure)
                ui.clear()
        else:
            combat(encounter, player)
    

if __name__ == "__main__":
    main()
