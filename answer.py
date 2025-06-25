from art import text2art
from colorama import init, Fore, Back, Style
result = text2art("BELIEVE AND ACHEIVE", font = "block")
result2 = text2art("HELLO", font = "sub-zero")
print(result)
print(result2)
bonus1 = text2art("I can do it", font = "rounded")
init()
bonus2 = Fore.RED +"HELLO"
print(bonus1)
print(bonus2) 