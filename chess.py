class Piece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

class Pawn(Piece):
    def get_moves(self, position, board):
        moves = []
        x, y = position
        direction = -1 if self.color == 'white' else 1
        
        if board[x + direction][y] is None:
            moves.append((x + direction, y))
            if (self.color == 'white' and x == 6) or (self.color == 'black' and x == 1):
                if board[x + 2 * direction][y] is None:
                    moves.append((x + 2 * direction, y))

        for dy in [-1, 1]:
            if 0 <= y + dy < 8:
                target = board[x + direction][y + dy]
                if target and target.color != self.color:
                    moves.append((x + direction, y + dy))

        return moves

class Rook(Piece):
    def get_moves(self, position, board):
        moves = []
        x, y = position

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] is None:
                    moves.append((nx, ny))
                elif board[nx][ny].color != self.color:
                    moves.append((nx, ny))
                    break
                else:
                    break
                nx += dx
                ny += dy
        return moves

class Knight(Piece):
    def get_moves(self, position, board):
        moves = []
        x, y = position
        knight_moves = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] is None or board[nx][ny].color != self.color:
                    moves.append((nx, ny))

        return moves

class Bishop(Piece):
    def get_moves(self, position, board):
        moves = []
        x, y = position

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] is None:
                    moves.append((nx, ny))
                elif board[nx][ny].color != self.color:
                    moves.append((nx, ny))
                    break
                else:
                    break
                nx += dx
                ny += dy

        return moves

class Queen(Piece):
    def get_moves(self, position, board):
        moves = []
        x, y = position
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] is None:
                    moves.append((nx, ny))
                elif board[nx][ny].color != self.color:
                    moves.append((nx, ny))
                    break
                else:
                    break
                nx += dx
                ny += dy
        return moves

class King(Piece):
    def get_moves(self, position, board):
        moves = []
        x, y = position
        king_moves = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        for dx, dy in king_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] is None or board[nx][ny].color != self.color:
                    moves.append((nx, ny))
        return moves

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

        def print_board(self):
            for row in self.board:
                print(' '.join([piece.name if piece else '.' for piece in row]))

if __name__ == '__main__':
    chess_board = Board()
    chess_board.print_board()