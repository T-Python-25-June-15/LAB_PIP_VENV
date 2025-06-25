from art import *
from colorama import Fore, Back, Style

Art=text2art("BELIEVE AND ACHEIVE",font='block',chr_ignore=True) 
Art2=text2art("HELLO",font='sub-zero',chr_ignore=True) 
Art3=text2art("Sarah",font='stforek',chr_ignore=True) 
print(Art)
print(Art2)
print(Fore.RED + Back.GREEN + Art3)