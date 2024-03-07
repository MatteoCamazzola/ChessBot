import tkinter as tk
from src.board.Chess_Board import Board

root = tk.Tk()
root.title("Chessboard")

gameBoard = Board()

canvas = tk.Canvas(root, width=450, height=450)
canvas.pack()


def draw_chessboard():
    square_color = "#F5F5DC"
    square_size = 56.25
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
    for row in range(8):
        for col in range(8):
            piece = gameBoard.chessBoard[row][col]
            if piece is not None:
                canvas.create_image(col * 56.25 + 56.25 / 2, row * 56.25 + 56.25 / 2, image=piece.image,
                                    anchor="center")


current_position = (0,0)
valid_moves = gameBoard.valid_moves(current_position)
possible_captures = gameBoard.possible_captures(valid_moves, gameBoard.chessBoard[0][0])


draw_chessboard()
place_pieces()
root.mainloop()
