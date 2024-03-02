from PIL import Image, ImageTk

class ChessPiece:
    def __init__(self, colour, row, col, piece_type):
        self.colour = colour
        self.position = (row, col)
        self.piece_type = piece_type
        self.image = self.load_image(colour, piece_type)

    def load_image(self, colour, piece_type):
        filename = f"images/{colour}_{piece_type}.png"
        image = Image.open(filename)
        photo = ImageTk.PhotoImage(image)
        return photo
