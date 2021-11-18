import random

import game_board
from player import Player
import numpy as np


def roll():
    dice = random.randint(1, 6) + random.randint(1, 6)
    while dice == 7:
        dice = random.randint(1,6) + random.randint(1,6)
    return int(dice)


class GamePlay():
    def __init__(self):
        self.game=game_board.GameBoard()
        self.player = Player()
        self.score = self.player.score
        self.iteration = 0
        self.reward = 0
 
        
    def reset(self):
        self.game.reset()
        self.player.refresh()
        self.score = self.player.score
        self.iteration = 0
        self.reward = 0
 


    def play_step(self, action):
        print("Turn",self.iteration)
        self.iteration += 1
        type_tuple = np.where(action == 1)
        type_action=int(type_tuple[0][0])
        #print(type(type_action))
        print("Type before subtraction",type_action)
        #if type_action == 0
        self.distribute_resources()
        if 0 <= type_action <= 71 and self.player.can_build_road():
            #type_action -=1
            print("Type action for road: ",type_action)
            self.place_roads(type_action)
        elif 72 <= type_action <= 125 and self.player.can_build_settlement():
            type_action -= 72
            print("Type action for settlement: ",type_action)
            self.place_settlement(type_action)
        elif type_action >= 126 and self.player.can_build_city():
            type_action -=126
            print("Type action for city: ",type_action)
            self.upgrade_to_city(type_action)
        elif type_action == 181:
            print("end turn")
        
        done=bool(self.score==10)
        if(done):
            print("Game over")
        return self.reward,done,self.score

    def place_settlement(self, action):
        self.game.add_settlement(action)
        self.player.create_settlement(action)
        self.score +=1
        reward = +1
        return reward

    def upgrade_to_city(self, action):
        self.game.upgrade_to_city(action)
        self.player.upgrade_to_city(action)
        self.score += 1
        reward = +1
        return reward

    def place_roads(self, action):
        self.game.build_road(action)
        self.player.build_road(action)
        self.score += 1

    def distribute_resources(self):
        self.player.receive_resources(self.game.distribute_resouces(int(roll())))
    

    #while True:
    #    score = game_board.calculate_score()
    #    if score > 10:
    #        break
    #    ai.make_decision(game_board.get_values())
    #    distribute_resources(random.randint(1, 6) + random.randint(1, 6))






if __name__ == '__main__':
    game_control = GamePlay()
    game_control.distribute_resources()
    game_control.distribute_resources()
    game_control.distribute_resources()
    game_control.distribute_resources()
    game_control.distribute_resources()
    game_control.distribute_resources()
    game_control.distribute_resources()

    # for node in game_control.game.find_available_cities():
    #     print(node.hex_one.resource + node.hex_two.resource + node.hex_three.resource)
    #while game_control.score < 10:
        #game_control.play_step(Agent.decision())
