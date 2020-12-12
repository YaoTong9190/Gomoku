"""
Human player
"""

class Human(object):

    def __init__(self):
        self.player = None

    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board):
        option = input("1. draw 2. exchange:  ")
        # draw
        if option == '1':
            try:
                location = input("Your move: ")
                if isinstance(location, str):  # for python3
                    location = [int(n, 10) for n in location.split(",")]
                move = board.location_to_move(location)
            except Exception as e:
                move = -1
            if move == -1 or move not in board.availables:
                print("invalid move")
                option, move = self.get_action(board)
            return option, move

        # exchange
        elif option == '2':
            try:
                location = input("Your exchange: ")
                if isinstance(location, str):  # for python3
                    location = [int(n, 10) for n in location.split(",")]
                print(location)
                move = board.location_to_exchange(location)
            except Exception as e:
                move = -1
            if move == -1 or move[0] in board.availables or move[1] in board.availables or board.states[move[0]]==board.states[move[1]]:
                print("invalid move")
                option, move = self.get_action(board)
            return option, move

        # invalid option number
        else:
            print("invalid action")
            option, move = self.get_action(board)
            return option, move



    def __str__(self):
        return "Human {}".format(self.player)


