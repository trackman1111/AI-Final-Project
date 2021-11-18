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

    def get_all_node_distances(self, owned_nodes):
        # initialize
        not_visited = self.get_all_node_ids()
        node_distance_dict = {}
        for node in owned_nodes:
            current_nodes = [node.node_id]
            neighboring_nodes = []
            count = 1

            while count <= 2 and len(current_nodes) != 0:
                for temp_node in current_nodes:
                    if temp_node in not_visited:
                        not_visited.remove(temp_node)
                for temp_node in current_nodes:
                    for i in self.get_neighboring_nodes(self.nodes[temp_node]):
                        if i in not_visited:
                            if not self.nodes[i].node_id in node_distance_dict:
                                node_distance_dict[self.nodes[i].node_id] = count
                            if self.nodes[i].node_id in node_distance_dict and node_distance_dict[self.nodes[i].node_id] > count:
                                node_distance_dict[self.nodes[i].node_id] = count
                            neighboring_nodes.append(self.nodes[i].node_id)
                current_nodes = []
                current_nodes.extend(neighboring_nodes)
                neighboring_nodes = []
                current_nodes = list(set(current_nodes))
                count += 1

        return node_distance_dict

    def node_path_owned_from_selected(self, selected_node):
        not_visited = self.get_all_node_ids()
        found = False;
        found_node = -1
        adjacent_array = []
        node_distance_dict = {}
        current_nodes = [selected_node.node_id]
        while not found:
            for temp_node in current_nodes:
                not_visited.remove(temp_node)
            for temp_node in current_nodes:
                for i in self.get_neighboring_nodes(self.nodes[temp_node]):
                    if i in not_visited:
                        adjacent_array.append(self.nodes[i].node_id)
                node_distance_dict[self.nodes[temp_node].node_id] = adjacent_array
                current_nodes.extend(adjacent_array)
                adjacent_array = []
                current_nodes = list(set(current_nodes))

            for node in current_nodes:
                if self.nodes[node].value >= 1:
                    found = True
                    found_node = self.nodes[node].node_id

        path = self.get_edge_path(self.bfs(node_distance_dict, selected_node.node_id, found_node))
        return path

    def get_edge_path(self, input_nodes):
        path = []
        for x in range(0, len(input_nodes) - 1):
            if self.edges[self.nodes[input_nodes[x]].edge_one].node_one == self.nodes[input_nodes[x+1]].node_id:
                path.append(self.nodes[input_nodes[x]].edge_one)
            if self.edges[self.nodes[input_nodes[x]].edge_one].node_two == self.nodes[input_nodes[x+1]].node_id:
                path.append(self.nodes[input_nodes[x]].edge_one)
            if self.edges[self.nodes[input_nodes[x]].edge_two].node_one == self.nodes[input_nodes[x+1]].node_id:
                path.append(self.nodes[input_nodes[x]].edge_two)
            if self.edges[self.nodes[input_nodes[x]].edge_two].node_two == self.nodes[input_nodes[x+1]].node_id:
                path.append(self.nodes[input_nodes[x]].edge_two)
            if self.edges[self.nodes[input_nodes[x]].edge_three].node_one == self.nodes[input_nodes[x+1]].node_id:
                path.append(self.nodes[input_nodes[x]].edge_three)
            if self.edges[self.nodes[input_nodes[x]].edge_three].node_two == self.nodes[input_nodes[x+1]].node_id:
                path.append(self.nodes[input_nodes[x]].edge_three)
        return path


    def bfs(self, graph, start, end):
        parent = {}
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node == end:
                return self.backtrace(parent, start, end)
            for adjacent in graph.get(node, []):
                if node not in queue:
                    parent[adjacent] = node  # <<<<< record its parent
                    queue.append(adjacent)

    def backtrace(self, parent, start, end):
        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        return path

    def get_neighboring_nodes(self, selected_node):
        neighboring_nodes = []
        for edge in self.edges:
            if edge.node_one == (selected_node.node_id) and edge.value != 1:
                neighboring_nodes.append(edge.node_two)
            if edge.node_two == (selected_node.node_id) and edge.value != 1:
                neighboring_nodes.append(edge.node_one)
        return neighboring_nodes

    def get_index_of_node(self, selected_node):
        return self.nodes.index(selected_node)


    def get_all_node_ids(self):
        return list(range(0, len(self.nodes)))

    # loop through nodes and determine which ones are 2 away from settlement, return distance in roads and resources
    def find_available_settlements(self):
        pass

    def find_available_cities(self):
        curr_settlements = []
        for node in self.nodes:
            if node.value == 2:
                curr_settlements.append(node)
        return curr_settlements

    def find_owned_nodes(self):
        curr_nodes = []
        for node in self.nodes:
            if node.value >= 1:
                curr_nodes.append(node)
        return curr_nodes

    def initialize_first_settlements(self):
        resource = ['ORE', 'SHEEP', 'WHEAT', 'BRICK', 'WOOD']
        self.add_settlement(35)
        self.add_settlement(40)
        self.build_road(46)
        self.build_road(50)



    # Set node value at location to 1
    def add_settlement(self, selected_node):
        print("selected settlement is: ", selected_node)
        self.nodes[selected_node].value = 2

    # Set node value at location to 2
    def upgrade_to_city(self, selected_node):
        print("selected city is: ", selected_node)
        self.nodes[selected_node].value = 3

    # Sets edge value at location to true (1)
    def build_road(self, selected_edge):
        self.edges[selected_edge].value = 1
        if self.nodes[self.edges[selected_edge].node_two].value < 1:
            self.nodes[self.edges[selected_edge].node_two].value = 1
        if self.nodes[self.edges[selected_edge].node_one].value < 1:
            self.nodes[self.edges[selected_edge].node_one].value = 1

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
