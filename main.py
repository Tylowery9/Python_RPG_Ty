#print("hello world ")
from RPG.character import Character 
from RPG.weapon import weapon
from RPG.armor import Armor
from RPG.monster import Monster
from RPG.combat import Combat

def ply_function(results):
    print(results)
    print("Hi, I'm the ply function")

def end_game_function(winner):
    print(winner)
    print("game over")

monster = Monster()
monster.hit_point_max = 4

donabar = Character()
#donabar.load_from_file("characters/Donabar.json")

game = Combat([donabar],[monster],ply_function,end_game_function)
game.start()

