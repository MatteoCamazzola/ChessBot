from src.board.Chess_Board import Board
from random import choice


# jeffrey task
# write a function that takes in one parameter which is always going to be gameBoard from main and will return the piece that is going to move and the row and col to move to
# To summarize:
# Input: instance of type Board (will always be gameBoard)
# Output: piece(the actual INSTANCE such as the knight or pawn object as we can see in the debugger), row and col to move to
def random_moves(gameBoard, colour_parameter):
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

