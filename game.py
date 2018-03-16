#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import os
from characters import *
from colorama import init, Fore, Style
from ui import UI
from random import choice

def main():
    player = Hero(20, 5)
    enemy = choice([Goblin(10, 2), Medic(10, 2), Shadow(2), Zombie(6, 1)])
    ui = UI()

    ui.clear()
    
    while enemy.alive() and player.alive():
        ui.print_status(player, enemy)
        print()
        ui.print_menu(enemy)
        raw_input = input()
        if raw_input == "1":
            player.attack(enemy)
            if not enemy.alive():
                print("The {} is dead.".format(type(enemy).__name__.lower()))
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input: {}. {} has a chance to attack!".format(raw_input, type(enemy).__name__.lower()))

        if enemy.alive():
            # Goblin attacks hero
            enemy.attack(player)
            if not player.alive():
                print("You are dead.")
        
        input("Press Enter to continue...")
        os.system('cls||clear')

if __name__ == "__main__":
    main()
