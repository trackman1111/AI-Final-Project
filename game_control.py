import random
import enum 
import ai
import game_board
from player import Player
import numpy as np







#if __name__ == '__main__':
class GamePlay:
    def __init__(self):
        self.game = game_board.GameBoard()
        self.player = Player(1, True)
        self.score = self.player.score
        self.frame_iteration = 0

    def reset(self):
        self.game = game_board.GameBoard()
        self.player = Player(1,True)
    
    def play_step(self,action):
        self.frame_iteration+=0
        typeAction = np.where(action==1)
        if typeAction==0:
            self.distributeresources()
        if typeAction <=1 and typeAction>=73:
            typeAction=-1
            self.placeRoads(typeAction)
        if typeAction <=74 and typeAction>=128:
            typeAction=-73
            self.placeSettlement(typeAction)
        if typeAction<=129:
            typeAction=-128
            self.upgradeToCity(typeAction)
            
            
    def roll(self):
        dice=random.randint(1,6)+random.randint(1,6)
        
    reward=0    
        
        
        
    def placeSettlement(self,action):
        self.game.add_settlement(self.player.create_settlement(action))
        reward=+1
        return reward
        
    
    def upgradeToCity(self,action):
        self.game.upgrade_to_city(self.player.upgrade_to_city(action))
        reward=+2
        return reward
        
    
    def placeRoads(self,action):
        self.game.build_road(self.player.build_road(action))

    
    def distribute_resources(self):
        self.player.receive_resources(self.game.distibute_resouces(self.roll))
    

    #while True:
    #    score = game_board.calculate_score()
    #    if score > 10:
    #        break
    #    ai.make_decision(game_board.get_values())
    #    distribute_resources(random.randint(1, 6) + random.randint(1, 6))








