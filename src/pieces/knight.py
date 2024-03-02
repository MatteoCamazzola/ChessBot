from src.pieces.Chess_Piece import ChessPiece
class Knight(ChessPiece):
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col, "knight")
    def valid_move(self, row, col):
        pass
