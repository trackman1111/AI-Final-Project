import random
import hex


initial_numbers = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]
hex_types = ['SAND', 'ORE', 'ORE', 'ORE', 'WHEAT', 'WHEAT', 'WHEAT', 'WHEAT',
             'WOOD', 'WOOD', 'WOOD', 'WOOD', 'SHEEP', 'SHEEP', 'SHEEP',
             'SHEEP', 'BRICK', 'BRICK', 'BRICK']


def initialize_nodes():
    with open("nodes.txt", "r") as nodestream:
        temp = []
        for line in nodestream:
            cv = line.split(",")
            temp.append(hex.Node(cv[0], cv[1], cv[2], cv[3] - 1, cv[4] - 1, cv[5] - 1, 0))
        return temp


def initialize_edges():
    with open("edges.txt", "r") as edgestream:
        temp = []
        for line in edgestream:
            cv = line.split(",")
            temp.append(hex.Edge(cv[0] - 1, cv[1] - 1, 0))
        return temp


class GameBoard:
    def __init__(self):
        self.hexes = self.randomize_game_board()
        self.nodes = initialize_nodes()
        self.edges = initialize_edges()

    def randomize_game_board(self):
        hexes = []
        current_number = 0
        for x in range(0, 19):
            current_hex = hex_types.pop(random.randrange(len(hex_types)))
            if current_hex == 'SAND':
                hexes.append(hex.Hex(current_hex, chr(97 + x), -1))
            else:
                hexes.append(hex.Hex(current_hex, chr(97 + x), initial_numbers[current_number]))
                current_number = current_number + 1

        hexes.append(hex.Hex('WATER', chr(97 + 19), -1))
        print(len(hexes))
        return hexes

    # Returns list of available settlement locations for player
    # If first turn, does not require road
    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    #loop through nodes and determine which ones are 2 away from settlement, return distance in roads and resources
    def find_available_settlements(self):
        pass

    def find

    # Set node value at location to 1
    def add_settlement(self, selected_node):
        selected_node.value = 1

    # Set node value at location to 2
    def upgrade_to_city(self, selected_node):
        selected_node.value = 2

    # Sets edge value at location to true (1)
    def build_road(self, selected_edge):
        selected_edge.value = 1

    # Finds hexes with dice roll value not blocked by robber
    # Returns array of 4x5 with resources allocated to each player
    def distibute_resouces(self, dice_roll):
        resources = [0, 0, 0, 0, 0]
        for curHex in self.hexes:
            if dice_roll == curHex.value:
                for node in curHex.getNodes():
                    if curHex.resource == 'SHEEP':
                        resources[0] += node.value
                    if curHex.resource == 'WHEAT':
                        resources[1] += node.value
                    if curHex.resource == 'WOOD':
                        resources[2] += node.value
                    if curHex.resource == 'BRICK':
                        resources[3] += node.value
                    if curHex.resource == 'ORE':
                        resources[4] += node.value

        return resources
