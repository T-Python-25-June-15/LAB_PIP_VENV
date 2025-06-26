from art import text2art
from colorama import Fore


text1 = text2art("BELIEVE AND ACHEIVE" , font="block")
print(text1)

text2 = text2art("HELLO" , font = "sub-zero") 
print(text2)

text3 = Fore.CYAN + text2art("DREAM BIG", font="block")
print(text3)