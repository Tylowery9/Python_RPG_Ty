import json

class Character():
    def __init__(self):
        self.name = "player"
        self.strength = 0
        self.intelligence = 0
        self. wisdom = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.race = "no race"
        self.Class = "no class"
        self.level = 1
        self.hit_point_max = 8
        self.movement = 0
        self.armors = []
        self.weapons = []
        self.xp = 0
        self.type = "no type"
        self.current_weapon = "none"
        self.current_armor = "none"



    def set_current_weapon(self):
        pass

    def roll_to_hit(self):
        return 20

    def roll_for_damage(self):
        return 4

    def get_ac(self):
        return 13

    def get_movement(self):
        pass

    def get_ability_bonuses(self):
        pass

    def load_from_file(self,path):
        with open(path) as f:
            character = json.load(f) 


    def save_character_to_file(self):
        pass

    
    
