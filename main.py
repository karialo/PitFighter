#!/usr/bin/python3

import player
import ui
import items
import enemy

while True:
    ui.page("Main Menu", ui.main_menu(), "Enter your choice:")
    choice = input("")
    if choice == "1":
        ui.clear()
        player = player.Player()
        ui.page(f"{player.name}'s Stats", player.display_stats(), "Press enter to return.")
        input()
    elif choice == "2":
        enemy = enemy.Ogre()
        ui.page(f"{enemy.name}'s Stats", enemy.display_stats(), "Press enter to return")
        input()
    elif choice == "3":
        pass # battle
    elif choice == "0":
        ui.clear()
        quit()


player.add_item(items.Gold(150))
player.add_item(items.Dagger())
