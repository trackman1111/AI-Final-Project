import random


class Player:
    def __init__(self):
        self.num_sheep = 0
        self.num_wheat = 0
        self.num_wood = 0
        self.num_brick = 0
        self.num_ore = 0
        self.num_settlements=0
        self.num_cities=0
        self.num_roads=0
        self.score = 0

    def create_settlement(self, selected_location):
        self.num_sheep -= 1
        self.num_wheat -= 1
        self.num_wood -= 1
        self.num_brick -= 1
        self.num_settlements +=1
        # set node at location to 1

    def upgrade_to_city(self, locations):
        self.num_wheat -= 2
        self.num_ore -= 3
        self.num_cities +=1
        # set node at location to 1

    def build_road(self, locations):
        self.num_wood -= 1
        self.num_brick -= 1
        self.num_roads +=1
        # set edge at location to 1

    def receive_resources(self, sheep, wheat, wood, brick, ore):
        self.num_sheep += sheep
        self.num_wheat += wheat
        self.num_wood += wood
        self.num_brick += brick
        self.num_ore += ore

    def get_resources(self):
        current_resources = [self.num_sheep, self.num_ore, self.num_wood, self.num_wheat, self.num_brick]
        return current_resources
