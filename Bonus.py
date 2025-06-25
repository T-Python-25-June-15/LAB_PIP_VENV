from art import text2art
from colorama import init, Fore, Style


init(autoreset=True)


colors = {
    "red": Fore.RED,
    "white": Fore.WHITE,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "cyan": Fore.CYAN
}

def colors_art(text, font, color_name):
    color = colors.get(color_name.lower(), Fore.RED) 
    art = text2art(text, font=font)
    print(color + art)

print("Available fonts: block, sub-zero, small, mini, slant, shadow")
print("Available colors: red, white, green, blue, cyan\n")

while True:
    user_input_art = input("Enter the text (or type 'exit' to quit): ")
    if user_input_art.lower() == "exit":
        print(Fore.YELLOW + "Goodbye! 👋")
        break

    user_input_font = input("Enter the font: ")
    user_input_color = input("Enter the color: ")

    colors_art(user_input_art, user_input_font, user_input_color)
