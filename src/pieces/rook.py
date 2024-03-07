from src.pieces.Chess_Piece import ChessPiece


class Rook(ChessPiece):
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col, "rook", 5)
        self.has_moved = False
