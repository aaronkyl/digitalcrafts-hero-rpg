from items import *
from random import randint
from ui import UI
ui = UI()

def combat(enemy, player):
    while enemy.alive() and player.alive():
        ui.print_combat_status_table(player, enemy)
        print()
        ui.print_combat_menu(enemy)
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
            enemy.attack(player)
            if not player.alive():
                print(Fore.RED + Style.BRIGHT + "You have failed..." + Style.RESET_ALL)
        
        input("Press" + Fore.GREEN + " Enter to continue..." + Style.RESET_ALL)
        
        # clear the screen
        ui.clear()