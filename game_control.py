import ai
import game_board
from player import Player

player = Player(1, True)

if __name__ == '__main__':
    game = game_board.GameBoard()
    hexes = game.hexes
    for cur_hex in hexes:
        print(cur_hex.__str__())

    while True:
        score = game_board.calculate_score()
        if score > 10:
            break
        distribute_resources(player.roll_dice())
        ai.find_best_build(game_board.get_layout)




def distribute_resources(roll):
    pass
    #go through all of the hexes and add resources to player
    #player.receive_resources(gameboard.distribute_resources(roll))



