from src.pieces.Chess_Piece import ChessPiece


class Rook(ChessPiece):
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col, "rook")

    def valid_move(self, row, col):
        pass
