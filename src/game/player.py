class Player:
    def __init__(self, name:str):
        self.name = name
        self.top_scores = {
            "2x3": 0,
            "3x4": 0,
            "4x5": 0,
            "5x6": 0
            }