from RPG import character
import random

class generator():
    def __init__(self):
        pass

    def character(self):
        char = character()
        char.hit_point_max = 6
        char.strength = random.randint(3,19)
        char.intelligence = random.randint(3,19)
        char.wisdom = random.randint(3,19)
        char.dexterity = random.randint(3,19)
        char.constitution = random.randint(3,19)
        char.charisma = random.randint(3,19)

        char.race = random.choice(["Human, Dwarf", "Elf"])
        char.Class = random.choice(["Fighter","Thief","Cleric"])

        return char
