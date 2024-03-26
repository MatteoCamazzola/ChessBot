import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk
from src.board.Chess_Board import Board
from src.bot.algorthim import get_best_move
from src.bot.algorthim import random_moves
import csv
import os

root = tk.Tk()
root.title("Chessboard")
canvas = tk.Canvas(root, width=472, height=472)
canvas.pack()

play_as_bot = True
selected_colour = "white"
selected_piece = None
current_player = "white"
square_size = 59
gameBoard = Board()

# setup opening_theory file

# Construct the path to the .tsv file
current_dir = os.path.dirname(__file__)  # Get the directory where bot_game.py is located
parent_dir = os.path.dirname(current_dir)  # Navigate up to the Chess_bot directory
data_dir = os.path.join(parent_dir, 'opening_data')  # Navigate into the opening_data directory
tsv_file_path = os.path.join(data_dir, 'opening_theory.tsv')  # Path to the .tsv file


def draw_chessboard():
    square_color = "#F5F5DC"
    for row in range(8):
        for col in range(8):
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=square_color, outline="black")
            square_color = "#C19A6B" if square_color == "#F5F5DC" else "#F5F5DC"
        square_color = "#C19A6B" if square_color == "#F5F5DC" else "#F5F5DC"


def place_pieces():
    # Delete all previously drawn pieces
    canvas.delete("piece")
    if selected_colour == "black":
        for row in range(8):
            for col in range(8):
                piece = gameBoard.chessBoard[row][col]
                if piece is not None:
                    # Create a new image for the piece with the tag "piece"
                    canvas.create_image(col * 59 + 59 / 2, row * 59 + 59 / 2, image=piece.image,
                                        anchor="center", tags="piece")
    else:
        # swap_board()
        for row in range(8):
            for col in range(8):
                piece = gameBoard.chessBoard[row][col]
                if piece is not None:
                    new_row = row_col_swap(row)
                    new_col = row_col_swap(col)
                    # Create a new image for the piece with the tag "piece"
                    canvas.create_image(new_col * 59 + 59 / 2, new_row * 59 + 59 / 2, image=piece.image,
                                        anchor="center", tags="piece")


