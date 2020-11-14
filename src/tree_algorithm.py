from board import *
from node import *
from default_args import *
import time
import random
import math


class MCTS:
    def __init__(self, board, players_in_turn, n_in_row=5,
                 confidence=2.0, time_limit=1.0, max_simulation=5, max_simulation_one_play=50):
        self.time_limit = float(time_limit)
        self.max_simulation = max_simulation
        self.max_simulation_one_play = max_simulation_one_play
        # a deep copy Board class object
        self.MCTSboard = Board(board, n_in_row)
        # confidence level of exploration
        self.confidence = confidence
        self.player_turn = players_in_turn
        self.get_player = {
            self.player_turn[0]: self.player_turn[1],
            self.player_turn[1]: self.player_turn[0],
        }
        self.sims = 0
        # always the AI first when calling this Algorithm
        self.player = self.player_turn[0]
        self.root = Node(None,
                         parent=None,
                         # here is a reverse, because root is your opponent
                         players_in_turn=players_in_turn,
                         num_child=len(self.MCTSboard.availables),
                         possible_child_moves=self.MCTSboard.availables,
                         possible_expand_moves=self.MCTSboard.neighbors,
                         num_expand=len(self.MCTSboard.neighbors),
                         board_width=self.MCTSboard.width,
                         board_height=self.MCTSboard.height)

    def get_action(self):
        if len(self.MCTSboard.availables) == 1:
            return list(self.MCTSboard.availables)[0]  # the only choice

        num_nodes = 0
        begin_time = time.time()

        while time.time() - begin_time < self.time_limit:
            # Selection & Expansion
            node_to_expand = self.select_and_expand()
            num_nodes += 1
            # Simulation & back propagation

            for _ in range(self.max_simulation):
                self.sims += 1
                board_deep_copy = copy.deepcopy(self.MCTSboard)
                self.simulate_and_bp(board_deep_copy, node_to_expand)

        if args.detail:
            print("total nodes expanded in one action:{}".format(num_nodes))

        percent_wins, move = max(
            (child.win_num / child.sim_num + child.winner, child.move)
            for child in self.root.children
        )  # choose a move with highest winning rate
        if args.detail:
            for child in self.root.children:
                if child.win_num / child.sim_num > 0.4:
                    print(child.win_num / child.sim_num, child.move)
            print('=-'*20)
            print(percent_wins, move)
        f = open("0.4_100_node_processed.txt", "a")
        f.write(str(num_nodes) + ",")
        f.close()

        return move

    def select_and_expand(self):
        "Selection: greedy search based on UCB value"
        cur_node = self.root
        while cur_node.children:
            # check if current node is fully expanded
            if len(cur_node.children) < cur_node.max_num_expansion:
                break

            ucb, select_node = 0, None
            for child in cur_node.children:

                ucb_child = child.win_num / child.sim_num + math.sqrt(
                    2 * math.log(cur_node.sim_num) / child.sim_num
                )
                if ucb_child >= ucb:
                    ucb, select_node = ucb_child, child
            cur_node = select_node

        "Expansion: randomly expand a node"
        expand_move = random.choice(
            list(cur_node.possible_expand_moves))
        expand_node = Node(expand_move, parent=cur_node)
        return expand_node

    def simulate_and_bp(self, cur_board, expand_node):
        # first get to the board now
        _node = expand_node

        while _node.parent.move:
            _node = _node.parent
            cur_board.update(_node.player, _node.move, update_neighbor=False)

        "Simulation: do simulation randomly & neighborly"
        if len(cur_board.neighbors) == 0:
            return

        cur_board.neighbors = cur_board.get_neighbors()
        player = expand_node.player
        win = cur_board.check_win(player, expand_node.move)
        if win:
            expand_node.winner = player
        cur_board.update(player, expand_node.move)

        #
        while not len(cur_board.neighbors) or not win:

            player = self.get_player[player]
            move = random.choice(list(cur_board.neighbors))
            win = cur_board.check_win(player, move)
            cur_board.update(player, move)

        "Back propagation"
        cur_node = expand_node
        while cur_node:
            cur_node.sim_num += 1
            if win and cur_node.player == player:
                # print('--------', player)
                # for row in cur_board.board:
                #     print(' '.join([str(i) for i in row]))
                cur_node.win_num += 1
            cur_node = cur_node.parent
