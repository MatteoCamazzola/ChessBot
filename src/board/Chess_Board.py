from src.pieces.pawn import Pawn
from src.pieces.knight import Knight
from src.pieces.bishop import Bishop
from src.pieces.king import King
from src.pieces.rook import Rook
from src.pieces.queen import Queen


class Board:
    def __init__(self):
        # make board with 8x8 list
        self.chessBoard = [None] * 8
        for i in range(8):
            self.chessBoard[i] = [None] * 8

        # make all our pieces

        pawn_black_1 = Pawn("black", 6, 0)
        pawn_black_2 = Pawn("black", 6, 1)
        pawn_black_3 = Pawn("black", 6, 2)
        pawn_black_4 = Pawn("black", 6, 3)
        pawn_black_5 = Pawn("black", 6, 4)
        pawn_black_6 = Pawn("black", 6, 5)
        pawn_black_7 = Pawn("black", 6, 6)
        pawn_black_8 = Pawn("black", 6, 7)

        rook_black_1 = Rook("black", 7, 0)
        rook_black_2 = Rook("black", 7, 7)
        knight_black_1 = Knight("black", 7, 1)
        knight_black_2 = Knight("black", 7, 6)
        bishop_black_1 = Bishop("black", 4, 4)
        bishop_black_2 = Bishop("black", 7, 5)
        queen_black = Queen("black", 7, 4)
        king_black = King("black", 7, 3)

        pawn_white_1 = Pawn("white", 1, 0)
        pawn_white_2 = Pawn("white", 1, 1)
        pawn_white_3 = Pawn("white", 1, 2)
        pawn_white_4 = Pawn("white", 1, 3)
        pawn_white_5 = Pawn("white", 1, 4)
        pawn_white_6 = Pawn("white", 1, 5)
        pawn_white_7 = Pawn("white", 1, 6)
        pawn_white_8 = Pawn("white", 1, 7)

        rook_white_1 = Rook("white", 0, 0)
        rook_white_2 = Rook("white", 0, 7)
        knight_white_1 = Knight("white", 0, 1)
        knight_white_2 = Knight("white", 0, 6)
        bishop_white_1 = Bishop("white", 0, 2)
        bishop_white_2 = Bishop("white", 0, 5)
        queen_white = Queen("white", 0, 4)
        king_white = King("white", 0, 3)

        # put pieces on board
        self.chessBoard[rook_white_1.position[0]][rook_white_1.position[1]] = rook_white_1
        self.chessBoard[knight_white_1.position[0]][knight_white_1.position[1]] = knight_white_1
        self.chessBoard[bishop_white_1.position[0]][bishop_white_1.position[1]] = bishop_white_1
        self.chessBoard[queen_white.position[0]][queen_white.position[1]] = queen_white
        self.chessBoard[king_white.position[0]][king_white.position[1]] = king_white
        self.chessBoard[bishop_white_2.position[0]][bishop_white_2.position[1]] = bishop_white_2
        self.chessBoard[knight_white_2.position[0]][knight_white_2.position[1]] = knight_white_2
        self.chessBoard[rook_white_2.position[0]][rook_white_2.position[1]] = rook_white_2

        self.chessBoard[pawn_white_1.position[0]][pawn_white_1.position[1]] = pawn_white_1
        self.chessBoard[pawn_white_2.position[0]][pawn_white_2.position[1]] = pawn_white_2
        self.chessBoard[pawn_white_3.position[0]][pawn_white_3.position[1]] = pawn_white_3
        self.chessBoard[pawn_white_4.position[0]][pawn_white_4.position[1]] = pawn_white_4
        self.chessBoard[pawn_white_5.position[0]][pawn_white_5.position[1]] = pawn_white_5
        self.chessBoard[pawn_white_6.position[0]][pawn_white_6.position[1]] = pawn_white_6
        self.chessBoard[pawn_white_7.position[0]][pawn_white_7.position[1]] = pawn_white_7
        self.chessBoard[pawn_white_8.position[0]][pawn_white_8.position[1]] = pawn_white_8

        self.chessBoard[rook_black_1.position[0]][rook_black_1.position[1]] = rook_black_1
        self.chessBoard[knight_black_1.position[0]][knight_black_1.position[1]] = knight_black_1
        self.chessBoard[bishop_black_1.position[0]][bishop_black_1.position[1]] = bishop_black_1
        self.chessBoard[queen_black.position[0]][queen_black.position[1]] = queen_black
        self.chessBoard[king_black.position[0]][king_black.position[1]] = king_black
        self.chessBoard[bishop_black_2.position[0]][bishop_black_2.position[1]] = bishop_black_2
        self.chessBoard[knight_black_2.position[0]][knight_black_2.position[1]] = knight_black_2
        self.chessBoard[rook_black_2.position[0]][rook_black_2.position[1]] = rook_black_2

        self.chessBoard[pawn_black_1.position[0]][pawn_black_1.position[1]] = pawn_black_1
        self.chessBoard[pawn_black_2.position[0]][pawn_black_2.position[1]] = pawn_black_2
        self.chessBoard[pawn_black_3.position[0]][pawn_black_3.position[1]] = pawn_black_3
        self.chessBoard[pawn_black_4.position[0]][pawn_black_4.position[1]] = pawn_black_4
        self.chessBoard[pawn_black_5.position[0]][pawn_black_5.position[1]] = pawn_black_5
        self.chessBoard[pawn_black_6.position[0]][pawn_black_6.position[1]] = pawn_black_6
        self.chessBoard[pawn_black_7.position[0]][pawn_black_7.position[1]] = pawn_black_7
        self.chessBoard[pawn_black_8.position[0]][pawn_black_8.position[1]] = pawn_black_8

    @staticmethod
    def coordinates_to_index(coordinate):
        if coordinate[0] in "abcdefgh" and coordinate[1] in "12345678":
            row = int(coordinate[1]) - 1
            col = ord(coordinate[0]) - ord("a")
            return row, col
        else:
            return "Invalid"

    @staticmethod
    def index_to_coordinate(row, column):
        if -1 < row < 8 and -1 < column < 8:
            coordinate = [None, None];
            coordinate[0] = chr(column + 97)
            coordinate[1] = chr(row + 49)
            return coordinate
        else:
            return "Invalid"

    def valid_moves(self, row, col, current_position):
        list_of_moves = []
        piece = self.chessBoard[current_position[0]][current_position[1]]
        if piece.piece_type == "knight" or piece.piece_type == "king" or piece.piece_type == "pawn":
            list_of_moves = piece.valid_move()
        else:
            self.blocking_pieces(list_of_moves, piece)
        self.landing_on_own_piece(list_of_moves, piece)
        return list_of_moves

    def landing_on_own_piece(self, list_of_moves, piece):
        for move in list_of_moves:
            x, y = move
            other_piece = self.chessBoard[x][y]
            if other_piece is not None and piece.colour == other_piece.colour:
                list_of_moves.remove(move)
            if piece.piece_type == "pawn" and other_piece is not None:
                list_of_moves.remove(move)




    def blocking_pieces(self, list_of_moves, piece):
        if piece.piece_type == "bishop":
            self.bishop_valid_moves(list_of_moves, piece)
        elif piece.piece_type == "rook":
            self.rook_valid_moves(list_of_moves, piece)
        elif piece.piece_type == "queen":
            self.queen_valid_moves(list_of_moves, piece)

    def check_move_filter(self):
        pass

    def is_check(self):
        pass

    def is_valid_move(self, valid_moves):
        pass

    def bishop_valid_moves(self, valid_moves, piece):
        current_row = piece.position[0]
        current_col = piece.position[1]

        row_temp = current_row
        col_temp = current_col

        # diagonal one
        while (row_temp + 1) < 8 and (col_temp + 1) < 8:
            if self.chessBoard[row_temp + 1][col_temp + 1] != None:
                break
            row_temp = row_temp + 1
            col_temp = col_temp + 1
            valid_moves.append((row_temp, col_temp))
        # diagonal two
        row_temp = current_row
        col_temp = current_col
        while (row_temp - 1) > -1 and (col_temp - 1) > -1:
            if self.chessBoard[row_temp - 1][col_temp - 1] != None:
                break
            row_temp = row_temp - 1
            col_temp = col_temp - 1
            valid_moves.append((row_temp, col_temp))
        row_temp = current_row
        col_temp = current_col
        # diagonal three
        while (row_temp + 1) < 8 and (col_temp - 1) > -1:
            if self.chessBoard[row_temp + 1][col_temp - 1] != None:
                break
            row_temp = row_temp + 1
            col_temp = col_temp - 1
            valid_moves.append((row_temp, col_temp))
        row_temp = current_row
        col_temp = current_col
        # diagonal four
        while (row_temp - 1) > -1 and (col_temp + 1) < 8:
            if self.chessBoard[row_temp - 1][col_temp + 1] != None:
                break
            row_temp = row_temp - 1
            col_temp = col_temp + 1
            valid_moves.append((row_temp, col_temp))

    def rook_valid_moves(self, valid_moves, piece):
        current_row = piece.position[0]
        current_col = piece.position[1]

        row_temp = current_row
        col_temp = current_col

        # forward

        while (row_temp + 1) < 8:
            if self.chessBoard[row_temp + 1][col_temp] != None:
                break
            row_temp = row_temp + 1
            valid_moves.append((row_temp, col_temp))

        row_temp = current_row
        col_temp = current_col

        # backwards
        while (row_temp - 1) > -1:
            if self.chessBoard[row_temp - 1][col_temp] != None:
                break
            row_temp = row_temp - 1
            valid_moves.append((row_temp, col_temp))

        row_temp = current_row
        col_temp = current_col

        # right
        while (col_temp + 1) < 8:
            if self.chessBoard[row_temp][col_temp + 1] != None:
                break
            col_temp = col_temp + 1
            valid_moves.append((row_temp, col_temp))

        row_temp = current_row
        col_temp = current_col

        # left
        while (col_temp - 1) > -1:
            if self.chessBoard[row_temp][col_temp - 1] != None:
                break
            col_temp = col_temp - 1
            valid_moves.append((row_temp, col_temp))

    def queen_valid_moves(self, valid_moves, piece):
        self.rook_valid_moves(valid_moves, piece)
        self.bishop_valid_moves(valid_moves, piece)