def on_canvas_click(event):
    global selected_piece
    global selected_colour
    if selected_colour == "white":
        col = row_col_swap(int(event.x // square_size))
        row = row_col_swap(int(event.y // square_size))
    else:
        col = int(event.x // square_size)
        row = int(event.y // square_size)
    if current_player == "black":
        checkmate_check_colour = "white"
    else:
        checkmate_check_colour = "black"
    # Now you have the row and column stored in row and col variables
    print(f"Clicked on row: {row}, col: {col}")
    piece = gameBoard.chessBoard[row][col]
    # if clicking on piece that is your own colour
    if piece is not None and piece.colour == current_player:
        valid_moves = []
        if selected_piece != None:
            valid_moves = gameBoard.valid_moves(selected_piece.position)
        if (row, col) in valid_moves:

            # stuff for book moves for bot
            if gameBoard.number_of_moves_made < 20:
                pgn_move = translator_to_pgn(row, col, selected_piece)
                gameBoard.number_of_moves_made = gameBoard.number_of_moves_made + 1
                gameBoard.previous_moves += (
                                                f"{gameBoard.number_of_moves_made // 2 + 1}." if gameBoard.number_of_moves_made % 2 == 1 else '') + f" {pgn_move} "

            gameBoard.make_move(row, col, gameBoard.valid_moves(selected_piece.position), selected_piece)
            place_pieces()
            selected_piece = None
            remove_possible_moves()
            root.after(200, lambda: check_for_game_over(checkmate_check_colour))
            current_player_swap()
            # bot move
            bot_move = random_moves(gameBoard, 3, current_player)
            if bot_move is not None:
                if gameBoard.number_of_moves_made < 20:
                    pgn_move = translator_to_pgn(bot_move[1][0], bot_move[1][1], bot_move[0])
                    gameBoard.number_of_moves_made = gameBoard.number_of_moves_made + 1
                    gameBoard.previous_moves += (
                                                    f"{gameBoard.number_of_moves_made // 2 + 1}." if gameBoard.number_of_moves_made % 2 == 1 else '') + f" {pgn_move} "

                gameBoard.make_move(bot_move[1][0], bot_move[1][1], gameBoard.valid_moves(bot_move[0].position),
                                    bot_move[0])
                place_pieces()
                current_player_swap()

        elif piece == selected_piece:
            remove_possible_moves()
            selected_piece = None
        else:
            selected_piece = piece
            remove_possible_moves()
            show_possible_moves(piece)
    # moving piece to open square
    elif piece is None and selected_piece is not None:
        if gameBoard.is_valid_move((row, col), selected_piece):
            if gameBoard.number_of_moves_made < 20:
                pgn_move = translator_to_pgn(row, col, selected_piece)
                gameBoard.number_of_moves_made = gameBoard.number_of_moves_made + 1
                gameBoard.previous_moves += (
                                                f"{gameBoard.number_of_moves_made // 2 + 1}." if gameBoard.number_of_moves_made % 2 == 1 else '') + f" {pgn_move} "

            gameBoard.make_move(row, col, gameBoard.valid_moves(selected_piece.position), selected_piece)
            place_pieces()
            selected_piece = None
            remove_possible_moves()
            root.after(200, lambda: check_for_game_over(checkmate_check_colour))
            current_player_swap()
            # bot move
            bot_move = random_moves(gameBoard, 3, current_player)
            if bot_move is not None:
                if gameBoard.number_of_moves_made < 20:
                    pgn_move = translator_to_pgn(bot_move[1][0], bot_move[1][1], bot_move[0])
                    gameBoard.number_of_moves_made = gameBoard.number_of_moves_made + 1
                    gameBoard.previous_moves += (
                                                    f"{gameBoard.number_of_moves_made // 2 + 1}." if gameBoard.number_of_moves_made % 2 == 1 else '') + f" {pgn_move} "

                gameBoard.make_move(bot_move[1][0], bot_move[1][1], gameBoard.valid_moves(bot_move[0].position),
                                    bot_move[0])
                place_pieces()
                current_player_swap()

    # capture piece
    if selected_piece != None:
        if (piece is not None and piece.colour != selected_piece.colour):
            if gameBoard.is_valid_move((row, col), selected_piece):
                if gameBoard.number_of_moves_made < 20:
                    pgn_move = translator_to_pgn(row, col, selected_piece)
                    gameBoard.number_of_moves_made = gameBoard.number_of_moves_made + 1
                    gameBoard.previous_moves += (
                                                    f"{gameBoard.number_of_moves_made // 2 + 1}." if gameBoard.number_of_moves_made % 2 == 1 else '') + f" {pgn_move} "

                gameBoard.make_move(row, col, gameBoard.valid_moves(selected_piece.position), selected_piece)
                place_pieces()
                selected_piece = None
                remove_possible_moves()
                root.after(200, lambda: check_for_game_over(checkmate_check_colour))
                current_player_swap()
                # bot move
                bot_move = random_moves(gameBoard, 3, current_player)
                if bot_move is not None:
                    pgn_move = translator_to_pgn(bot_move[1][0], bot_move[1][1], bot_move[0])
                    gameBoard.number_of_moves_made = gameBoard.number_of_moves_made + 1
                    gameBoard.previous_moves += (
                                                    f"{gameBoard.number_of_moves_made // 2 + 1}." if gameBoard.number_of_moves_made % 2 == 1 else '') + f" {pgn_move} "
                    gameBoard.make_move(bot_move[1][0], bot_move[1][1], gameBoard.valid_moves(bot_move[0].position),
                                        bot_move[0])
                    place_pieces()
                current_player_swap()


def remove_possible_moves():
    canvas.delete('valid_move')


def show_possible_moves(piece):
    global square_size
    valid_moves = gameBoard.valid_moves(piece.position)

    # Define the radius and alpha (transparency) for the circle
    circle_radius = square_size // 7  # Adjust as needed
    alpha = 255  # Adjust transparency (0=fully transparent, 255=fully opaque)

    for move in valid_moves:
        row, col = move
        if selected_colour == "white":
            row = row_col_swap(row)
            col = row_col_swap(col)

        # Create an off-screen image (RGBA for transparency support)
        img = Image.new('RGBA', (square_size, square_size), (0, 0, 0, 0))  # White, opaque background
        draw = ImageDraw.Draw(img)

        # Center of the off-screen image
        image_center_x = square_size // 2
        image_center_y = square_size // 2

        # Draw a fully opaque grey ellipse on the off-screen image
        draw.ellipse([(image_center_x - circle_radius, image_center_y - circle_radius),
                      (image_center_x + circle_radius, image_center_y + circle_radius)],
                     fill=(128, 128, 128, 98), outline=None)

        # Convert the PIL image to a Tkinter PhotoImage
        photo_img = ImageTk.PhotoImage(img)

        # Display the image on the canvas
        canvas.create_image(col * square_size + square_size // 2, row * square_size + square_size // 2,
                            image=photo_img, tags='valid_move')

        # Keep a reference to the image to prevent garbage collection
        if not hasattr(canvas, 'valid_move_images'):
            canvas.valid_move_images = []
        canvas.valid_move_images.append(photo_img)


def check_for_game_over(checkmate_check_colour):
    game_over_message = ""
    if gameBoard.checkmate(checkmate_check_colour):
        game_over_message = "Checkmate. "
        if checkmate_check_colour == "black":
            game_over_message += "White wins!"
        else:
            game_over_message += "Black wins!"
    elif gameBoard.stalemate(checkmate_check_colour):
        game_over_message = "Stalemate. The game is a draw."

    if game_over_message:  # If there's a game over message to display
        # Show the game over message in a pop-up
        messagebox.showinfo("Game Over", game_over_message)
        root.destroy()  # Close the Tkinter window after the user acknowledges the message


def row_col_swap(to_swap):
    if to_swap == 0:
        return 7
    if to_swap == 1:
        return 6
    if to_swap == 2:
        return 5
    if to_swap == 3:
        return 4
    if to_swap == 4:
        return 3
    if to_swap == 5:
        return 2
    if to_swap == 6:
        return 1
    if to_swap == 7:
        return 0


def swap_board():
    for row in range(4):
        for col in range(8):
            to_swap = gameBoard.chessBoard[row][col]
            row_to_move = row_col_swap(row)
            col_to_move = row_col_swap(col)
            temp = gameBoard.chessBoard[row_to_move][col_to_move]
            gameBoard.chessBoard[row_to_move][col_to_move] = to_swap
            gameBoard.chessBoard[row][col] = temp


def current_player_swap():
    global current_player
    if current_player == "white":
        current_player = "black"
    else:
        current_player = "white"


# note this may only be called after a move is made will translate the move that was just made
def translator_to_pgn(row_to_move, col_to_move, piece_to_move):
    files = 'abcdefgh'
    ranks = '87654321'

    # Determine if there's a capture
    is_capture = gameBoard.chessBoard[row_to_move][col_to_move] is not None and gameBoard.chessBoard[row_to_move][
        col_to_move].colour != piece_to_move.colour

    # Get the piece type and current position
    piece_type = piece_to_move.piece_type.capitalize()
    current_row, current_col = piece_to_move.position

    # Translate the current and target positions to PGN format
    from_square = files[current_col] + ranks[current_row]
    to_square = files[col_to_move] + ranks[row_to_move]

    # Construct the move notation
    move = ''
    if piece_type == 'Pawn':
        if is_capture:
            move = from_square[0] + 'x' + to_square  # Include originating file for pawn captures
        else:
            move = to_square
    else:
        move = piece_type[0] + ('x' if is_capture else '') + to_square

    # simulate move

    gameBoard.chessBoard[piece_to_move.position[0]][piece_to_move.position[1]] = None
    temp = gameBoard.chessBoard[row_to_move][col_to_move]
    gameBoard.chessBoard[row_to_move][col_to_move] = piece_to_move
    temp_white = gameBoard.white_king_pos
    temp_black = gameBoard.black_king_pos
    if piece_to_move.piece_type == "king":
        if piece_to_move.colour == "black":
            gameBoard.black_king_pos = move
        else:
            gameBoard.white_king_pos = move
    if piece_to_move.colour == "white":
        if gameBoard.is_check("black"):
            move += '+'
    else:
        if gameBoard.is_check("white"):
            move += '+'
    gameBoard.chessBoard[piece_to_move.position[0]][piece_to_move.position[1]] = piece_to_move
    gameBoard.chessBoard[row_to_move][col_to_move] = temp
    if piece_to_move.piece_type == "king":
        if piece_to_move.colour == "black":
            gameBoard.black_king_pos = temp_black
        else:
            gameBoard.white_king_pos = temp_white

    if gameBoard.chessBoard[row_to_move][col_to_move] != None:
        if gameBoard.chessBoard[row_to_move][col_to_move].colour == piece_to_move.colour:
            if abs(gameBoard.chessBoard[row_to_move][col_to_move].position[1] - piece_to_move.position[1]) > 3:
                move = "O-O-O"
            else:
                move = "O-O"

    return move


def translate_from_pgn(pgn_string):
    pass


def read_tsv(file_path):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')  # Set the delimiter to tab
        third_column_data = [row[2] for row in reader if len(row) > 2]  # List comprehension to extract the third column
    return third_column_data


draw_chessboard()
place_pieces()

if (play_as_bot and selected_colour == "white") or (selected_colour == "black" and not play_as_bot):
    bot_colour = selected_colour
    bot_move = random_moves(gameBoard, 3, bot_colour)
    if bot_move is not None:
        if gameBoard.number_of_moves_made < 20:
            pgn_move = translator_to_pgn(bot_move[1][0], bot_move[1][1], bot_move[0])
            gameBoard.number_of_moves_made = gameBoard.number_of_moves_made + 1
            gameBoard.previous_moves += (
                                            f"{gameBoard.number_of_moves_made // 2 + 1}." if gameBoard.number_of_moves_made % 2 == 1 else '') + f" {pgn_move} "


        gameBoard.make_move(bot_move[1][0], bot_move[1][1], gameBoard.valid_moves(bot_move[0].position),
                            bot_move[0])
        place_pieces()
        current_player_swap()

opening_data = read_tsv(tsv_file_path)
pgn_move = translator_to_pgn(2, 0, gameBoard.chessBoard[0][0])
canvas.bind("<Button-1>", on_canvas_click)
root.mainloop()
