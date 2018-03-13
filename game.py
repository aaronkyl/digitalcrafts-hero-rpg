#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

from goblin import Goblin
from hero import Hero

def main():
    enemy = Goblin()
    player = Hero()

    while enemy.alive() and player.alive():
        print("You have {} health and {} power.".format(player.health, player.power))
        print("The goblin has {} health and {} power.".format(enemy.health, enemy.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            player.attack(enemy)
            if not enemy.alive():
                print("The goblin is dead.")
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

main()
