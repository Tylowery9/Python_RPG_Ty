import json

class Armor():
    def __init__(self):
        self.name = "No Armor"
        self.price = 0
        self.weight = 0
        self.ac = 11
        
    def name(self):
        pass

    def price(self):
        pass

    def weight(self):
        pass

    def ac (self):
        pass

    def load(self,path):
        with open(path) as f:
           Armor = json.load(f)

           print(Armor) 

