class Hex:

    def __init__(self, hex_type, hex_id, number):
        self.number = number
        self.id = hex_id
        self.type = hex_type

    def __str__(self):
        return "Hex: " + self.id + " Hex Type: " + self.type + " Hex Number: " + str(self.number)
