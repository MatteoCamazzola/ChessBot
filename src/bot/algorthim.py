from random import choice
import math
best_piece = None
best_move = None
from src.pieces.queen import Queen
from src.pieces.pawn import Pawn
import re

def get_best_move(gameBoard, depth, colour_parameter):
    global best_piece, best_move
    maximizingPlayer = (colour_parameter == 'white')
    best_score = float('-inf') if maximizingPlayer else float('inf')

    # Call maxi or mini based on the maximizing player
    if maximizingPlayer:
        for move in get_all_moves(gameBoard, colour_parameter):
            row, col, new_row, new_col = move  # Unpack the move tuple
            has_moved_swapped,captured_pieces,original_piece=temp_move(gameBoard, move,gameBoard.last_move)
            eval_score = mini(gameBoard, depth - 1, False, colour_parameter,move)
            unmake_move(gameBoard, move,has_moved_swapped,captured_pieces,original_piece)  # Undo the move
            if eval_score > best_score:
                best_score = eval_score
                row, col, new_row, new_col= move
                best_move=(new_row,new_col)
                best_piece = gameBoard.chessBoard[row][col]  # Get the piece at the start position
    else:
        for move in get_all_moves(gameBoard, colour_parameter):
            row, col, new_row, new_col = move  # Unpack the move tuple
            has_moved_swapped, captured_pieces, original_piece = temp_move(gameBoard, move, gameBoard.last_move)
            eval_score = maxi(gameBoard, depth - 1, True, colour_parameter,move)
            unmake_move(gameBoard, move, has_moved_swapped, captured_pieces, original_piece)  # Undo the move
            if eval_score < best_score:
                best_score = eval_score
                row, col, new_row, new_col=move
                best_move = (new_row, new_col)
                best_piece = gameBoard.chessBoard[row][col]  # Get the piece at the start position

    return best_piece, best_move
