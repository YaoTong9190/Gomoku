import numpy as np


class Gomoku:
    #Initialize function
    def __init__(self):
        self.widthGrid = 15
        self.heightGrid = 15
        self.board = np.zeros((self.widthGrid, self.heightGrid), dtype=int)
        self.turn = 0
        self.win = False
        self.flag_empty = 0

    #Go board display function
    def show(self):
        print("======Current Board State======")
        print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                         for row in self.board]))
        print('\n')

    #Game start function
    def game_start(self):
        # first turn, no need to exchange
        self.show()
        self.drawGo()
        print("You don't have right to exchange for the first turn.")
        self.turnChange()
        self.show()
        self.drawGo()
        print("You don't have right to exchange for the first turn.")
        self.turnChange()

        # after the first turn
        while True:
            self.show()
            self.drawGo()
            self.win = self.isWin()
            if self.win: break

            self.show()
            self.exchangeGo()
            self.win = self.isWin()
            if self.win: break
            self.turnChange()



    def drawGo(self):
        current_player = "Black" if self.turn == 0 else "White"
        print("Draw Go Action: " + current_player)
        is_valid = False
        coordinate = 0,0
        while not is_valid:
            coordinate = eval(input("Please enter the coordinate you want to draw:"))
            is_valid = self.isDrawValid(coordinate)
            if is_valid: break
            else: print("Your coordinate is inValid, please enter a valid coordinate.")
        x, y = coordinate
        if self.turn == 0:
            self.board[x, y] = 1  # player 1 with black chess
        else:
            self.board[x, y] = 2  # player 2 with white chess
        if self.isWin():
            self.win = True


    def exchangeGo(self):
        current_player = "Black" if self.turn == 0 else "White"
        print("Exchange Go Action: " + current_player)
        is_valid = False
        while True:
            coordinate1 = eval(input("Please enter the original coordinate: "))
            coordinate2 = eval(input("Please enter the exchange coordinate: "))
            is_valid = self.isExchangeValid(coordinate1, coordinate2)
            if is_valid is False: print("Your action is invalid, please re-enter your number!")
            else: break
        x1, y1 = coordinate1
        x2, y2 = coordinate2
        self.board[x1][y1], self.board[x2][y2] = self.board[x2][y2], self.board[x1][y1]

    def isWin(self):
        for i in range(15):
            for j in range(15):
                if self.board[i][j] == 0:
                    continue
                if i<=10:
                    color = self.board[i][j]
                    count = 1
                    for step in range(1,5):
                        if self.board[i+step][j] == color:
                            count += 1
                    if count == 5 : return True
                if j<=10:
                    color = self.board[i][j]
                    count = 1
                    for step in range(1, 5):
                        if self.board[i][j+step] == color:
                            count += 1
                    if count == 5: return True
                if i<=10 and j<=10:
                    color = self.board[i][j]
                    count = 1
                    for step in range(1, 5):
                        if self.board[i + step][j + step] == color:
                            count += 1
                    if count == 5: return True
                if i<=10 and j>=4:
                    color = self.board[i][j]
                    count = 1
                    for step in range(1, 5):
                        if self.board[i + step][j - step] == color:
                            count += 1
                    if count == 5: return True
        return False

    def turnChange(self):
        self.turn = (self.turn+1)%2


    def isDrawValid(self, coordinate):
        x, y = coordinate
        if x<0 or x>=self.widthGrid or y<0 or y>=self.heightGrid or self.board[x][y] != 0:
            return False
        return True

    def isExchangeValid(self, coordinate1, coordinate2):
        x1, y1 = coordinate1
        x2, y2 = coordinate2
        # boundary check
        if x1<0 or x1>self.widthGrid or y1<0 or y1>self.heightGrid or x2<0 or x2>self.widthGrid or y2<0 or y2>self.heightGrid:
            return False
        # blank go and same go color check
        if self.board[x1][y1] == self.board[x2][y2] or self.board[x1][y1] == 0 or self.board[x2][y2] == 0:
            return False
        return True

    def game_end(self):
        winner = "Black" if self.turn==0 else "White"

        print("Congraulations! " + winner + " win the game!")
        self.show()


if __name__ == "__main__":
    print("====Welcome to GOMOKU game!====")
    print("          Game Start!          ")
    print("      Note:Black-1,White-2     ")
    game = Gomoku()
    game.game_start()
    game.game_end()
