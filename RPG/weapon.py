import json

class weapon():
    def __init__(self):
        self.name = "no weapon"
        self.price = 0
        self.size = 0
        self.weight = 0
        self.damage_low = 1
        self.damage_high = 4


    
    
    def name(self):
        pass

    def price(self):
        pass

    def size(self):
        pass

    def weight(self):
        pass

    def damage_low(self):
        pass

    def damage_high(self):
        pass

    def load(self,path):
        with open(path) as f:
           weapon = json.load(f)

           print(weapon)




