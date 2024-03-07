from src.pieces.Chess_Piece import ChessPiece


class Bishop(ChessPiece):
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col, "bishop", 3)
