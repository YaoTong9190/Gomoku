import copy


class Board:
    '''
    Initialize the Gomoku board with 15 by 15 grids and the rule of thumb is 5 pieces in a row
    for each draw the method check_win will examine whether the move will cause the winner 

    '''

    def __init__(self, board, n_in_row=5):
        self.width = len(board[0])
        self.height = len(board)
        self.board = copy.deepcopy(board)
        self.n_in_row = n_in_row
        self.availables = set([
            (i, j) for i in range(self.height) for j in range(self.width) if board[i][j] == 0
        ])
        self.neighbors = self.get_neighbors()
        self.winner = None

    def get_neighbors(self):
        neighbors = set()
        if len(self.availables) == self.width * self.height:
            "if the board is empty, then choose from the center one"
            "assume our board is bigger than 1x1"
            x0, y0 = self.width // 2 - 1, self.height // 2 - 1
            neighbors.add((x0, y0))
            return neighbors
        else:
            for i in range(self.height):
                for j in range(self.width):
                    if self.board[i][j]:
                        neighbors.add((i - 1, j - 1))
                        neighbors.add((i - 1, j))
                        neighbors.add((i - 1, j + 1))
                        neighbors.add((i, j - 1))
                        neighbors.add((i, j + 1))
                        neighbors.add((i + 1, j - 1))
                        neighbors.add((i + 1, j))
                        neighbors.add((i + 1, j + 1))

            return neighbors & self.availables

    def update(self, player, move, update_neighbor=True):
        """
        update the board and check if player wins, so one should use like this:
            if board.update(player, move):
                winner = board.winner
        :param player: the one to take the move
        :param move: a tuple (x, y)
        :param update_neighbor: built for periods when you are sure no one wins
        :return: 1 denotes player wins and 0 denotes not
        """
        assert len(move) == 2, "move is invalid, length = {}".format(len(move))
        self.board[move[0]][move[1]] = player
        self.availables.remove(move)

        if update_neighbor:
            self.neighbors.remove(move)

            neighbors = set()
            x, y = move
            up, down, left, right = x, self.height - 1 - x, y, self.width - 1 - y
            if up:
                neighbors.add((x - 1, y))
                if left:
                    neighbors.add((x - 1, y - 1))
                if right:
                    neighbors.add((x - 1, y + 1))
            if down:
                neighbors.add((x + 1, y))
                if left:
                    neighbors.add((x + 1, y - 1))
                if right:
                    neighbors.add((x + 1, y + 1))
            if left:
                neighbors.add((x, y - 1))
            if right:
                neighbors.add((x, y + 1))
            neighbors = self.availables & neighbors
            self.neighbors = self.neighbors | neighbors

    def check_win(self, player, move):
        """check if player win, this function will not actually do the move"""
        original = self.board[move[0]][move[1]]
        self.board[move[0]][move[1]] = player
        x_this, y_this = move
        # get the boundaries
        up = min(x_this, self.n_in_row - 1)
        down = min(self.height - 1 - x_this, self.n_in_row - 1)
        left = min(y_this, self.n_in_row - 1)
        right = min(self.width - 1 - y_this, self.n_in_row - 1)
        # \
        up_left = min(up, left)
        down_right = min(down, right)
        for i in range(up_left + down_right - self.n_in_row + 2):
            a = [
                self.board[x_this - up_left + i + j][y_this - up_left + i + j] for j in range(self.n_in_row)
            ]
            assert len(a) == self.n_in_row, "error when check if win on board"
            if len(set(a)) == 1 and a[0] > 0:
                self.board[move[0]][move[1]] = original
                return 1
        # /
        up_right = min(up, right)
        down_left = min(down, left)
        for i in range(up_right + down_left - self.n_in_row + 2):
            a = [
                self.board[x_this - up_right + i + j][y_this + up_right - i - j] for j in range(self.n_in_row)
            ]
            assert len(a) == self.n_in_row, "error when check if win on board"
            if len(set(a)) == 1 and a[0] > 0:
                self.board[move[0]][move[1]] = original
                return 1
        # --
        for i in range(left + right - self.n_in_row + 2):
            a = [
                self.board[x_this][y_this - left + i + j] for j in range(self.n_in_row)
            ]
            assert len(a) == self.n_in_row, "error when check if win on board"
            if len(set(a)) == 1 and a[0] > 0:
                self.board[move[0]][move[1]] = original
                return 1
        # |
        for i in range(up + down - self.n_in_row + 2):
            a = [
                self.board[x_this - up + i + j][y_this] for j in range(self.n_in_row)
            ]
            assert len(a) == self.n_in_row, "error when check if win on board"
            if len(set(a)) == 1 and a[0] > 0:
                self.board[move[0]][move[1]] = original
                return 1
        # no one wins
        self.board[move[0]][move[1]] = original
        return 0
