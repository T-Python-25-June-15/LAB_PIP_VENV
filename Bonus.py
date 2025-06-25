from art import *
from colorama import Fore, Back, Style

print(Style.BRIGHT + Fore.WHITE + "\n--- WELLCOME TO APP ---")

user_name = input('What is your name? ')
print(f'Wellcom {user_name}')


menu = '''
1. show my name with alligator2 font
2. show my name with dancingfont font 
3. exit 
'''
while True:
    user_choise = int(input(menu))
    match user_choise:
        case 1:
            name = text2art(user_name, font='alligator2')
            print(Fore.CYAN + Style.DIM + name)


        case 2:
            name = text2art(user_name, font='dancingfont')
            print(Fore.CYAN + Style.DIM + name)

        case 3:
            print(text2art(f'Goodby {user_name}', font='random'))
            header_decoration = decor("barcode1")
            print(Fore.CYAN + Style.DIM + header_decoration)
            print(Fore.RESET)
            break

        case _:
            print('invalid number')


