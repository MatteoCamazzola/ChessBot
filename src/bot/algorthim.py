from random import choice
import math
best_piece = None
best_move = None
from src.pieces.queen import Queen

def get_best_move(gameBoard, depth, colour_parameter):
    global best_piece, best_move
    maximizingPlayer = (colour_parameter == 'white')
    best_score = float('-inf') if maximizingPlayer else float('inf')

    # Call maxi or mini based on the maximizing player
    if maximizingPlayer:
        for move in get_all_moves(gameBoard, colour_parameter):
            row, col, new_row, new_col = move  # Unpack the move tuple
            temp_move(gameBoard, move)
            eval_score = mini(gameBoard, depth - 1, False, colour_parameter)
            unmake_move(gameBoard,move)  # Undo the move
            if eval_score > best_score:
                best_score = eval_score
                row, col, new_row, new_col= move
                best_move=(new_row,new_col)
                best_piece = gameBoard.chessBoard[row][col]  # Get the piece at the start position
    else:
        for move in get_all_moves(gameBoard, colour_parameter):
            row, col, new_row, new_col = move  # Unpack the move tuple
            temp_move(gameBoard, move)
            eval_score = maxi(gameBoard, depth - 1, True, colour_parameter)
            unmake_move(gameBoard,move)  # Undo the move
            if eval_score < best_score:
                best_score = eval_score
                row, col, new_row, new_col=move
                best_move = (new_row, new_col)
                best_piece = gameBoard.chessBoard[row][col]  # Get the piece at the start position

    return best_piece, best_move
def temp_move(temp_board, move):
    row, col, new_row, new_col = move
    piece_to_move = temp_board.chessBoard[row][col]

    if piece_to_move:  # Check if there's a piece at the given position
        # Check for pawn promotion
        if piece_to_move.piece_type == "pawn" and (new_row == 0 or new_row == 7):
            # Promote the pawn to a queen
            promoted_piece = Queen(piece_to_move.colour, new_row, new_col)
            temp_board.chessBoard[new_row][new_col] = promoted_piece
            return  # Exit the function without calling make_move
        list_of_moves_for_piece_to_move = temp_board.valid_moves(piece_to_move.position)
        if list_of_moves_for_piece_to_move:  # Check if valid_moves returned moves
            # Make the move and check if a capture occurred
            captured_piece = temp_board.make_move(new_row, new_col, list_of_moves_for_piece_to_move, piece_to_move)
            if captured_piece:
                temp_board.captured_pieces[int(captured_piece.colour == "black")].append(captured_piece)


def unmake_move(self, move):
    start_row, start_col, end_row, end_col = move
    piece_moved = self.chessBoard[end_row][end_col]

    if piece_moved is None:
        pass
    elif piece_moved.piece_type == "king":
        # Check if the moved piece is a king
        if piece_moved.colour == "white":
            self.white_king_pos = (start_row, start_col)
        elif piece_moved.colour == "black":
            self.black_king_pos = (start_row, start_col)

    piece_moved.position = (start_row, start_col)

    # Update the board representation
    self.chessBoard[start_row][start_col] = piece_moved
    self.chessBoard[end_row][end_col] = None

    # Restore captured pieces to the board
    for colour_pieces in self.captured_pieces:
        for captured_piece in colour_pieces:
            if captured_piece:
                self.chessBoard[captured_piece.position[0]][captured_piece.position[1]] = captured_piece


def random_moves(gameBoard, hi, colour_parameter):
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


def maxi(gameBoard, depth, maximizingPlayer, colour_parameter):
    if depth == 0:
        return eval(gameBoard)
    max_score = float('-inf')
    for move in get_all_moves(gameBoard, 'white'):  # Assuming 'white' is the maximizing player
        temp_move(gameBoard, move)  # Make the temporary move
        score = mini(gameBoard, depth - 1, False, colour_parameter)
        max_score = max(max_score, score)
        unmake_move(gameBoard, move)  # Unmake the temporary move
    return max_score


def mini(gameBoard, depth, maximizingPlayer, colour_parameter):
    if depth == 0:
        return -eval(gameBoard)
    min_score = float('inf')
    for move in get_all_moves(gameBoard, 'black'):# Assuming 'black' is the minimizing player
        temp_move(gameBoard, move)  # Make the temporary move
        score = maxi(gameBoard, depth - 1, True, colour_parameter)
        min_score = min(min_score, score)
        unmake_move(gameBoard, move)  # Unmake the temporary move
    return min_score


def get_all_moves(gameBoard, colour_parameter):
    colour = colour_parameter
    moves = []
    pieces = gameBoard.get_all_pieces(colour)

    for piece in pieces:
        piece_moves = gameBoard.valid_moves(piece.position)
        current_row, current_col = piece.position  # Extract current row and column
        moves.extend([(current_row, current_col, move[0], move[1]) for move in piece_moves])  # Include current row and column
    return moves


def eval(gameBoard):
    material_score = piece_values(gameBoard)
    combined_score = material_score
    return combined_score
