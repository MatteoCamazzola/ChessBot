from src.pieces.Chess_Piece import ChessPiece
class King(ChessPiece):
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col, "king", 10000)
        self.has_moved = False

    def valid_move(self):
        valid_moves=[]
        current_row= self.position[0]
        current_col =self.position[1]
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row, new_col = current_row + dr, current_col + dc
                if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                    valid_moves.append((new_row,new_col))
        return valid_moves