def temp_move(temp_board, move,last_move):
    has_moved_swapped=False
    row, col, new_row, new_col = move
    original_piece=None
    captured_pieces = []
    if last_move is not None and len(last_move)==4:
        if temp_board.chessBoard[last_move[2]][last_move[3]] is None:
            last_move_temp=None
        else:
            last_move_temp=[last_move[0],last_move[1],temp_board.chessBoard[last_move[2]][last_move[3]].piece_type, temp_board.chessBoard[last_move[2]][last_move[3]].colour,last_move[2],last_move[3]]
    else:
        last_move_temp=last_move
    piece_to_move = temp_board.chessBoard[row][col]

    if piece_to_move:
        if temp_board.chessBoard[new_row][new_col] is not None and piece_to_move.colour==temp_board.chessBoard[new_row][new_col].colour:

            if abs(piece_to_move.position[1] - new_col) == 3:
                temp_board.chessBoard[new_row][3].has_moved = True
                temp_board.chessBoard[new_row][3].position = (new_row, 1)
                temp_board.chessBoard[new_row][0].has_moved = True
                temp_board.chessBoard[new_row][0].position = (new_row, 2)

                temp_board.chessBoard[new_row][1] = temp_board.chessBoard[new_row][3]
                temp_board.chessBoard[new_row][2] = temp_board.chessBoard[new_row][0]
                temp_board.chessBoard[new_row][3] = None
                temp_board.chessBoard[new_row][0] = None

                if piece_to_move.colour == "white":
                    temp_board.white_king_pos = (0, 1)
                else:
                    temp_board.black_king_pos = (7, 1)

            else:
                temp_board.chessBoard[new_row][3].has_moved = True
                temp_board.chessBoard[new_row][3].position = (new_row, 5)
                temp_board.chessBoard[new_row][7].has_moved = True
                temp_board.chessBoard[new_row][7].position = (new_row, 4)

                temp_board.chessBoard[new_row][5] = temp_board.chessBoard[new_row][3]
                temp_board.chessBoard[new_row][4] = temp_board.chessBoard[new_row][7]
                temp_board.chessBoard[new_row][3] = None
                temp_board.chessBoard[new_row][7] = None

                if piece_to_move.colour == "white":
                    temp_board.white_king_pos = (0, 5)
                else:
                    temp_board.black_king_pos = (7, 5)

        else:
            if temp_board.chessBoard[new_row][new_col] == None:
                if last_move_temp is not None:
                    init_row,init_col,last_piece_type,last_piece_colour,last_row,last_col=last_move_temp
                if piece_to_move.piece_type=="rook":
                    if piece_to_move.has_moved==False:
                        has_moved_swapped=True
                    piece_to_move.has_moved=True
                    temp_board.chessBoard[row][col] = None
                    temp_board.chessBoard[new_row][new_col] = piece_to_move
                    piece_to_move.position = new_row, new_col
                elif piece_to_move.piece_type == "king" and piece_to_move.colour == "white":
                    if piece_to_move.has_moved==False:
                        has_moved_swapped=True
                    piece_to_move.has_moved = True
                    temp_board.chessBoard[row][col] = None
                    temp_board.white_king_pos = (new_row, new_col)
                    temp_board.chessBoard[new_row][new_col] = piece_to_move
                    piece_to_move.position = new_row, new_col
                elif piece_to_move.piece_type == "king" and piece_to_move.colour == "black":
                    if piece_to_move.has_moved==False:
                        has_moved_swapped=True
                    piece_to_move.has_moved = True
                    temp_board.chessBoard[row][col] = None
                    temp_board.black_king_pos = (new_row, new_col)
                    temp_board.chessBoard[new_row][new_col] = piece_to_move
                    piece_to_move.position = new_row, new_col
                elif piece_to_move.piece_type == "pawn":
                    if piece_to_move.colour == "white" and row == 1 and new_row == 3:
                        last_move_temp = [new_row, new_col, piece_to_move.piece_type, piece_to_move.colour, row, col]
                        temp_board.chessBoard[row][col] = None
                        temp_board.chessBoard[new_row][new_col] = piece_to_move
                        piece_to_move.position = new_row, new_col
                    elif piece_to_move.colour == "black" and row == 6 and new_row == 4:
                        last_move_temp = [new_row, new_col, piece_to_move.piece_type, piece_to_move.colour, row, col]
                        temp_board.chessBoard[row][col] = None
                        temp_board.chessBoard[new_row][new_col] = piece_to_move
                        piece_to_move.position = new_row, new_col
                    elif (new_row == 0 or new_row == 7):
                        promoted_piece = Queen(piece_to_move.colour, new_row, new_col)
                        temp_board.chessBoard[row][col] = None
                        temp_board.chessBoard[new_row][new_col] = promoted_piece
                        original_piece= temp_board.chessBoard[row][col]
                    elif last_move_temp is not None and last_piece_type == "pawn" and piece_to_move.colour != last_piece_colour and abs(init_row - last_row) == 2 and abs(last_row - piece_to_move.position[0]) == 0 and abs(last_col - piece_to_move.position[1]) == 1 and new_col==last_col and abs(new_row-last_row)==1 :
                        if piece_to_move.colour == "white":
                            en_passant_row = piece_to_move.position[0] + 1
                            en_passant_col = last_col
                        else:
                            en_passant_row = piece_to_move.position[0] - 1
                            en_passant_col = last_col
                        temp_board.chessBoard[last_row][last_col] = None
                        temp_board.chessBoard[en_passant_row][en_passant_col] = piece_to_move
                        temp_board.chessBoard[row][col] = None
                        piece_to_move.position = en_passant_row,en_passant_col
                        last_temp_move = temp_board.last_move
                    else:
                        temp_board.chessBoard[new_row][new_col]=piece_to_move
                        piece_to_move.position=new_row,new_col
                        temp_board.chessBoard[row][col]
                else:
                    temp_board.chessBoard[new_row][new_col] = piece_to_move
                    piece_to_move.position = new_row, new_col
                    temp_board.chessBoard[row][col]

            if temp_board.chessBoard[new_row][new_col] != None:
                if piece_to_move.piece_type=="rook":
                    if piece_to_move.has_moved==False:
                        has_moved_swapped=True
                    piece_to_move.has_moved=True
                    captured_piece = temp_board.chessBoard[new_row][new_col]
                    if captured_piece.colour == "white":
                        captured_pieces.append(captured_piece)  # Append to white captures
                    elif captured_piece.colour == "black":
                        captured_pieces.append(captured_piece)
                    temp_board.chessBoard[new_row][new_col] = None
                    temp_board.chessBoard[new_row][new_col] = piece_to_move
                    temp_board.chessBoard[row][col] = None
                    piece_to_move.position = new_row, new_col
                elif piece_to_move.piece_type == "king" and piece_to_move.colour == "white":
                    if piece_to_move.has_moved==False:
                        has_moved_swapped=True
                    piece_to_move.has_moved = True
                    captured_piece = temp_board.chessBoard[new_row][new_col]
                    if captured_piece.colour == "white":
                        captured_pieces.append(captured_piece)  # Append to white captures
                    elif captured_piece.colour == "black":
                        captured_pieces.append(captured_piece)
                    temp_board.chessBoard[new_row][new_col] = None
                    temp_board.white_king_pos = (new_row, new_col)
                    temp_board.chessBoard[new_row][new_col] = piece_to_move
                    temp_board.chessBoard[row][col] = None
                    piece_to_move.position = new_row, new_col
                elif piece_to_move.piece_type == "king" and piece_to_move.colour == "black":
                    if piece_to_move.has_moved==False:
                        has_moved_swapped=True
                    piece_to_move.has_moved = True
                    captured_piece = temp_board.chessBoard[new_row][new_col]
                    if captured_piece.colour == "white":
                        captured_pieces.append(captured_piece)  # Append to white captures
                    elif captured_piece.colour == "black":
                        captured_pieces.append(captured_piece)
                    temp_board.chessBoard[new_row][new_col] = None
                    temp_board.black_king_pos = (new_row, new_col)
                    temp_board.chessBoard[new_row][new_col] = piece_to_move
                    temp_board.chessBoard[row][col] = None
                    piece_to_move.position = new_row, new_col
                elif piece_to_move.piece_type == "pawn" and (new_row == 0 or new_row == 7):
                    captured_piece = temp_board.chessBoard[new_row][new_col]
                    if captured_piece.colour == "white":
                        captured_pieces.append(captured_piece)  # Append to white captures
                    elif captured_piece.colour == "black":
                        captured_pieces.append(captured_piece)
                    temp_board.chessBoard[new_row][new_col] = None
                    promoted_piece = Queen(piece_to_move.colour, new_row, new_col)
                    original_piece = temp_board.chessBoard[row][col]
                    temp_board.chessBoard[new_row][new_col] = promoted_piece
                    temp_board.chessBoard[row][col] = None
                    original_piece=temp_board.chessBoard[row][col]
                else:
                    captured_piece = temp_board.chessBoard[new_row][new_col]
                    if captured_piece.colour == "white":
                        captured_pieces.append(captured_piece)  # Append to white captures
                    elif captured_piece.colour == "black":
                        captured_pieces.append(captured_piece)
                    temp_board.chessBoard[new_row][new_col] = None
                    temp_board.chessBoard[new_row][new_col] = piece_to_move
                    temp_board.chessBoard[row][col] = None
                    piece_to_move.position=new_row,new_col
    return has_moved_swapped,captured_pieces,original_piece
