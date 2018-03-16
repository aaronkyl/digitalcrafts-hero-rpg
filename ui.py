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
            print(Fore.WHITE + Style.BRIGHT + "|   Hero   |" + Fore.RED + "   {}".format(str(player.health).zfill(2)) + Fore.WHITE + "   |" + Fore.WHITE + "  {}".format(str(player.power).zfill(2)) + "   |")
        elif player.health <= 10:
            print(Fore.WHITE + Style.BRIGHT + "|   Hero   |" + Fore.YELLOW + "   {}".format(str(player.health).zfill(2)) + Fore.WHITE + "   |" + Fore.WHITE + "  {}".format(str(player.power).zfill(2)) + "   |")
        else:
            print(Fore.WHITE + Style.BRIGHT + "|   Hero   |   {}   |  {}   |".format(str(player.health).zfill(2), str(player.power).zfill(2)) + Style.RESET_ALL)
        
        print(Fore.WHITE + Style.BRIGHT + "+---------------------------+" + Style.RESET_ALL)
        print("|  {} |   {}   |  {}   |".format(type(target).__name__.ljust(7), str(target.health).zfill(2), str(target.power).zfill(2)))
        print(Fore.WHITE + Style.BRIGHT + "*---------------------------*" + Style.RESET_ALL)
        
    def print_menu(self, target):
        print("What do you want to do?")
        print("1. fight {}".format(type(target).__name__.lower()))
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        
    def clear(self):
        os.system('cls||clear')