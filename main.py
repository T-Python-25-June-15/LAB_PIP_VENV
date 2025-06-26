from art import *
from colorama import Fore, Back, Style

print(text2art("BELIEVE \nAND \nACHEIVE",font="black")) 
print(text2art("HELLO", font="sub-zero"))




#bonus
print(Fore.YELLOW + text2art("Abdulaziz A+", font="tarty1") + Style.RESET_ALL)
print(Style.RESET_ALL)
print(Back.BLUE + Fore.WHITE + Style.BRIGHT + " Hello word " + Style.RESET_ALL)


