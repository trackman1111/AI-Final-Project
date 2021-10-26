import game_board
from player import Player

players = [Player(1, False), Player(2, True), Player(3, False), Player(4, False)]

if __name__ == '__main__':
    game = game_board.GameBoard()
    hexes = game.hexes
    for cur_hex in hexes:
        print(cur_hex.__str__())

    # while True:
    #     for player in players:
    #         player_roll = player.roll_dice()
    #         game.distibute_resouces(player_roll)
    #         curr_input = ""
    #         while curr_input != "5":
    #             curr_input = input("Enter Decision: \n"
    #                                + "0 for trade"
    #                                + "1 for settlement"
    #                                + "2 for road"
    #                                + "3 for city"
    #                                + "4 for buy card"
    #                                + "5 for play card"
    #                                + "6 for end turn")
    #             if curr_input == "0":
    #                 player.request_trade()
    #             elif curr_input == "1":
    #                 player.create_settlement()
    #             elif curr_input == "2":
    #                 player.build_road()
    #             elif curr_input == "3":
    #                 player.upgrade_to_city()
    #             elif curr_input == "4":
    #                 player.buy_card()
    #             elif curr_input == "5":
    #                 player.play_card()
    #         if player.score >= 10:
    #             print("You win!")
    #             break
    #
    #     for player in player:
    #         print("Current Score for player " + player.player_id + ": " + player.score)


