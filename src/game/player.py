class Player:
    def __init__(self, name):
        self.name = name
        self.nbr_of_matches = 0
        self.nbr_of_flipps = 0

    def add_match(self):
        self.nbr_of_matches += 1

    def add_flip(self):
        self.nbr_of_flipps += 1