def unmake_move(temp_board, move, has_moved_swapped,captured_pieces,original_piece):
    start_row, start_col, end_row, end_col = move
    piece_moved = temp_board.chessBoard[end_row][end_col]
    if piece_moved is None:
        pass
   # ----------------------------------------------------------------------------------------------------------------------------
    if piece_moved==None:
        if start_col==0:
            piece_moved=temp_board.chessBoard[start_row][end_col-1]
        if end_col==0:
            piece_moved=temp_board.chessBoard[start_row][end_col+1]
        if end_col==7:
            piece_moved=temp_board.chessBoard[start_row][end_col-2]
        if start_col==7:
            piece_moved=temp_board.chessBoard[start_row][end_col+1]
        if piece_moved.piece_type == "king":
            if piece_moved.colour == "white" and abs(start_col-end_col)==4:#queenside
                temp_board.white_king_pos = (start_row, start_col)
                piece_moved.has_moved=False
                rook=temp_board.chessBoard[end_row][start_col+1]
                temp_board.chessBoard[end_row][end_col]=rook
                temp_board.chessBoard[end_row][start_col+1]=None
                rook.position=end_row,end_col
                rook.has_moved=False
                temp_board.chessBoard[start_row][start_col]=piece_moved
                temp_board.chessBoard[end_row][start_col+2]=None
                piece_moved.position=(start_row,start_col)


            elif piece_moved.colour == "black" and abs(start_col-end_col)==4:
                temp_board.black_king_pos = (start_row, start_col)
                piece_moved.has_moved = False
                rook = temp_board.chessBoard[end_row][start_col+1]
                temp_board.chessBoard[end_row][end_col] = rook
                temp_board.chessBoard[end_row][start_col+1] = None
                rook.position = end_row, end_col
                rook.has_moved = False
                temp_board.chessBoard[start_row][start_col] = piece_moved
                temp_board.chessBoard[end_row][start_col + 2] = None
                piece_moved.position = (start_row,start_col)

            elif piece_moved.colour == "white" and abs(start_col-end_col)==3:#kingside
                temp_board.white_king_pos = (start_row, start_col)
                piece_moved.has_moved = False
                rook = temp_board.chessBoard[end_row][start_col-1]
                temp_board.chessBoard[end_row][end_col] = rook
                temp_board.chessBoard[end_row][start_col-1] = None
                rook.position = end_row, end_col
                rook.has_moved = False
                temp_board.chessBoard[start_row][start_col] = piece_moved
                temp_board.chessBoard[end_row][start_col-2] = None
                piece_moved.position = (start_row,start_col)
            elif piece_moved.colour == "black" and abs(start_col-end_col)==3:
                temp_board.black_king_pos = (start_row, start_col)
                piece_moved.has_moved = False
                rook = temp_board.chessBoard[end_row][start_col-1]
                temp_board.chessBoard[end_row][end_col] = rook
                temp_board.chessBoard[end_row][start_col-1] = None
                rook.position = end_row, end_col
                rook.has_moved = False
                temp_board.chessBoard[start_row][start_col] = piece_moved
                temp_board.chessBoard[end_row][start_col-2] = None
                piece_moved.position = (start_row,start_col)

        if piece_moved.piece_type=="rook":
            if start_col==0 and end_col==3 and temp_board.chessBoard[end_row][start_col+1] is not None and piece_moved.colour=="white":
                king=temp_board.chessBoard[end_row][start_col+1]
                temp_board.chessBoard[end_row][end_col]=king
                temp_board.chessBoard[end_row][start_col+1]=None
                king.position=end_row,end_col
                temp_board.white_king_pos=(end_row,end_col)
                piece_moved.has_moved = False
                king.has_moved = False
                temp_board.chessBoard[start_row][start_col]=piece_moved
                temp_board.chessBoard[start_row][end_col-1]=None
                piece_moved.position=start_row,start_col
            elif start_col==0 and end_col==3 and temp_board.chessBoard[end_row][start_col+1] is not None and piece_moved.colour=="black":
                king=temp_board.chessBoard[end_row][start_col+1]
                temp_board.chessBoard[end_row][end_col]=king
                temp_board.chessBoard[end_row][start_col+1]=None
                king.position=end_row,end_col
                temp_board.black_king_pos=(end_row,end_col)
                piece_moved.has_moved = False
                king.has_moved = False
                temp_board.chessBoard[start_row][start_col] = piece_moved
                temp_board.chessBoard[start_row][end_col - 1] = None
                piece_moved.position = start_row, start_col
            elif start_col==7 and end_col==3 and temp_board.chessBoard[end_row][start_col-2] and piece_moved.colour=="white":
                king=temp_board.chessBoard[end_row][start_col-2]
                temp_board.chessBoard[end_row][end_col]=king
                temp_board.chessBoard[end_row][start_col-2]=None
                king.position=end_row,end_col
                temp_board.white_king_pos=(end_row,end_col)
                piece_moved.has_moved = False
                king.has_moved = False
                temp_board.chessBoard[start_row][start_col] = piece_moved
                temp_board.chessBoard[start_row][end_col + 1] = None
                piece_moved.position = start_row, start_col
            elif start_col == 7 and end_col == 3 and temp_board.chessBoard[end_row][start_col-2] and piece_moved.colour=="black":
                king = temp_board.chessBoard[end_row][start_col - 2]
                temp_board.chessBoard[end_row][end_col] = king
                temp_board.chessBoard[end_row][start_col - 2] = None
                king.position = end_row, end_col
                temp_board.black_king_pos = (end_row, end_col)
                piece_moved.has_moved = False
                king.has_moved = False
                temp_board.chessBoard[start_row][start_col] = piece_moved
                temp_board.chessBoard[start_row][end_col + 1] = None
                piece_moved.position = start_row, start_col
