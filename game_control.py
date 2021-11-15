import random
import enum
import game_board
from player import Player
import numpy as np


# if __name__ == '__main__':
class GamePlay:
    def __init__(self):
        self.game = game_board.GameBoard()
        self.player = Player()
        self.frame_iteration = 0

    def reset(self):
        self.game = game_board.GameBoard()
        self.player = Player()

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

    reward = 0

    def place_settlement(self, action):
        self.game.add_settlement(self.player.create_settlement(action))
        reward = +1
        return reward

    def upgrade_to_city(self, action):
        self.game.upgrade_to_city(self.player.upgrade_to_city(action))
        reward = +1
        return reward

    def place_roads(self, action):
        self.game.build_road(self.player.build_road(action))

    def distribute_resources(self):
        self.player.receive_resources(self.game.distibute_resouces())

    # while True:
    #    score = game_board.calculate_score()
    #    if score > 10:
    #        break
    #    ai.make_decision(game_board.get_values())
    #    distribute_resources(random.randint(1, 6) + random.randint(1, 6))
