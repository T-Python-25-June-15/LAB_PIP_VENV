from art import text2art
from colorama import Fore, Style

# Bonus Section - More Art + Colors
print(Fore.YELLOW + text2art("PYTHON POWER", font='random'))
print(Fore.MAGENTA + text2art("CODE WITH PURPOSE", font='slant'))
print(Fore.BLUE + text2art("NEVER GIVE UP", font='fancy1'))
print(Fore.RED + text2art("STAY CURIOUS", font='cybermedium'))

# Extra Style
print(Fore.LIGHTWHITE_EX + Style.BRIGHT + text2art("INSPIRE", font='tarty1'))
