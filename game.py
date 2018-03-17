import os
from characters import *
from colorama import init, Fore, Style
from ui import UI
from random import choice, randint
from combat_engine import combat
from items.treasurechest import TreasureChest
from store import Store

def main():
    player = Hero(20, 5)
    encounter = choice([Goblin(10, 2), Medic(10, 2), Shadow(2), Zombie(6, 1), "peaceful"])
    ui = UI()

    ui.clear()
    ui.title_screen()
    ui.clear()
    ui.start_screen()
    
    while player.alive():
        ui.clear()
        ui.main_screen()
        raw_input = input().upper()
        if raw_input == 'C':
            encounter = choice([Goblin(10, 2), Medic(10, 2), Shadow(2), Zombie(1, 6), "peaceful"])
            if encounter == "peaceful":
                ui.clear()
                if randint(0, 10) > 5:
                    ui.peaceful_turn_screen()
                else:
                    chest = TreasureChest()
                    treasure = chest.contains()
                    ui.treasure_chest_screen(treasure)
                    if type(treasure).__name__.lower() == "goldpouch":
                        player.purse += treasure.value
                    else:
                        player.inventory[treasure.name] = treasure
            else:
                ui.clear()
                combat(encounter, player)
        elif raw_input == 'R':
            ui.clear()
            store = Store()
            ui.store_screen(store)
            purchase = input("Enter number of item to buy item or press" + Fore.GREEN + " Enter" + Style.RESET_ALL+ " to leave > ")
            if purchase:
                purchase = int(purchase) - 1
                ### THIS IS BROKEN
                if store.inventory[purchase].name in player.inventory:
                    player.inventory[store.inventory[purchase].name].quantity += 1
                else:
                    player.inventory[store.inventory[purchase].name] = store.inventory[purchase]
        elif raw_input == 'U':
            ui.clear()
            ui.view_player_inventory(player)
            item_to_use = int(input("Enter the number of the item to use or press" + Fore.GREEN + " Enter" + Style.RESET_ALL+ " to leave > ")) - 1
            player.inventory[item_to_use].use(player)
            player.inventory[item_to_use].quantity -= 1
            if player.inventory[item_to_use].quantity == 0:
                del player.inventory[item_to_use]
        elif raw_input == 'A':
            ui.clear()
            ui.abandonment_screen()
            ui.clear()
            ui.game_over_screen()
            break
        else:
            continue
    

if __name__ == "__main__":
    main()
