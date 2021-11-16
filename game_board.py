import random
import hex

initial_numbers = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]
hex_types = ['WOOD', 'SHEEP', 'WHEAT', 'SHEEP', 'WHEAT', 'ORE', 'WOOD', 'WHEAT', 'ORE', 'BRICK', 'SAND', 'BRICK', 'ORE',
             'BRICK', 'WOOD', 'SHEEP', 'SHEEP', 'WOOD', 'WHEAT']


def initialize_nodes(hexes):
    with open("nodes.txt", "r") as nodestream:
        x = 0
        temp = []
        for line in nodestream:
            line = line.strip()
            cv = line.split(",")
            temp.append(hex.Node(x, hexes[ord(cv[0]) - 97], hexes[ord(cv[1]) - 97], hexes[ord(cv[2]) - 97], int(cv[3]) - 1,
                                 int(cv[4]) - 1, int(cv[5]) - 1, 0))
            x += 1
        return temp


def initialize_edges():
    with open("edges.txt", "r") as edgestream:
        temp = []
        for line in edgestream:
            line = line.strip()
            cv = line.split(",")
            temp.append(hex.Edge(int(cv[0]) - 1, int(cv[1]) - 1, 0))
        return temp


class GameBoard:
    def __init__(self):
        self.hexes = self.randomize_game_board()
        self.nodes = initialize_nodes(self.hexes)
        self.edges = initialize_edges()
        self.initialize_first_settlements()

    def randomize_game_board(self):
        hexes = []
        current_number = 0
        x = 0
        while len(hex_types) > 0:
            current_hex = hex_types.pop(0)
            if current_hex == 'SAND':
                hexes.append(hex.Hex(current_hex, chr(97 + x), -1))
            else:
                hexes.append(hex.Hex(current_hex, chr(97 + x), initial_numbers[current_number]))
                current_number = current_number + 1
            x += 1

        hexes.append(hex.Hex('WATER', chr(97 + 19), -1))
        # print(hexes)
        return hexes

    # Returns list of available settlement locations for player
    # If first turn, does not require road
    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def get_all_node_distances(self):
        selected_node = self.nodes[28] #testing
        
        selected_node_id= self.get_index_of_node(selected_node)
        self.get_edges_connected_to_node(selected_node_id)

        # get node index of selected node
        # get temp stack of all nodes
        # retrieve list of all edges connected to that selected node
            # get nodes connected to edges
            # pop list of nodes from list
            # push nodes and distnace into dictionary 
            # push edges into list (distance ++)


        visited_nodes = []
        edge_queue = []
        visited_nodes.append(selected_node)
        edge_queue.append(selected_node_id)

        while edge_queue: 
            temp = edge_queue.pop(0)
            print(temp, end = " ")

            for next_edge in  
        
        pass

    def get_node_connected_to_edge(self, selected_node):
        for node in self.nodes: 
            if(node.hex_one == selected_node.hex_one or node.hex_two == selected_node.hex_two or node.hex_three == selected_node.hex_three):
                print(node)

    def get_edges_connected_to_node(self, selected_node_id):
        for edge in self.edges: 
            if(selected_node_id == edge.node_one or selected_node_id == edge.node_two):
                print(edge) 
    
    def get_index_of_node(self, selected_node):
        return self.nodes.index(selected_node)

    # loop through nodes and determine which ones are 2 away from settlement, return distance in roads and resources
    def find_available_settlements(self):
        pass

    def find_available_cities(self):
        curr_settlements = []
        for node in self.nodes:
            if node.value == 1:
                curr_settlements.append(node)
        return curr_settlements

    def initialize_first_settlements(self):
        resource = ['ORE', 'SHEEP', 'WHEAT', 'BRICK', 'WOOD']
        self.nodes[35].value = 1
        self.nodes[40].value = 1
        self.edges[46].value = 1
        self.edges[50].value = 1



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
