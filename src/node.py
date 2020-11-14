import copy


class Node:
    '''
    The Node class is to record individual board state during the MCTS algorithm. Notice the rollouts are not purely random
    the neighbors of opponents will be explored.
    '''

    def __init__(self, move, players_in_turn=None, parent=None,
                 num_child=-1, possible_child_moves=None, possible_expand_moves=None,
                 board_width=None, board_height=None, num_expand=None):
        self.move = move
        self.parent = parent
        self.children = []
        self.sim_num = 0
        self.win_num = 0
        self.winner = 0
        # root node will have no parents and inherit child's moves
        if parent is None:
            self.max_num_child = num_child
            self.max_num_expansion = num_expand
            self.board_width = board_width
            self.board_height = board_height
            self.possible_child_moves = copy.deepcopy(
                possible_child_moves)
            self.possible_expand_moves = copy.deepcopy(
                possible_expand_moves)
            # child node
        if parent is not None:
            if parent.max_num_child > 0:
                self.max_num_child = parent.max_num_child - 1
            # avoid expanding a move twice
            parent.possible_expand_moves.remove(move)

            # independently inherit
            self.possible_child_moves = copy.deepcopy(
                parent.possible_child_moves)
            self.possible_child_moves.remove(move)
            # update the neighbor information
            self.possible_expand_moves = copy.deepcopy(
                parent.possible_expand_moves)
            self.board_width = parent.board_width
            self.board_height = parent.board_height
            x, y = move
            up, down, left, right = x, self.board_height - 1 - x, y, self.board_width - 1 - y
            if up:
                self.possible_expand_moves.add((x - 1, y))
                if left:
                    self.possible_expand_moves.add((x - 1, y - 1))
                if right:
                    self.possible_expand_moves.add((x - 1, y + 1))
            if down:
                self.possible_expand_moves.add((x + 1, y))
                if left:
                    self.possible_expand_moves.add((x + 1, y - 1))
                if right:
                    self.possible_expand_moves.add((x + 1, y + 1))
            if left:
                self.possible_expand_moves.add((x, y - 1))
            if right:
                self.possible_expand_moves.add((x, y + 1))
            self.possible_expand_moves = self.possible_expand_moves & self.possible_child_moves
            self.max_num_expansion = len(self.possible_expand_moves)
            self.opponent = parent.player
            self.player = parent.opponent
            parent.children.append(self)
            self.winner = parent.winner
        else:
            # reverse turn
            self.player = players_in_turn[1]
            self.opponent = players_in_turn[0]