# ----------------------------------------------------------------------------------------------------------------------
    else:
        if has_moved_swapped == True:
            piece_moved.has_moved = False
        if piece_moved.colour == "white" and piece_moved.piece_type=="king":
            temp_board.white_king_pos = (start_row, start_col)
        elif piece_moved.colour == "black" and piece_moved.piece_type=="king":
            temp_board.black_king_pos = (start_row, start_col)
        elif original_piece is not None:
            temp_board.chessBoard[end_row][end_col] = Pawn(piece_moved.colour,end_row,end_col)
            piece_moved=temp_board.chessBoard[end_row][end_col]
        temp_board.chessBoard[start_row][start_col] = piece_moved
        temp_board.chessBoard[end_row][end_col]=None
        piece_moved.position=start_row,start_col
        temp_board.chessBoard[captured_pieces[0].position[0]][captured_pieces[0].position[1]]=captured_pieces[0]

def random_moves(gameBoard, hi, colour_parameter, theory_list):
    if gameBoard.number_of_moves_made < 20:
        opening_string = find_matching_opening(gameBoard.previous_moves, theory_list)
        if opening_string is not None:
            pgn_move = extract_substring(colour_parameter, opening_string)
            move = translate_from_pgn(pgn_move, gameBoard)
            return move
    colour = colour_parameter
    pieces = []
    for x in range(8):
        for y in range(8):
            piece = gameBoard.chessBoard[x][y]
            if piece is not None and piece.colour == colour:
                pieces.append(piece)

    if pieces:
        random_piece = choice(pieces)
        random_piece_moves = gameBoard.valid_moves(random_piece.position)
        if random_piece_moves:
            random_move = choice(random_piece_moves)
            return random_piece, random_move
        while not random_piece_moves:
            random_piece = choice(pieces)
            random_piece_moves = gameBoard.valid_moves(random_piece.position)
            if random_piece_moves:
                random_move = choice(random_piece_moves)
                return random_piece, random_move
            elif gameBoard.checkmate(colour) or gameBoard.stalemate(colour):
                return None
    else:
        return None


