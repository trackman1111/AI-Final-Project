import random
import ai


class Player:
    def __init__(self, player_id, is_ai):
        self.player_id = player_id
        self.is_ai = is_ai;
        self.num_sheep = 0
        self.num_wheat = 0
        self.num_wood = 0
        self.num_brick = 0
        self.num_ore = 0
        self.score = 0

    def create_settlement(self, locations):
        if self.num_sheep > 0 and self.num_wheat > 0 and self.num_brick > 0 and self.num_wood > 0:
            if len(locations == 0):
                print("No available locations.")
                return -1
            else:
                selected_location = input("Choose from locations: " + locations)
                if selected_location in locations:
                    self.num_sheep -= 1
                    self.num_wheat -= 1
                    self.num_wood -= 1
                    self.num_brick -= 1
                    return selected_location
                else:
                    print("Unavailable.")
                    return -1
        else:
            print("Lacking resources.")

    def upgrade_to_city(self, locations):
        if self.num_wheat >= 2 and self.num_ore >= 3:
            if len(locations == 0):
                print("No available locations.")
                return -1
            else:
                selected_location = input("Choose from locations: " + locations)
                if selected_location in locations:
                    self.num_wheat -= 2
                    self.num_ore -= 3
                    return selected_location
                else:
                    print("Unavailable.")
                    return -1

    def build_road(self, locations):
        if self.num_wood >= 2 and self.num_brick >= 1:
            if len(locations == 0):
                print("No available locations.")
                return -1
            else:
                selected_location = input("Choose from locations: " + locations)
                if selected_location in locations:
                    self.num_wood -= 1
                    self.num_brick -= 1
                    return selected_location
                else:
                    print("Unavailable.")
                    return -1

    def receive_resources(self, sheep, wheat, wood, brick, ore):
        self.num_sheep += sheep
        self.num_wheat += wheat
        self.num_wood += wood
        self.num_brick += brick
        self.num_ore += ore
