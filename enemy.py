class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.level = 1
    

        self.stats = {  "Name": self.name,
                        "Level": self.level,
                        "Health": self.health,
                        "strength": self.strength  }
 
    def is_alive(self):
        return self.health > 0
    
    def display_stats(self):
        output = ""
        for i in self.stats:
            output += f"{i+':':>12} {self.stats[i]}\n"
            if "Level" in i:
                output += "\n"
        output += ""
        return output

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", health=10, strength=2)
 
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", health=30, strength=15)
