from src.pieces.Chess_Piece import ChessPiece
class Knight(ChessPiece):
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col, "knight", 3)
    def valid_move(self):
        valid_moves = []
        current_row = self.position[0]
        current_col = self.position[1]
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                        (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for dr, dc in knight_moves:
            new_row, new_col = current_row + dr, current_col + dc
            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                valid_moves.append((new_row, new_col))

        return valid_moves
