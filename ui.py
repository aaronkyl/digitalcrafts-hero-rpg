from colorama import init, Fore, Style
import os

class UI:
    def __init__(self):
        pass
    
    def print_status(self, player, target):
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
        
    def print_menu(self, target):
        print("What do you want to do?")
        print("1. fight {}".format(type(target).__name__.lower()))
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        
    def clear(self):
        os.system('cls||clear')