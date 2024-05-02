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