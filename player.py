import random


class Player:
    def __init__(self):
        self.num_sheep = 0
        self.num_wheat = 0
        self.num_wood = 0
        self.num_brick = 0
        self.num_ore = 0
        self.num_settlements = 2
        self.num_cities = 0
        self.num_roads = 2
        self.score = 0

    def create_settlement(self, selected_location):
        self.num_sheep -= 1
        self.num_wheat -= 1
        self.num_wood -= 1
        self.num_brick -= 1
        self.num_settlements += 1
        # set node at location to 1

    def upgrade_to_city(self, locations):
        self.num_wheat -= 2
        self.num_ore -= 3
        self.num_cities += 1
        # set node at location to 1

    def build_road(self, locations):
        self.num_wood -= 1
        self.num_brick -= 1
        self.num_roads += 1
        # set edge at location to 1

    def receive_resources(self, resources):
        self.num_sheep += resources[0]
        self.num_wheat += resources[1]
        self.num_wood += resources[2]
        self.num_brick += resources[3]
        self.num_ore += resources[4]

    def can_build_road(self):
        if self.num_brick >= 1 and self.num_wood >= 1:
            return True
        return False

    def can_build_settlement(self):
        if self.num_sheep >= 1 and self.num_wheat >= 1 and self.num_brick >= 1 and self.num_wood >= 1:
            return True
        return False

    def can_build_city(self):
        if self.num_ore >= 3 and self.num_wheat >= 2:
            return True
        return False

    def get_resources(self):
        current_resources = [self.num_sheep, self.num_ore, self.num_wood, self.num_wheat, self.num_brick]
        return current_resources
