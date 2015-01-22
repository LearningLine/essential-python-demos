

class Game:
    def __init__(self):
        self.board=[]

        self.e=0
        self.x=1
        self.o=-1
        self.currentPlayer=self.o

        self.build_empty_board()

    def build_empty_board(self):
        e = self.e

        self.board = [
            [e, e, e],
            [e, e, e],
            [e, e, e],
        ]

    def __str__(self):
        text = ""
        for row in self.board:
            for c in row:
                text += ('x' if c == self.x else ('o' if c == self.o else '.'))
            text += "\n"
        text += "\n"
        return text

    def find_winner(self):
        game = self.board
        winner = None
        for i in range(3):
            sums = [
                game[0][0] + game[0][1] + game[0][2],  # row 1
                game[1][0] + game[1][1] + game[1][2],  # row 2
                game[2][0] + game[2][1] + game[2][2],  # row 3
                game[0][0] + game[1][0] + game[2][0],  # col 1
                game[0][1] + game[1][1] + game[2][1],  # col 2
                game[0][2] + game[1][2] + game[2][2],  # col 3
                game[0][0] + game[1][1] + game[2][2],  # diagonal 1
                game[0][2] + game[1][1] + game[2][0]  # diaglonal 2
            ]

            if 3 in sums:
                winner = "X"

            if -3 in sums:
                winner = "O"

        return winner

    def cell_already_played(self, row, col):
        return not self.board[row][col] == self.e


    def play_cell(self, row, col):
        self.board[row][col] = self.currentPlayer

    @property
    def hasWinner(self):
        return self.find_winner()

    def swap_players(self):
        self.currentPlayer *= -1