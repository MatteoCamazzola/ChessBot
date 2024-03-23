import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
from src.board.Chess_Board import Board
from src.bot.algorthim import random_moves

root = tk.Tk()
root.title("Chessboard")
canvas = tk.Canvas(root, width=472, height=472)
canvas.pack()

current_player = "white"
selected_piece = None
square_size = 59
gameBoard = Board()

return_from_function = random_moves(gameBoard)

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
    for row in range(8):
        for col in range(8):
            piece = gameBoard.chessBoard[row][col]
            if piece is not None:
                # Create a new image for the piece with the tag "piece"
                canvas.create_image(col * 59 + 59 / 2, row * 59 + 59 / 2, image=piece.image,
                                    anchor="center", tags="piece")


def on_canvas_click(event):
    global selected_piece
    global current_player
    col = int(event.x // square_size)
    row = int(event.y // square_size)
    # Now you have the row and column stored in row and col variables
    print(f"Clicked on row: {row}, col: {col}")
    piece = gameBoard.chessBoard[row][col]
    # if clicking on piece
    if piece is not None and piece.colour == current_player:
        valid_moves = []
        if selected_piece != None:
            valid_moves = gameBoard.valid_moves(selected_piece.position)
        if (row, col) in valid_moves:
            gameBoard.make_move(row, col, gameBoard.valid_moves(selected_piece.position), selected_piece)
            place_pieces()
            selected_piece = None
            remove_possible_moves()
            if current_player == "white":
                current_player = "black"
            else:
                current_player = "white"
        elif piece == selected_piece:
            remove_possible_moves()
            selected_piece = None
        else:
            selected_piece = piece
            remove_possible_moves()
            show_possible_moves(piece)
    # make move
    elif piece is None and selected_piece is not None:
        if gameBoard.is_valid_move((row, col), selected_piece):
            gameBoard.make_move(row, col, gameBoard.valid_moves(selected_piece.position), selected_piece)
            place_pieces()
            selected_piece = None
            remove_possible_moves()
            if current_player == "white":
                current_player = "black"
            else:
                current_player = "white"
    # capture piece
    if selected_piece != None:
        if (piece is not None and piece.colour != selected_piece.colour):
            if gameBoard.is_valid_move((row, col), selected_piece):
                gameBoard.make_move(row, col, gameBoard.valid_moves(selected_piece.position), selected_piece)
                place_pieces()
                selected_piece = None
                remove_possible_moves()
                if current_player == "white":
                    current_player = "black"
                else:
                    current_player = "white"


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


draw_chessboard()
place_pieces()

canvas.bind("<Button-1>", on_canvas_click)
root.mainloop()
