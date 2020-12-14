
"""
Human VS AI opponent
for draw action input format: x,y
for exchange action input format: x1,y1, x2,y2
"""

from __future__ import print_function
import pickle
import torch
from gomoku import *
from human import *
from baseline import *
from mcts import MCTSPlayer as MCTS_Pure
from mcts_nn import *
from net import PolicyValueNetNumpy as net



def option_choose():
    # option_size = 0
    # opponent = 0
    print("Welcome to Gomuku game \n")
    print("==============================")
    print("Please choose size: \n 1. 3*3 - 3 in a row \n 2. 6*6 - 4 in a row \n 3. 8*8 - 5 in a row \n 4. 10*10 - 5 in a row \n 5. 12*12 - 5 in a row" )
    option_size = input("choose your size here: ")
    print("Please choose opponent: \n 1. human \n 2. baseline AI \n 3. tree-based AI \n 4. tree+NN-based AI")
    opponent = input("choose your opponent here: ")
    return option_size,opponent

def run():
    #size set up
    option_size,opponent = option_choose()

    if option_size == '1':
        width, height, n = 3, 3, 3
    elif option_size == '2':
        width, height, n = 6, 6, 4
    elif option_size == '3':
        width, height, n = 8, 8, 5
    elif option_size == '4':
        width, height, n = 10, 10, 5
    elif option_size == '5':
        width, height, n = 12, 12, 5
    else:
        print("invalid size option, game end.")
        return

    #opponent set up
    if opponent == '1':
        player2 = Human()
    elif opponent == '2':
        player2 = Random()
    elif opponent == '3':
        player2 = MCTS_Pure(c_puct=5, n_playout=1000)
    elif opponent == '4':
        if option_size == '1':
            model_file = 'model1.model'
            player2 = MCTS_Pure(c_puct=5, n_playout=1000)
        elif option_size == '2':
            model_file = 'model2.model'
            policy_param = pickle.load(open(model_file, 'rb'), encoding='bytes')
            best_policy = net(width, height, policy_param)
            player2 = MCTSPlayer(best_policy.policy_value_fn, c_puct=5, n_playout=400)
        elif option_size == '3':
            model_file = 'model3.model'
            policy_param = pickle.load(open(model_file, 'rb'), encoding='bytes')
            best_policy = net(width, height, policy_param)
            player2 = MCTSPlayer(best_policy.policy_value_fn, c_puct=5, n_playout=400)
        elif option_size == '4':
            model_file = 'model4.model'
            player2 = MCTS_Pure(c_puct=5, n_playout=1000)
        else:
            model_file = 'model5.model'
            player2 = MCTS_Pure(c_puct=5, n_playout=1000)


    else:
        print("invalid opponent option, game end.")
        return


    # start game
    try:
        board = Board(width=width, height=height, n_in_row=n)
        game = Game(board)
        player1 = Human()
        game.start_play(player1, player2, start_player=1, is_shown=1)
    except KeyboardInterrupt:
        print('\n\rquit')




if __name__ == '__main__':
    run()

