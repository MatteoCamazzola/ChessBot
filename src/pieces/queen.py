from src.pieces.Chess_Piece import ChessPiece


class Queen(ChessPiece):
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col, "queen")

    def valid_move(self):
        valid_moves = []
        current_row = self.position[0]
        current_col = self.position[1]

        row_temp = current_row
        col_temp = current_col

        # diagonal one
        while (row_temp + 1) < 8 and (col_temp + 1) < 8:
            row_temp = row_temp + 1
            col_temp = col_temp + 1
            valid_moves.append(row_temp)
            valid_moves.append(col_temp)
        # diagonal two
        row_temp = current_row
        col_temp = current_col
        while (row_temp - 1) > -1 and (col_temp - 1) > -1:
            row_temp = row_temp - 1
            col_temp = col_temp - 1
            valid_moves.append(row_temp)
            valid_moves.append(col_temp)
        row_temp = current_row
        col_temp = current_col
        # diagonal three
        while (row_temp + 1) < 8 and (col_temp - 1) > -1:
            row_temp = row_temp + 1
            col_temp = col_temp - 1
            valid_moves.append(row_temp)
            valid_moves.append(col_temp)
        row_temp = current_row
        col_temp = current_col
        # diagonal four
        while (row_temp - 1) > -1 and (col_temp + 1) < 8:
            row_temp = row_temp - 1
            col_temp = col_temp + 1
            valid_moves.append(row_temp)
            valid_moves.append(col_temp)

        row_temp = current_row
        col_temp = current_col

        # forward
        while (row_temp + 1) < 8:
            row_temp = row_temp + 1
            valid_moves.append(row_temp)
            valid_moves.append(col_temp)

        row_temp = current_row
        col_temp = current_col

        # backwards
        while (row_temp - 1) > -1:
            row_temp = row_temp - 1
            valid_moves.append(row_temp)
            valid_moves.append(col_temp)

        row_temp = current_row
        col_temp = current_col

        # right
        while (col_temp + 1) < 8:
            col_temp = col_temp + 1
            valid_moves.append(row_temp)
            valid_moves.append(col_temp)

        row_temp = current_row
        col_temp = current_col

        # left
        while (col_temp - 1) > -1:
            col_temp = col_temp - 1
            valid_moves.append(row_temp)
            valid_moves.append(col_temp)

        return valid_moves
