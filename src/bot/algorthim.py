from src.board.Chess_Board import Board
from random import choice
from copy import deepcopy


def get_best_move(gameBoard, depth, colour_parameter):
    best_piece = None
    best_move = None
    best_score = float('-inf') if gameBoard.current_player == 'white' else float('inf')

    for piece in gameBoard.get_all_pieces(colour_parameter):
        for move in gameBoard.valid_moves(piece.position):
            gameBoard_copy = deepcopy(gameBoard)
            temp_move(gameBoard_copy, (piece.position[0], piece.position[1], move))
            eval_score = minimax_alpha_beta(gameBoard_copy, depth - 1, float('-inf'), float('inf'), False,
                                            colour_parameter)

            if (gameBoard.current_player == 'white' and eval_score > best_score) or \
                    (gameBoard.current_player == 'black' and eval_score < best_score):
                best_score = eval_score
                best_piece = piece
                best_move = move
    return best_piece, best_move



# jeffrey task
# write a function that takes in one parameter which is always going to be gameBoard from main and will return the piece that is going to move and the row and col to move to
# To summarize:
# Input: instance of type Board (will always be gameBoard)
# Output: piece(the actual INSTANCE such as the knight or pawn object as we can see in the debugger), row and col to move to
def random_moves(gameBoard, hi, colour_parameter):
    colour = colour_parameter
    pieces = []
    for x in range(8):
        for y in range(8):
            piece = gameBoard.chessBoard[x][y]
            if piece is not None and piece.colour == colour:
                pieces.append(piece)

    if pieces:  # Check if there are any white pieces
        random_piece = choice(pieces)  # Choose a random piece from the list
        random_piece_moves = gameBoard.valid_moves(random_piece.position)  # Get valid moves for the random piece
        if random_piece_moves:  # Check if there are any valid moves
            random_move = choice(random_piece_moves)  # Choose a random move for the random piece
            return random_piece, random_move  # Return the piece and the randomly selected move
        while not random_piece_moves:
            random_piece = choice(pieces)  # Choose a random piece from the list
            random_piece_moves = gameBoard.valid_moves(random_piece.position)
            if random_piece_moves:  # Check if there are any valid moves
                random_move = choice(random_piece_moves)  # Choose a random move for the random piece
                return random_piece, random_move  # Return the piece and the randomly selected move
                continue
            else:
                if gameBoard.checkmate(colour) or gameBoard.stalemate(colour):
                    return None
                    continue
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

    piece_value_eval=white_values - black_values
    return piece_value_eval

def minimax_alpha_beta(gameBoard, depth, alpha, beta, maximizingPlayer, colour_parameter):
    colour = colour_parameter
    if depth == 0 or gameBoard.checkmate(colour) or gameBoard.stalemate(colour):
        return eval(gameBoard)
    gameBoard_copy = deepcopy(gameBoard)
    if maximizingPlayer:
        max_eval = float('-inf')
        for move in get_all_moves(gameBoard,colour_parameter):
            temp_move(gameBoard_copy,move)
            eval_score = minimax_alpha_beta(gameBoard_copy, depth - 1, alpha, beta, False, colour)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_all_moves(gameBoard, colour_parameter):
            gameBoard_copy = deepcopy(gameBoard)  # Create a copy of the game board
            temp_move(gameBoard_copy, move)  # Apply the move to the copied game board
            eval_score = minimax_alpha_beta(gameBoard_copy, depth - 1, alpha, beta, True, colour)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval








def get_all_moves(gameBoard, colour_parameter):
    colour = colour_parameter
    moves = []
    pieces = []
    for x in range(8):
        for y in range(8):
            piece = gameBoard.chessBoard[x][y]
            if piece is not None and piece.colour == colour:
                pieces.append(piece)

    for piece in pieces:
        piece_moves = gameBoard.valid_moves(piece.position)
        moves.extend([(piece.position[0], piece.position[1], move) for move in piece_moves])
    return moves

def temp_move(gameBoard,move):
    original_board_state = deepcopy(gameBoard)
    row, col, new_row, new_col = move
    piece_to_move=gameBoard.chessBoard[row][col]
    list_of_moves_for_piece_to_move=gameBoard.valid_moves(piece_to_move.position)
    gameBoard.make_move(new_row,new_col,list_of_moves_for_piece_to_move,piece_to_move)


def eval(gameBoard):
    material_score=piece_values(gameBoard)
    # You can add more evaluation factors here and calculate their scores
    # For example:
    # mobility_score = mobility_evaluation(gameBoard)
    # pawn_structure_score = pawn_structure_evaluation(gameBoard)
    # king_safety_score = king_safety_evaluation(gameBoard)
    # Combine the scores into a single evaluation score
    combined_score = material_score  # Initialize with material score
    # Combine with other scores if applicable
    # combined_score += mobility_score
    # combined_score += pawn_structure_score
    # combined_score += king_safety_score
    return combined_score

