class Piece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

class Pawn(Piece):
    pass

class Rook(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

class Board:
        def __init__(self):
            self.board = [[None for _ in range(8)] for _ in range(8)]
            self.setup_pieces()

        def setup_pieces(self):
            for i in range(8):
                self.board[1][i] = Pawn('black', 'P')
                self.board[6][i] = Pawn('white', 'P')
            self.board[0][0] = self.board[0][7] = Rook('black', 'R')
            self.board[7][0] = self.board[7][7] = Rook('white', 'R')
            self.board[0][1] = self.board[0][6] = Knight('black', 'N')
            self.board[7][1] = self.board[7][6] = Knight('white', 'N')
            self.board[0][2] = self.board[0][5] = Bishop('black', 'B')
            self.board[7][2] = self.board[7][5] = Bishop('white', 'B')
            self.board[0][3] = Queen('black', 'Q')
            self.board[0][4] = King('black', 'K')
            self.board[7][3] = Queen('white', 'Q')
            self.board[7][4] = King('white', 'K')