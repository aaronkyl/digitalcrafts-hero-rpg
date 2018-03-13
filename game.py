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

    while enemy.health > 0 and player.health > 0:
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
            if enemy.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.health > 0:
            # Goblin attacks hero
            player.health -= enemy.power
            print("The goblin does {} damage to you.".format(enemy.power))
            if player.health <= 0:
                print("You are dead.")

main()
