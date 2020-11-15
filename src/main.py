from board import *
from node import *
from default_args import *
from tree_algorithm import *
import matplotlib.pyplot as plt
import random
board = [[0 for i in range(args.board_size)] for j in range(args.board_size)]
boardObject = Board(board)
board = boardObject.board


def AI_turn():
    """
    MCTS Algorithm runs
    """

    MCTS_AI = MCTS(board,
                   players_in_turn=[1, 2],  # brain is 1
                   n_in_row=args.n_in_row,
                   confidence=1.96,
                   time_limit=args.time_limit,
                   max_simulation=args.max_simulation,  # should not be too large
                   max_simulation_one_play=args.max_simulation_one_step)

    while True:
        move = MCTS_AI.get_action()
        x, y = move

        if isFree(x, y):
            break

    AI_draw(x, y)
    print("AI draws at:", x, y)
    return x, y


def game_restart():
    for x in range(boardObject.width):
        for y in range(boardObject.height):
            board[x][y] = 0

    print("OK,restart the game")


def isFree(x, y):
    """whether (x, y) is available"""
    return board[x][y] == 0


def AI_draw(x, y):
    """my turn: take the step on (x,y)"""
    if isFree(x, y):
        board[x][y] = 1
    else:
        print("Sorry Error Move")


def human_draw(x, y):
    """oppoent's turn: take the step on (x,y)"""
    if isFree(x, y):
        board[x][y] = 2
    else:
        print("Sorry Error Move and you have to redraw")
        return -1


def exchange(x1, y1, x2, y2):
    if board[x1][y1] != 2 or board[x2][y2] != 1:
        return -1
    temp = board[x1][y1]
    board[x1][y1] = board[x2][y2]
    board[x2][y2] = temp


def board_show():
    st = '  '
    for i in range(len(board[0])):
        if i > 9:
            st += str(i) + ' '
        else:
            st += ' ' + str(i) + ' '
    print(st)
    c = 0
    for row in board:
        if c > 9:
            print(c, end=' ')
        else:
            print('', c, end=' ')
        c += 1
        st = ''
        for ii in row:
            if ii == 1:
                st += 'O  '
            elif ii == 2:
                st += 'X  '
            else:
                st += '-  '
        print(st)


def redraw():
    x = input(
        "Your can give a coordinate 'x y': \nOr a pair of coordinates to exchange: \n")
    print()
    if x == 'quit':
        print('You quit.')
        return -99
    if len(x.split()) == 2:
        x = x.split()
        if human_draw(int(x[0]), int(x[1])) == -1:
            return -1
    elif len(x.split()) == 4:
        x1, y1, x2, y2 = x.split()
        if exchange(int(x1), int(y1), int(x2), int(y2)) == -1:
            return -1
    return 0


def player_play_draw():

    print('(if you want to quit, ENTER quit)')
    x = input("Your turn, please give a coordinate 'x y':")
    print()
    if x == 'quit':
        print('You quit.')
        return None
    x = x.split()
    if human_draw(int(x[0]), int(x[1])) == -1:
        return -1
    return 0


def player_play_exchange():
    print('(ENTER quit to quit game)')
    x = input(
        "Your can give a coordinate 'x y': \nOr a pair of coordinates to exchange: \n")
    print()
    if x == 'quit':
        print('You quit.')
        return -99
    if len(x.split()) == 2:
        x = x.split()

        if human_draw(int(x[0]), int(x[1])) == -1:
            return -1
        else:
            return 0
    elif len(x.split()) == 4:
        x1, y1, x2, y2 = x.split()
        if exchange(int(x1), int(y1), int(x2), int(y2)) == -1:
            return -1
        else:
            return 0

    return -1


def random_pick():
    x, y = random.sample(boardObject.availables, 1)[0]

    print(x, y)
    # board[x][y] = 2 ------test purpose

    board[x][y] = 1
    return x, y


def main1():

    board_show()
    while player_play_draw() == -1:
        continue
    AI_turn()
    board_show()
    while 1:
        result = player_play_exchange()
        if result == -99:
            break
        if result == -1:
            while redraw() == -1:
                continue
        AI_turn()
        board_show()


def main2():

    board_show()
    while player_play_draw() is not None:
        random_pick()
        # if (boardObject.check_win(1))
        board_show()


def plot_wins(winsR, winsMCS):
    left = [1, 2]
    # heights of bars
    height = [winsR, winsMCS]
    # labels for bars
    tick_label = ['winning - random', 'winning - MCTS']

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label,
            width=0.5, color=['black', 'black'])

    # naming the x-axis
    plt.xlabel('x - axis')
    # naming the y-axis
    plt.ylabel('y - axis')
    # plot title
    plt.title('Competing between two AIs')

    # function to show the plot
    plt.show()


def test_num(num):
    # count step
    winsR, winsMCS = 0, 0
    step_to_win = 0
    step_to_win_list = []
    while winsR + winsMCS < num:
        if boardObject.check_win(2, tuple(random_pick())):
            winsR += 1
            game_restart()
        elif boardObject.check_win(1, tuple(AI_turn())):
            print("MCTS steps to win are:", step_to_win)

            step_to_win = 0
            winsMCS += 1
            game_restart()
        else:
            step_to_win += 1
        # board_show()
    plot_wins(winsR, winsMCS)
    print("Rando:", winsR, "MCTSL", winsMCS)


def plot_line():
    wins = [48, 62, 79, 84, 95, 99, 100, 100, 100, 100, 100, 100]

    # setting the ranges and no. of intervals
    range = (0, 10)
    bins = 11

    # plotting a line chart
    plt.plot(wins, color='green')

    # x-axis label
    plt.xlabel('number of nodes processed each action')
    # frequency label
    plt.ylabel('MCTS winning rate per 100 games')
    # plot title
    plt.title('Num of node expanded with MCST wins')
    plt.grid(True)
    # function to show the plot
    plt.show()


if __name__ == "__main__":

    print("====Welcome to GOMOKU game!====")
    print("          Game Start!          ")
    print("      Note:Black-B,White-W     ")
    print("choose the smarter AI or dumb one: (1-for monte-carlo 2-for random pick)")
    if int(input()) == 1:
        main1()
    else:
        main2()

    #test#
    # test_num(100)