def piece_values(gameBoard):
    white_values = 0
    black_values = 0

    piece_values = {
        "pawn": 1,
        "knight": 3,
        "bishop": 3,
        "rook": 5,
        "queen": 9
    }

    for x in range(8):
        for y in range(8):
            piece = gameBoard.chessBoard[x][y]
            if piece is not None and piece.piece_type != "king":
                value = piece_values.get(piece.piece_type, 0)
                if piece.colour == "white":
                    white_values += value
                elif piece.colour == "black":
                    black_values += value

    piece_value_eval = white_values - black_values
    return piece_value_eval


def maxi(gameBoard, depth, maximizingPlayer, colour_parameter,last_move):
    if depth == 0:
        return eval(gameBoard)
    max_score = float('-inf')
    for move in get_all_moves(gameBoard, 'white'):  # Assuming 'white' is the maximizing player
        has_moved_swapped,captured_pieces,original_piece=temp_move(gameBoard, move,last_move)  # Make the temporary move
        score = mini(gameBoard, depth - 1, False, colour_parameter,move)
        max_score = max(max_score, score)
        unmake_move(gameBoard, move,has_moved_swapped,captured_pieces,original_piece)  # Unmake the temporary move
    return max_score


def mini(gameBoard, depth, maximizingPlayer, colour_parameter,last_move):
    if depth == 0:
        return -eval(gameBoard)
    min_score = float('inf')
    for move in get_all_moves(gameBoard, 'black'):# Assuming 'black' is the minimizing player
        has_moved_swapped,captured_pieces,original_piece=temp_move(gameBoard, move,last_move)  # Make the temporary move
        score = maxi(gameBoard, depth - 1, True, colour_parameter,move)
        min_score = min(min_score, score)
        unmake_move(gameBoard, move,has_moved_swapped,captured_pieces,original_piece)  # Unmake the temporary move
    return min_score


