from .player import Player
from .game_board import Game_board

class Memory_game:
    def __init__(self, name:str, size:tuple):
        self.player = Player(name)
        self.game = Game_board(size)
        self.nbr_of_flipps = 0
        self.nbr_of_matches = 0
        self.cards_flipped = 0
    
    def is_finished(self):
        if self.game.all_cards_matched():
            return True
        else:
            return False
    
    def print_board(self):
        self.game.print_board()

    def flip(self, row, column):
        self.game.flip_card(row, column)