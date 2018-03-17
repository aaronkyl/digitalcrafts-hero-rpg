from colorama import init, Fore, Style
from items.treasurechest import TreasureChest
import os

class UI:
    def __init__(self):
        pass
    
    def print_combat_status_table(self, player, target):
        print(Fore.WHITE + Style.BRIGHT + "*---------------------------*" + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "|          |" + Fore.CYAN + " Health" + Fore.WHITE + " |" + Fore.CYAN + " Power" + Fore.WHITE + " |" + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "+---------------------------+" + Style.RESET_ALL)
        
        if player.health <= 5:
            print(Fore.WHITE + Style.BRIGHT + "|   Hero   |" + Fore.RED + "   {}".format(str(player.health).zfill(2)) + Fore.WHITE + "   |" + Fore.WHITE + "  {}".format(str(player.power).zfill(2)) + "   |" + Style.RESET_ALL)
        elif player.health <= 10:
            print(Fore.WHITE + Style.BRIGHT + "|   Hero   |" + Fore.YELLOW + "   {}".format(str(player.health).zfill(2)) + Fore.WHITE + "   |" + Fore.WHITE + "  {}".format(str(player.power).zfill(2)) + "   |" + Style.RESET_ALL)
        else:
            print(Fore.WHITE + Style.BRIGHT + "|   Hero   |   {}   |  {}   |".format(str(player.health).zfill(2), str(player.power).zfill(2)) + Style.RESET_ALL)
        
        print(Fore.WHITE + Style.BRIGHT + "+---------------------------+" + Style.RESET_ALL)
        
        if target.health <= 5:
            print(Fore.WHITE + Style.BRIGHT + "|  {} |".format(type(target).__name__.ljust(7)) + Fore.RED + "   {}".format(str(target.health).zfill(2)) + Fore.WHITE + "   |" + Fore.WHITE + "  {}".format(str(target.power).zfill(2)) + "   |" + Style.RESET_ALL)
        elif target.health <= 10:
            print(Fore.WHITE + Style.BRIGHT + "|  {} |".format(type(target).__name__.ljust(7)) + Fore.YELLOW + "   {}".format(str(target.health).zfill(2)) + Fore.WHITE + "   |" + Fore.WHITE + "  {}".format(str(target.power).zfill(2)) + "   |" + Style.RESET_ALL)
        else:
            print(Fore.WHITE + Style.BRIGHT + "|  {} |" + Fore.YELLOW + "   {}".format(str(player.health).zfill(2)) + Fore.WHITE + "   |" + Fore.WHITE + "  {}".format(str(player.power).zfill(2)) + "   |")

        print(Fore.WHITE + Style.BRIGHT + "*---------------------------*" + Style.RESET_ALL)
        
    def print_combat_menu(self, target):
        print("What do you want to do?")
        print("1. fight {}".format(type(target).__name__.lower()))
        print("2. do nothing")
        print("3. flea") # if user chooses "flea" they turn into a flea with 1 HP >:)
        print("> ", end=' ')
        
    def clear(self):
        os.system('cls||clear')
    
    def title_screen(self):
        print("                     _        ____                 _   ")
        print("  /\  /\___ _ __ ___( )__    /___ \_   _  ___  ___| |_ ")
        print(" / /_/ / _ \ '__/ _ \/ __|  //  / / | | |/ _ \/ __| __|")
        print("/ __  /  __/ | | (_) \__ \ / \_/ /| |_| |  __/\__ \ |_ ")
        print("\/ /_/ \___|_|  \___/|___/ \___,_\ \__,_|\___||___/\__|")
        print()
        print()
        print()
        print()
        print()
        print()
        input("Press" + Fore.GREEN + " Enter" + Style.RESET_ALL+ " to continue...")
        
    def start_screen(self):
        print("You enter the door at the back of the shop's storeroom,")
        print("determined to save your brother from whatever unholy")
        print("creatures took him during the last full moon. You find")
        print("yourself in a downward-sloping tunnel, nothing but")
        print("darkness ahead.")
        print()
        print("You begin walking...")
        print()
        input("Press" + Fore.GREEN + " Enter" + Style.RESET_ALL+ " to continue...")
    
    def main_screen(self):
        print("The tunnel continues forward into the unending darkness,")
        print("its gentle downward slope unchanging.")
        print("Will you (C)ontinue, (R)esupply, or (A)bandon your quest?")
        for i in range(0, 8):
            print()
        print("> ", end=' ')
        
    def peaceful_turn_screen(self):
        print("You continue down the tunnel, the sound of dripping")
        print("liquids everpresent even though you have yet to see")
        print("any signs of water.")
        for i in range(0, 8):
            print()
        input("Press" + Fore.GREEN + " Enter" + Style.RESET_ALL+ " to continue...")
    
    def treasure_chest_screen(self, contents):
        print("You come across a treasure chest sitting in the middle")
        print("of the tunnel! You open it and find" + Fore.YELLOW + Style.BRIGHT + " {}!".format(contents) + Style.RESET_ALL)
        for i in range(0, 9):
            print()
        input("Press" + Fore.GREEN + " Enter" + Style.RESET_ALL+ " to continue...")

    def game_over_screen(self):
        print(Fore.RED + "                   *              )               (     ")
        print(" (        (      (  `          ( /(               )\ )  ")
        print(" )\ )     )\     )\))(   (     )\()) (   (   (   (()/(  ")
        print("(()/(  ((((_)(  ((_)()\  )\   ((_)\  )\  )\  )\   /(_)) ")
        print(" /(_))" + Fore.YELLOW + "_" + Fore.RED + " )\ " + Fore.YELLOW + "_" + Fore.RED +" )\ (_()((_)((_)    ((_)((_)((_)((_) (_))   ")
        print("(_))" + Fore.YELLOW +" __|" + Fore.RED + "(_)" + Fore.YELLOW +"_\\" + Fore.RED + "(_)" + Fore.YELLOW + "|  \/  || __|  / _ \\\ \ / / | __|| _ \  ")
        print("  | (_ | / _ \  | |\/| || _|  | (_) |\ V /  | _| |   /  ")
        print("   \___|/_/ \_\ |_|  |_||___|  \___/  \_/   |___||_|_\  " + Style.RESET_ALL)
        for i in range(0, 3):
            print()
        









                                                        