def get_all_moves(gameBoard, colour_parameter):
    colour = colour_parameter
    moves = []
    pieces = gameBoard.get_all_pieces(colour)

    for piece in pieces:
        piece_moves = gameBoard.valid_moves(piece.position)
        current_row, current_col = piece.position  # Extract current row and column
        moves.extend(
            [(current_row, current_col, move[0], move[1]) for move in piece_moves])  # Include current row and column
    return moves


def eval(gameBoard):
    material_score = piece_values(gameBoard)
    combined_score = material_score
    return combined_score


def find_matching_opening(current_moves, theory_list):
    for opening in theory_list:
        if opening.startswith(current_moves):
            # Calculate the starting index of the different part
            # Adding 1 to account for the space after the current_moves substring
            start_index = len(current_moves) + 1 if len(current_moves) < len(opening) else len(opening)
            # Return the substring from the opening string that is different
            return opening[start_index:]
    return None  # Return None if no match is found


def extract_substring(colour_parameter, input_string):
    if colour_parameter == "white":
        match = re.search(r'\d+\S* (\S+)', input_string)
    else:
        match = re.search(r'(\S+)', input_string)

    if match:
        # Extract the matched group if a match is found
        return match.group(1)
    else:
        return None

def translate_from_pgn(pgn_string, gameBoard):
    # Mapping of PGN piece symbols to piece_type strings used in your program
    piece_symbols = {'N': 'Knight', 'B': 'Bishop', 'R': 'Rook', 'Q': 'Queen', 'K': 'King'}

    # Default piece type for pawns if no piece symbol is provided
    piece_type = 'Pawn'

    # If the first character is a piece symbol, set the piece_type accordingly
    if pgn_string[0] in piece_symbols:
        piece_type = piece_symbols[pgn_string[0]]
        pgn_string = pgn_string[1:]  # Remove the piece symbol from the string

    # Extract the target square from the PGN string
    # Assuming the format is like "e4" or "exd4" for captures
    target_square = pgn_string[-2:]

    # Convert target square to row and column
    files = 'abcdefgh'
    ranks = '87654321'
    col_to_move = files.index(target_square[0])
    row_to_move = ranks.index(target_square[1])

    # Loop through the board to find a piece of the specified type that can move to the target square
    for row in range(8):
        for col in range(8):
            piece = gameBoard.chessBoard[row][col]
            if piece and piece.piece_type == piece_type and piece.colour == colour_parameter:  # Check piece type and color
                # Check if the move is valid for this piece
                if gameBoard.is_valid_move((row_to_move, col_to_move), gameBoard.valid_moves((row, col))):
                    return piece, (row_to_move, col_to_move)

    return None, None  # If no valid piece and move are found
