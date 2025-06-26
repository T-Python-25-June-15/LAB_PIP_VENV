from art import tprint, text2art
from colorama import init, Fore



print(tprint("BELIEVE AND ACHEIVE", font="block"))
print(tprint("HELLO", font="sub-zero"))

print(Fore.YELLOW + text2art("Python", font="digital"))
print(Fore.RED + text2art("Code", font="slant"))
print(Fore.MAGENTA + text2art("Art", font=("speed")))
