import random
from hex import Hex

initial_numbers = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]
hex_types = ['SAND', 'ORE', 'ORE', 'ORE', 'WHEAT', 'WHEAT', 'WHEAT', 'WHEAT',
             'WOOD', 'WOOD', 'WOOD', 'WOOD', 'SHEEP', 'SHEEP', 'SHEEP',
             'SHEEP', 'BRICK', 'BRICK', 'BRICK']
nodes = []
edges = []


class GameBoard:
    def __init__(self):
        self.blocked_hex = 'none'
        self.hexes = self.randomize_game_board()

    def block(self, hex_id):
        self.blocked_hex = hex_id

    def randomize_game_board(self):
        hexes = []
        current_number = 0
        for x in range(0, 19):
            current_hex = hex_types.pop(random.randrange(len(hex_types)))
            if current_hex == 'SAND':
                hexes.append(Hex(current_hex, chr(97 + x), -1))
                self.block(chr(97 + x))
            else:
                hexes.append(Hex(current_hex, chr(97 + x), initial_numbers[current_number]))
                current_number = current_number + 1
        return hexes

    # Returns list of available settlement locations for player
    # If first turn, does not require road
    def find_available_settlements(self, player_id, is_first):
        return None

    # Set node value at location to 1
    def add_settlement(self, selected_location, player_id):
        return None

    # Returns list of current settlements made by player
    def find_current_settlements(self, player_id):
        return None

    # Set node value at location to 2
    def upgrade_to_city(self, selected_location, player_id):
        return None

    # Sets edge value at location to true (1)
    def build_road(self, selected_location, player_id):
        return None

    # Finds hexes with dice roll value not blocked by robber
    # Returns array of 4x5 with resources allocated to each player
    def distibute_resouces(self, dice_roll):
        return None
