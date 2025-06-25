from art import text2art
from colorama import Fore, Back, Style

print(text2art("BELIEVE AND ACHEIVE",font='block'))
print("-"*20)
print(text2art("HELLO" ,font='sub-zero'))
print("-"*20)
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "PYTHON" + Style.RESET_ALL)

print("-"*20)
text = input("Type your text:")
color= input('''
    Choose text color :
             1. Red
             2. Green
             3. bule
             ''')

if color == "1":
    print(Fore.RED + text +  Style.RESET_ALL)
elif color == "2":
    print(Fore.GREEN + text + Style.RESET_ALL)
elif color == "3":
    print(Fore.BLUE + text + Style.RESET_ALL)
else:
    print("Invalid choice.")



