import tkinter as tk
from board.board import Board

gameBoard = Board()

root = tk.Tk()
root.title("Chessboard")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

def draw_chessboard():
    square_color = "#F5F5DC"
    square_size = 50
    for row in range(8):
        for col in range(8):
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=square_color, outline="black")
            square_color = "#C19A6B" if square_color == "#F5F5DC" else "#F5F5DC"
        square_color = "#C19A6B" if square_color == "#F5F5DC" else "#F5F5DC"

draw_chessboard()


root.mainloop()