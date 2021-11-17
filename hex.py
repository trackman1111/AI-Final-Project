class Hex:
    def __init__(self, resource, hex_id, value):
        self.resource = resource
        self.hex_id = hex_id
        self.value = value


class Node:
    def __init__(self, node_id, hex_one, hex_two, hex_three, edge_one, edge_two, edge_three, value):
        self.node_id = node_id
        self.value = value
        self.edge_three = edge_three
        self.edge_two = edge_two
        self.edge_one = edge_one
        self.hex_three = hex_three
        self.hex_two = hex_two
        self.hex_one = hex_one


class Edge:
    def __init__(self, node_one, node_two, value):
        self.value = value
        self.node_two = node_two
        self.node_one = node_one
