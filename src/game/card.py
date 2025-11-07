class Card:
    def __init__(self, id: int, image, ):
        self.id = id
        self.image = image
        self.is_flipped = False
        self.is_matched = False
    
    def flip_card(self):
        self.is_flipped = not self.is_flipped

    