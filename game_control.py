import random
import enum

#import Agent
import game_board
from player import Player
import numpy as np


class GamePlay:
    def __init__(self):
        self.game = game_board.GameBoard()
        self.player = Player()
        self.frame_iteration = 0
        self.score = 0
        self.reward = 0

    def play_step(self, action):
        self.frame_iteration += 0
        type_action = np.where(action == 1)
        if type_action == 0:
            pass
        elif 1 >= type_action >= 73:
            type_action = -1
            self.place_roads(type_action)
        elif 74 >= type_action >= 128:
            type_action = -73
            self.place_settlement(type_action)
        elif type_action <= 129:
            type_action = -128
            self.upgradeToCity(type_action)

    def place_settlement(self, action):
        self.game.add_settlement(self.player.create_settlement(action))
        self.score +=1
        reward = +1
        return reward

    def upgrade_to_city(self, action):
        self.game.upgrade_to_city(self.player.upgrade_to_city(action))
        self.score += 1
        reward = +1
        return reward

    def place_roads(self, action):
        self.game.build_road(self.player.build_road(action))
        self.score += 1

    def distribute_resources(self):
        self.player.receive_resources(self.game.distibute_resouces())


if __name__ == '__main__':
    game_control = GamePlay()
    print(game_control.game.get_all_node_distances(game_control.game.find_owned_nodes()))
    # for node in game_control.game.find_available_cities():
    #     print(node.hex_one.resource + node.hex_two.resource + node.hex_three.resource)
    #while game_control.score < 10:
        #game_control.play_step(Agent.decision())
