class Player:
    def __init__(self, name):
        self.name = name #Något som stoppar den från att vara en tom sträng?
        self.nbr_of_matches = 0
        self.nbr_of_flipps = 0

    def add_match(self):
        self.nbr_of_matches += 1

    def add_flip(self):
        self.nbr_of_flipps += 1

    def to_dict(self):
        return {"name": self.name,
                "nbr_of_matches": self.nbr_of_matches, 
                "nbr_of_flipps": self.nbr_of_flipps}