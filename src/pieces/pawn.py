from src.pieces.Chess_Piece import ChessPiece


class Pawn(ChessPiece):
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col, "pawn")

    def valid_move(self):
        valid_moves = []
        current_row = self.position[0]
        current_col = self.position[1]
        dr=1 if self.colour == "white" else -1
        new_row, new_col = current_row + dr, current_col
        if 0 <= new_row <= 7 and 0 <= new_col <= 7:
            valid_moves.append((new_row, new_col))
        if self.colour=="white":
            if 1==current_row:
              dr=2
              new_row, new_col = current_row + dr, current_col
              if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                  valid_moves.append((new_row, new_col))
        else:
            if 6==current_row:
                dr=-2
                new_row, new_col = current_row + dr, current_col
                if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                    valid_moves.append((new_row, new_col))
        return valid_moves
