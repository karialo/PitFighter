import os

class Character_Screen:
    def __init__(self):
        clear()

    

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def title(text):
    length = (40 - len(text)) / 2 
    print("="*40)
    print(" "*int(length) ,text)
    print("="*40,"\n")

def footer(text):
    print("="*40)
    print(f" {text}")
    print("="*40,"\n")

def page(title_text, output, footer_text):
    clear()
    title(title_text)
    print(output, "\n")
    footer(footer_text)

def main_menu():
    menu = ("1. Create Character", "2. Create Enemy", "\n3. Battle\n" "\n0. Exit")
    output = ""
    clear()
    for option in menu:
        output += f"{option}\n"
    return output
    