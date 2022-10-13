from xml.dom.pulldom import CHARACTERS
import random 


class Combat():
    def __init__(self,player_characters,NPCs,player_ply_function,endgame_function):
        self.player_characters = player_characters
        self.NPCs = NPCs
        self.interactive_mode = False
        self.party_xp = 0
        self.party_success = False
        self.ordered_combatants = []
        self.player_ply_function = player_ply_function
        self.endgame_function = endgame_function

    def are_all_players_dead(self,characters):
        dead_characters = []
        for character in characters:
            if character.hit_point_max <=0:
                dead_characters.append(character)
        if len(characters) == len(dead_characters):
            return True

        else: 
            return False


    

    def is_combat_over(self):
        if self.are_all_players_dead(self.player_characters) or self.are_all_players_dead(self.NPCs):
            return True
        
        else: 
            return False
        

    def end_combat(self):
        if not self.are_all_players_dead(self.player_characters):
            self.party_success = True

        return self.party_success
        pass

    def ply(self,attacker,defender):
        hit_roll = attacker.roll_to_hit()
        hit = False

        if hit_roll > defender.get_ac():
            damage_roll = attacker.roll_for_damage()
            defender.hit_point_max = defender.hit_point_max - damage_roll
        
        return {
            "hit": hit,
            "hit_roll": hit_roll,
            "defender_hp": defender.hit_point_max,
            "attacker_name": attacker.name,
            "defender_name": defender.name
        }

    def print_stats(self):
        pass

    def turn(self):
        #1 Loop through everyone so everyone gets a "ply" function
        for attacker in self.ordered_combatants:
        #2 Choose an attacker and defender
            if  attacker in self.player_characters:
                attacker_is_player = True
                defender = random.choice(self.NPCs)

            else: 
                attacker_is_player = False
                defender = random.choice(self.player_characters)
        
        

            #3 ply
            result = self.ply(attacker,defender)
        
            #4 return results to client using player_ply function 
            self.player_ply_function(result)

        

            #5 Determine if the defender needs to be removed from the all combatants list 
            if result["defender_hp"] <= 0:
                self.ordered_combatants.remove(defender)
                if attacker_is_player:
                    self.NPCs.remove(defender)
            
                else: 
                    self.player_characters.remove(defender)
            #6 Determine if the game is over
            if self.is_combat_over():
                self.end_combat()
        

    def start(self):
        self.ordered_combatants = self.player_characters  +  self.NPCs
        while not self.is_combat_over():
            winner = self.turn()

        self.endgame_function(winner)
    