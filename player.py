import ui
import items
import random

class Player():
    def __init__(self):
        self.name = input("Enter your character's name: ")
        self.level = 1
        self.gold = 0
        self.inventory = []

        self.health = 30
        self.max_health = self.health

        self.mana = 30
        self.max_mana = 30

        self.strength = 5
        self.max_strength = self.strength

        self.toughness = 5
        self.max_toughness = self.toughness

        self.accuracy = 5
        self.max_accuracy = self.accuracy

        self.dodge = 5
        self.max_dodge = self.dodge

        self.initiative = 5
        self.max_initiative = self.initiative


        self.stats = {
                        "Name": self.name,
                        "Gold": self.gold,
                        "Health": self.health,
                        "Mana": self.mana,
                        "Strength": self.strength,
                        "Toughness": self.toughness,
                        "Accuracy": self.accuracy,
                        "Dodge": self.dodge,
                        "Initiative": self.initiative
                                                        }

        self.max_stats= {   
                        "Max Health": self.max_health,
                        "Max Mana": self.max_mana,
                        "Max Strength": self.max_strength,
                        "Max Toughness": self.max_toughness,
                        "Max Accuracy": self.max_accuracy,
                        "Max Dodge": self.max_dodge,
                        "Max Initiative": self.max_initiative
                                                        }
    def is_alive(self):
        return self.health > 0

    def display_stats(self):
        output = ""
        for i in self.stats:
            output += f"{i+':':>15} {self.stats[i]}\n"
            if "Gold"  in i:
                output += "\n"
            if "Mana" in i:
                output += "\n"
        output += ""
        return output

    def display_inventory(self):
        output = ""
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                output += f"{i.name} (Damage: {i.damage})\n"
            else:
                output += f"{i.name} ({i.amount})\n"
            output += f"  {i.description}\n\n"
        return output

    def add_item(self, item):
        self.inventory.append(item)
    
    def attack(self, enemy):
        output = ""
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
        output += f"{enemy.name} " ####
        output += f"You use {best_weapon.name} against {enemy.name}!\n"
        enemy.health -= best_weapon.damage
        if not enemy.is_alive():
            output += f"You killed {enemy.name}!"
        else:
            output += f"{enemy.name} has {enemy.health} left."
        return output