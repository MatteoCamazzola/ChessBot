from PIL import Image, ImageTk


class ChessPiece:
    def __init__(self, colour, row, col, piece_type, value):
        self.colour = colour
        self.position = (row, col)
        self.piece_type = piece_type
        self.image = self.load_image(colour, piece_type)
        self.value = value
        self.position_history = []
        self.has_moved_history = []

    def set_position(self, row, col, keep_history=True):
        if keep_history:
            self.position_history.append((self.row, self.col))
            self.has_moved_history.append(False if not self.position_history else True)
        self.row = row
        self.col = col

    def get_previous_position(self):
        if self.position_history:
            return self.position_history[-1]
        return None
    def load_image(self, colour, piece_type):
        filename = f"images/{colour}_{piece_type}.png"
        image = Image.open(filename)
        photo = ImageTk.PhotoImage(image)
        return photo
