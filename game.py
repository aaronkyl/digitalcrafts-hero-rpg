#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

from colorama import Fore, Style
from goblin import Goblin
from hero import Hero
from zombie import Zombie
from medic import Medic

def main():
    # enemy = Goblin(10, 2)
    # enemy = Zombie(6, 1)
    enemy = Medic(100, 2)
    player = Hero(20, 5)

    while enemy.alive() and player.alive():
        player.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight {}".format(type(enemy).__name__.lower()))
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
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
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            # Goblin attacks hero
            enemy.attack(player)
            if not player.alive():
                print("You are dead.")

if __name__ == "__main__":
    main()
