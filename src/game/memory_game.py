from .player import Player
from .game_board import Game_board

class Memory_game:
    def __init__(self, name:str, size:tuple):
        self.player = Player(name)
        self.game = Game_board(size)
        self.nbr_of_flipps = 0

    