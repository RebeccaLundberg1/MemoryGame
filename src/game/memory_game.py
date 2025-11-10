from .game_board import Game_board

def NotAbleToMatchError(Exception):
    pass

class Memory_game:
    def __init__(self, name:str, size:tuple):
        self.player = name
        self.game = Game_board(size)
        self.nbr_of_flipps = 0
        self.nbr_of_matches = 0
        self.flipps_in_round = 0

    def is_finished(self):
        return self.game.all_cards_matched()

    def print_summery(self):
        print("=" * 50)
        print(f"Congratulations {self.player.name}, you solved the memory!\n"
              f"Total attemts: {self.nbr_of_flipps}\n"
              f"Board: {self.game.rows} x {self.game.columns}")
        print("=" * 50)

    def try_flip(self, card_postion:tuple):
        """ try flip_card(), if true then add one to flipps_in_round"""
        if self.game.flip_card(card_postion):
            self.flipps_in_round += 1

    def try_match(self):  
        """ if two flipps are made, add 1 to nbr of flipps then check if it is
            a match. If it is, add 1 to nbr_of_matches """  
        if self.flipps_in_round == 2:
            self.nbr_of_flipps += 1
            if self.game.check_match():
                self.nbr_of_matches += 1
                return True
            return False
        raise NotAbleToMatchError("You need to turn to cards before match is able")

    def set_next_round(self):
        """ set_cards_to_not_flipped() and then reset flipps in round to 0 to 
            allow player to do a new first choice"""
        self.game.set_cards_to_not_flipped()
        self.flipps_in_round = 0

    def print_board(self):
        self.game.print_board()