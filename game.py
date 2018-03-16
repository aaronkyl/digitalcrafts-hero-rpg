import os
from characters import *
from colorama import init, Fore, Style
from ui import UI
from random import choice
from game_engine import combat

def main():
    player = Hero(20, 5)
    enemy = choice([Goblin(10, 2), Medic(10, 2), Shadow(2), Zombie(6, 1)])
    ui = UI()

    ui.clear()
    
    combat(enemy, player)
    os.system('cls||clear')

if __name__ == "__main__":
    main()
