
"""
Random player
"""

import random

class Random(object):

    def __init__(self):
        self.player = None

    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board):
        if len(board.states) < 2:
            option = 1
        else:
            option = random.randint(1,2)
        # option = 1
        if option == 1:
            index = random.randint(0,len(board.availables))
            print(index)
            move = board.availables[index]
            return str(option), move
        else:
            while(True):
                move1 = random.choice(list(board.states.keys()))
                move2 = random.choice(list(board.states.keys()))
                if board.states[move1] != board.states[move2]:
                    break
            return str(option), [move1,move2]

    def __str__(self):
        return "Random {}".format(self.player)