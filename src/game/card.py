#List of all images witch are used as Card-images
card_images = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

class Card:
    def __init__(self, id: int, image):
        self.id = id
        self.image = image
        self.is_flipped = False
        self.is_matched = False
    
    def flip_card(self) -> None:
        self.is_flipped = not self.is_flipped

    def set_is_matched(self) -> None:
        self.is_matched = True

    