from .player import Player
from .game_board import Game_board

class Memory_game:
    def __init__(self, name:str, size:tuple):
        self.player = Player(name)
        self.game = Game_board(size)
        self.nbr_of_flipps = 0
        self.nbr_of_matches = 0
        self.flipps_in_round = 0

    def is_finished(self):
        if self.game.all_cards_matched():
            return True
        else:
            return False
    
    def print_board(self):
        self.game.print_board()

    def try_flip(self, card_postion:tuple):    
        if self.game.flip_card(card_postion):
            self.flipps_in_round += 1

    def try_match(self):    
        if self.flipps_in_round == 2:
            self.nbr_of_flipps += 1
            if self.game.check_match():
                self.nbr_of_matches += 1
                return True
            return False
        #raise ett fel? inte gjort två vändningar?

    def set_next_round(self):
        self.game.set_cards_to_not_flipped()
        self.flipps_in_round = 0