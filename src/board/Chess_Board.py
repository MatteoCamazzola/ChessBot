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
        pawn_black_4 = Pawn("black", 5, 0)
        pawn_black_5 = Pawn("black", 5, 1)
        pawn_black_6 = Pawn("black", 6, 5)
        pawn_black_7 = Pawn("black", 6, 6)
        pawn_black_8 = Pawn("black", 4, 7)

        rook_black_1 = Rook("black", 7, 0)
        rook_black_2 = Rook("black", 7, 7)
        knight_black_1 = Knight("black", 7, 1)
        knight_black_2 = Knight("black", 3, 3)
        bishop_black_1 = Bishop("black", 7, 2)
        bishop_black_2 = Bishop("black", 6, 4)
        queen_black = Queen("black", 4, 3)
        king_black = King("black", 7, 3)

        pawn_white_1 = Pawn("white", 1, 0)
        pawn_white_2 = Pawn("white", 1, 1)
        pawn_white_3 = Pawn("white", 1, 2)
        pawn_white_4 = Pawn("white", 2, 0)
        pawn_white_5 = Pawn("white", 2, 1)
        pawn_white_6 = Pawn("white", 1, 5)
        pawn_white_7 = Pawn("white", 4, 6)
        pawn_white_8 = Pawn("white", 1, 7)

        rook_white_1 = Rook("white", 0, 0)
        rook_white_2 = Rook("white", 0, 7)
        knight_white_1 = Knight("white", 0, 1)
        knight_white_2 = Knight("white", 0, 6)
        bishop_white_1 = Bishop("white", 0, 5)
        bishop_white_2 = Bishop("white", 0, 2)
        queen_white = Queen("white", 1, 3)
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

        self.white_king_pos = (0, 3)
        self.black_king_pos = (7, 3)
        self.captured_pieces = [["white"], ["black"]]
        self.last_move = [4,7,"pawn","black"]

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

    def valid_moves(self, current_position):
        list_of_moves = []
        piece = self.chessBoard[current_position[0]][current_position[1]]
        if piece.piece_type == "knight" or piece.piece_type == "king" or piece.piece_type == "pawn":
            list_of_moves = piece.valid_move()
        else:
            self.blocking_pieces(list_of_moves, piece)
        self.landing_on_own_piece(list_of_moves, piece)

        if piece.piece_type == "rook" or piece.piece_type == "king":
            self.add_castling(piece, list_of_moves)

        if piece.piece_type == "pawn":
            self.pawn_diagonal(piece, list_of_moves)
        self.en_passant(piece,list_of_moves,self.last_move)

        # check for moving into check
        moves_to_remove = []
        for move in list_of_moves:
            self.chessBoard[current_position[0]][current_position[1]] = None
            temp = self.chessBoard[move[0]][move[1]]
            self.chessBoard[move[0]][move[1]] = piece
            if self.is_check(piece.colour):
                moves_to_remove.append(move)
            self.chessBoard[current_position[0]][current_position[1]] = piece
            self.chessBoard[move[0]][move[1]] = temp

        for move in moves_to_remove:
            list_of_moves.remove(move)

        return list_of_moves

    def landing_on_own_piece(self, list_of_moves, piece):
        moves_to_remove = []  # Create a list to store moves to be removed
        for move in list_of_moves[:]:  # Iterate over a copy of the list
            x, y = move
            other_piece = self.chessBoard[x][y]

            if other_piece is not None and piece.colour == other_piece.colour and piece.piece_type != "pawn":
                moves_to_remove.append(move)

            elif other_piece is not None and piece.piece_type == "pawn" and abs(
                    piece.position[0] - other_piece.position[0]) == 1:
                moves_to_remove.clear()
                pass

            elif other_piece is not None and piece.piece_type == "pawn":
                moves_to_remove.append(move)

        # Remove moves from the original list
        for move in moves_to_remove:
            list_of_moves.remove(move)

    def pawn_diagonal(self, piece, list_of_moves):
        row, col = piece.position[0], piece.position[1]
        if piece.colour == "white":
            other_piece_white_bigger = (row + 1, col + 1)
            other_piece_white_smaller = (row + 1, col - 1)
            if 0 <= other_piece_white_bigger[0] < 8 and 0 <= other_piece_white_bigger[1] < 8:
                if self.chessBoard[other_piece_white_bigger[0]][other_piece_white_bigger[1]] is not None \
                        and self.chessBoard[other_piece_white_bigger[0]][
                    other_piece_white_bigger[1]].colour != piece.colour:
                    list_of_moves.append(other_piece_white_bigger)
            if 0 <= other_piece_white_smaller[0] < 8 and 0 <= other_piece_white_smaller[1] < 8:
                if self.chessBoard[other_piece_white_smaller[0]][other_piece_white_smaller[1]] is not None \
                        and self.chessBoard[other_piece_white_smaller[0]][
                    other_piece_white_smaller[1]].colour != piece.colour:
                    list_of_moves.append(other_piece_white_smaller)
        if piece.colour == "black":
            other_piece_black_bigger = (row - 1, col + 1)
            other_piece_black_smaller = (row - 1, col - 1)
            if 0 <= other_piece_black_bigger[0] < 8 and 0 <= other_piece_black_bigger[1] < 8:
                if self.chessBoard[other_piece_black_bigger[0]][other_piece_black_bigger[1]] is not None \
                        and self.chessBoard[other_piece_black_bigger[0]][
                    other_piece_black_bigger[1]].colour != piece.colour:
                    list_of_moves.append(other_piece_black_bigger)
            if 0 <= other_piece_black_smaller[0] < 8 and 0 <= other_piece_black_smaller[1] < 8:
                if self.chessBoard[other_piece_black_smaller[0]][other_piece_black_smaller[1]] is not None \
                        and self.chessBoard[other_piece_black_smaller[0]][
                    other_piece_black_smaller[1]].colour != piece.colour:
                    list_of_moves.append(other_piece_black_smaller)

    def blocking_pieces(self, list_of_moves, piece):
        if piece.piece_type == "bishop":
            self.bishop_valid_moves(list_of_moves, piece)
        elif piece.piece_type == "rook":
            self.rook_valid_moves(list_of_moves, piece)
        elif piece.piece_type == "queen":
            self.queen_valid_moves(list_of_moves, piece)

    def check_move_filter(self):
        pass

    def white_king_location(self):
        return self.white_king_pos

    def track_white_king(self, new_row, new_col):
        self.white_king_pos = (new_row, new_col)

    def black_king_location(self):
        return self.black_king_pos

    def track_black_king(self, new_row, new_col):
        self.black_king_pos = (new_row, new_col)

    # input black or white        #output true for check false for not in check
    def is_check(self, colour):
        for x in range(8):
            for y in range(8):
                piece = self.chessBoard[x][y]
                if piece is None:
                    continue
                elif piece.piece_type == "king" and piece.colour != colour:
                    continue
                elif piece.colour != colour and piece.colour == "black":
                    if self.white_king_pos in self.list_of_moves_for_check(piece):
                        return True
                elif piece.colour != colour and piece.colour == "white":
                    if self.black_king_pos in self.list_of_moves_for_check(piece):
                        return True
        return False

    def is_valid_move(self, row, col, valid_moves):
        if (row, col) in valid_moves:
            return True

    def bishop_valid_moves(self, valid_moves, piece):
        current_row = piece.position[0]
        current_col = piece.position[1]

        row_temp = current_row
        col_temp = current_col

        # diagonal one
        while (row_temp + 1) < 8 and (col_temp + 1) < 8:
            if self.chessBoard[row_temp + 1][col_temp + 1] != None:
                if self.chessBoard[row_temp + 1][col_temp + 1].colour == piece.colour:
                    break
                else:
                    valid_moves.append((row_temp + 1, col_temp + 1))
                    break
            row_temp = row_temp + 1
            col_temp = col_temp + 1
            valid_moves.append((row_temp, col_temp))
        # diagonal two
        row_temp = current_row
        col_temp = current_col
        while (row_temp - 1) > -1 and (col_temp - 1) > -1:
            if self.chessBoard[row_temp - 1][col_temp - 1] != None:
                if self.chessBoard[row_temp - 1][col_temp - 1].colour == piece.colour:
                    break
                else:
                    valid_moves.append((row_temp - 1, col_temp - 1))
                    break
            row_temp = row_temp - 1
            col_temp = col_temp - 1
            valid_moves.append((row_temp, col_temp))
        row_temp = current_row
        col_temp = current_col
        # diagonal three
        while (row_temp + 1) < 8 and (col_temp - 1) > -1:
            if self.chessBoard[row_temp + 1][col_temp - 1] != None:
                if self.chessBoard[row_temp + 1][col_temp - 1].colour == piece.colour:
                    break
                else:
                    valid_moves.append((row_temp + 1, col_temp - 1))
                    break
            row_temp = row_temp + 1
            col_temp = col_temp - 1
            valid_moves.append((row_temp, col_temp))
        row_temp = current_row
        col_temp = current_col
        # diagonal four
        while (row_temp - 1) > -1 and (col_temp + 1) < 8:
            if self.chessBoard[row_temp - 1][col_temp + 1] != None:
                if self.chessBoard[row_temp - 1][col_temp + 1].colour == piece.colour:
                    break
                else:
                    valid_moves.append((row_temp - 1, col_temp + 1))
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
                if self.chessBoard[row_temp + 1][col_temp].colour == piece.colour:
                    break
                else:
                    valid_moves.append((row_temp + 1, col_temp))
                    break
            row_temp = row_temp + 1
            valid_moves.append((row_temp, col_temp))

        row_temp = current_row
        col_temp = current_col

        # backwards
        while (row_temp - 1) > -1:
            if self.chessBoard[row_temp - 1][col_temp] != None:
                if self.chessBoard[row_temp - 1][col_temp].colour == piece.colour:
                    break
                else:
                    valid_moves.append((row_temp - 1, col_temp))
                    break
            row_temp = row_temp - 1
            valid_moves.append((row_temp, col_temp))

        row_temp = current_row
        col_temp = current_col

        # right
        while (col_temp + 1) < 8:
            if self.chessBoard[row_temp][col_temp + 1] != None:
                if self.chessBoard[row_temp][col_temp + 1].colour == piece.colour:
                    break
                else:
                    valid_moves.append((row_temp, col_temp + 1))
                    break
            col_temp = col_temp + 1
            valid_moves.append((row_temp, col_temp))

        row_temp = current_row
        col_temp = current_col

        # left
        while (col_temp - 1) > -1:
            if self.chessBoard[row_temp][col_temp - 1] != None:
                if self.chessBoard[row_temp][col_temp - 1].colour == piece.colour:
                    break
                else:
                    valid_moves.append((row_temp, col_temp - 1))
                    break
            col_temp = col_temp - 1
            valid_moves.append((row_temp, col_temp))

    def queen_valid_moves(self, valid_moves, piece):
        self.rook_valid_moves(valid_moves, piece)
        self.bishop_valid_moves(valid_moves, piece)

    def possible_captures(self, list_of_moves, piece,last_move):
        possible_captures = []
        for move in list_of_moves:
            x, y = move
            other_piece = self.chessBoard[x][y]
            if other_piece is not None and piece.colour != other_piece.colour and piece.piece_type != "pawn":
                capture_row = other_piece.position[0]
                capture_col = other_piece.position[1]
                possible_captures.append((capture_row, capture_col))
            elif piece.piece_type == "pawn" and other_piece is not None and piece.colour != other_piece.colour:
                if abs(x - piece.position[0]) == 1 and abs(y - piece.position[1]) == 1:
                    capture_row = other_piece.position[0]
                    capture_col = other_piece.position[1]
                    possible_captures.append((capture_row, capture_col))
            self.last_move = last_move
        self.en_passant(piece,possible_captures,self.last_move)
        return possible_captures

    def capture_handler(self, capturee):
        # remove capturee from the chess board
        self.chessBoard[capturee.position[0]][capturee.position[1]] = None
        # place the capturee in the captured pieces list
        if capturee.colour == "white":
            self.captured_pieces[0].append(capturee)
        else:
            self.captured_pieces[1].append(capturee)

    # assuming that the move is valid
    # remember to update the king position in member variable
    def make_move(self, row, col, list_of_moves, piece_to_move):
        # handle castling
        if self.chessBoard[row][col] != None:
            if self.chessBoard[row][col].colour == piece_to_move.colour:
                self.castle_handler(row, col, piece_to_move)
                self.last_move = [None, None,None,None]

        else:
            if piece_to_move.piece_type == "king":
                if piece_to_move.colour == "white":
                    self.track_white_king(row, col)
                else:
                    self.track_black_king(row, col)
            if piece_to_move.piece_type == "king" or piece_to_move.piece_type == "rook":
                piece_to_move.has_moved = True
            possible_captures = self.possible_captures(list_of_moves, piece_to_move)
            if (row, col) in possible_captures:
                if self.chessBoard[row][col] == None:
                   if piece_to_move.colour == "white":
                    self.capture_handler(self.chessBoard[row -1][col])
                   else:
                       self.capture_handler(self.chessBoard[row + 1][col])
                self.capture_handler(self.chessBoard[row][col])
            piece_to_move.position = (row, col)
            self.chessBoard[row][col] = piece_to_move
            self.last_move = [row, col, piece_to_move.piece_type,piece_to_move.colour]

    def add_castling(self, piece, list_of_moves):
        colour = piece.colour
        if colour == "white":
            if piece.piece_type == "rook":
                if self.did_not_move(piece, self.chessBoard[self.white_king_pos[0]][self.white_king_pos[1]]):
                    if self.piece_in_between(piece):
                        if not self.is_check(colour):
                            if self.king_through_check(piece,
                                                       self.chessBoard[self.white_king_pos[0]][self.white_king_pos[1]]
                                                       ):
                                list_of_moves.append((0, 3))
            else:
                if not piece.has_moved:
                    if self.chessBoard[0][0] != None:
                        if self.chessBoard[0][0].piece_type == "rook":
                            if not self.chessBoard[0][0].has_moved:
                                if self.piece_in_between(self.chessBoard[0][0]):
                                    if not self.is_check(colour):
                                        if self.king_through_check(self.chessBoard[0][0], piece):
                                            list_of_moves.append((0, 0))
                    if self.chessBoard[0][7] != None:
                        if self.chessBoard[0][7].piece_type == "rook":
                            if not self.chessBoard[0][7].has_moved:
                                if self.piece_in_between(self.chessBoard[0][7]):
                                    if not self.is_check(colour):
                                        if self.king_through_check(self.chessBoard[0][7], piece):
                                            list_of_moves.append((0, 7))


        else:
            if piece.piece_type == "rook":
                if self.did_not_move(piece, self.chessBoard[self.black_king_pos[0]][self.black_king_pos[1]]):
                    if self.piece_in_between(piece):
                        if not self.is_check(colour):
                            if self.king_through_check(piece,
                                                       self.chessBoard[self.black_king_pos[0]][self.black_king_pos[1]]
                                                      ):
                                list_of_moves.append((7, 3))
            else:
                if not piece.has_moved:
                    if self.chessBoard[7][0] != None:
                        if self.chessBoard[7][0].piece_type == "rook":
                            if not self.chessBoard[7][0].has_moved:
                                if self.piece_in_between(self.chessBoard[7][0]):
                                    if not self.is_check(colour):
                                        if self.king_through_check(self.chessBoard[7][0], piece):
                                            list_of_moves.append((7, 0))
                    if self.chessBoard[7][7] != None:
                        if self.chessBoard[7][7].piece_type == "rook":
                            if not self.chessBoard[7][7].has_moved:
                                if self.piece_in_between(self.chessBoard[7][7]):
                                    if not self.is_check(colour):
                                        if self.king_through_check(self.chessBoard[7][7], piece):
                                            list_of_moves.append((7, 7))

    def did_not_move(self, piece_one, piece_two):
        if (not piece_one.has_moved) and (not piece_two.has_moved):
            return True
        else:
            return False

    def piece_in_between(self, piece_one):
        if piece_one.position[1] > 5:
            if self.chessBoard[piece_one.position[0]][5] == None and self.chessBoard[piece_one.position[0]][
                6] == None and self.chessBoard[piece_one.position[0]][4] == None:
                return True
            else:
                return False
        else:
            if self.chessBoard[piece_one.position[0]][1] == None and self.chessBoard[piece_one.position[0]][
                2] == None:
                return True
            else:
                return False
            pass

    def king_through_check(self, piece_one, piece_two):
        colour = piece_two.colour

        if colour == "white":
            if piece_one.position[1] > 5:
                self.track_white_king(piece_two.position[0], 4)
                if self.is_check(piece_two.colour):
                    self.track_white_king(piece_two.position[0], 3)
                    return False
                self.track_white_king(piece_two.position[0], 5)
                if self.is_check(piece_two.colour):
                    self.track_white_king(piece_two.position[0], 3)
                    return False
            else:
                self.track_white_king(piece_two.position[0], 1)
                if self.is_check(piece_two.colour):
                    self.track_white_king(piece_two.position[0], 3)
                    return False
                self.track_white_king(piece_two.position[0], 2)
                if self.is_check(piece_two.colour):
                    self.track_white_king(piece_two.position[0], 3)
                    return False
        else:
            if piece_one.position[1] > 5:
                self.track_black_king(piece_two.position[0], 4)
                if self.is_check(piece_two.colour):
                    self.track_black_king(piece_two.position[0], 3)
                    return False
                self.track_black_king(piece_two.position[0], 5)
                if self.is_check(piece_two.colour):
                    self.track_black_king(piece_two.position[0], 3)
                    return False
            else:
                self.track_black_king(piece_two.position[0], 1)
                if self.is_check(piece_two.colour):
                    self.track_black_king(piece_two.position[0], 3)
                    return False
                self.track_black_king(piece_two.position[0], 2)
                if self.is_check(piece_two.colour):
                    self.track_black_king(piece_two.position[0], 3)
                    return False
        return True

    #for en_passant need a last move i can store the last move made in list from the move fucntion getting executed then can
    #check the list to see last move made see if its all good then i can clear the list and add the last move into the list again
    def en_passant(self, piece, list_of_moves, last_move):
        self.last_move = last_move
        if last_move == [None, None, None, None]:
            return
        last_row, last_col, last_piece_type, last_piece_colour = last_move
        if piece.piece_type == "pawn" and last_piece_type == "pawn" and piece.colour != last_piece_colour:
            if abs(last_row - piece.position[0]) == 0 and abs(last_col - piece.position[1]) == 1:
                if piece.colour == "white":
                    en_passant_row = piece.position[0] + 1
                    en_passant_col = last_col  # The column where the opponent's pawn moved
                else:
                    en_passant_row = piece.position[0] - 1
                    en_passant_col = last_col  # The column where the opponent's pawn moved
                # Add the en passant move to the list of valid moves
                list_of_moves.append((en_passant_row, en_passant_col))

    def list_of_moves_for_check(self, piece):
        list_of_moves = []
        if piece.piece_type == "knight" or piece.piece_type == "king" or piece.piece_type == "pawn":
            list_of_moves = piece.valid_move()
        else:
            self.blocking_pieces(list_of_moves, piece)
        self.landing_on_own_piece(list_of_moves, piece)

        if piece.piece_type=="pawn":
            self.pawn_diagonal(piece,list_of_moves)
        self.en_passant(piece,list_of_moves,self.last_move)
        return list_of_moves

    def castle_handler(self, row, col, piece):
        if abs(piece.position[1] - col) == 3:
            self.chessBoard[row][3].has_moved = True
            self.chessBoard[row][3].position = (row, 1)
            self.chessBoard[row][0].has_moved = True
            self.chessBoard[row][0].position = (row, 2)

            self.chessBoard[row][1] = self.chessBoard[row][3]
            self.chessBoard[row][2] = self.chessBoard[row][0]
            self.chessBoard[row][3] = None
            self.chessBoard[row][0] = None

            if piece.colour == "white":
                self.white_king_pos = (0, 1)
            else:
                self.black_king_pos = (7, 1)

        else:
            self.chessBoard[row][3].has_moved = True
            self.chessBoard[row][3].position = (row, 5)
            self.chessBoard[row][7].has_moved = True
            self.chessBoard[row][7].position = (row, 4)

            self.chessBoard[row][5] = self.chessBoard[row][3]
            self.chessBoard[row][4] = self.chessBoard[row][7]
            self.chessBoard[row][3] = None
            self.chessBoard[row][7] = None

            if piece.colour == "white":
                self.white_king_pos = (0, 5)
            else:
                self.black_king_pos = (7, 5)
