from .game_board import Game_board
from .player import Player

def NotAbleToMatchError(Exception):
    pass

class Memory_game:
    def __init__(self, players:list[Player], size:tuple):
        self.players = players
        self.current_player = 0
        self.game = Game_board(size)
        self.flipps_in_round = 0

    def is_finished(self):
        return self.game.all_cards_matched()

    def print_summary(self):
        most_pairs = max(p.nbr_of_matches for p in self.players)
        player_won = [p.name for p in self.players if p.nbr_of_matches == most_pairs]
        player_won_name = ' & '.join(player_won)

        print("=" * 50)
        print("Game is over")
        if len(player_won) == 1:
            print(f"Congratulations {player_won_name}, you won the game!")
        else: 
            print(f"Congratulations, it is a tie, {player_won_name}, you won the game!")

        print()
        for player in self.players:
            print(f"{player.name}: {player.nbr_of_matches} pairs")
        print("=" * 50)

    def try_flip(self, card_postion:tuple):
        """ try flip_card(), if true then add one to flipps_in_round"""
        if self.game.flip_card(card_postion):
            self.flipps_in_round += 1

    def try_match(self):
        """ if two flipps are made, add 1 to nbr of flipps then check if it is
            a match. If it is, add 1 to nbr_of_matches """  
        if self.flipps_in_round == 2:
            self.players[self.current_player].add_flip()
            if self.game.check_match():
                self.players[self.current_player].add_match()
                return True
            else:
                self.switch_player()
                return False
        raise NotAbleToMatchError("You need to turn to cards before match is able")

    def switch_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def set_next_round(self):
        """ set_cards_to_not_flipped() and then reset flipps in round to 0 to 
            allow player to do a new first choice"""
        self.game.set_cards_to_not_flipped()
        self.flipps_in_round = 0

    def print_board(self):
        self.game.print_board()