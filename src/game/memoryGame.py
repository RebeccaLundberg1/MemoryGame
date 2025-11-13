from .gameBoard import GameBoard
from .exceptions import NotAbleToMatchError
from .player import Player

class MemoryGame:
    def __init__(self, size:tuple, players:list[Player] = None):
        if players == None:
            players = []
        self.players = players
        self.size = size
        self.game = GameBoard(size)
        self.current_player = 0
        self.flipps_in_round = 0

    def is_game_ready_to_start(self) -> bool:
        """ Check if there is players added to the game """
        return bool(self.players)
    
    def update_latest_game(self, dict) -> None:
        """ 
        Update game status from JSON
        
        Reconstruct players, restore board and update the gama status such as 
        current player and flipps in round.
        
        Args:
            dict, expetcted keys:
                'players'
                'board'
                'current_player'
                'flipps_in_round' 
        """
        for p in dict["players"]:
            player = Player(p["name"])
            player.nbr_of_matches = p["nbr_of_matches"]
            player.nbr_of_flipps = p["nbr_of_flipps"]
            self.players.append(player)
            ### Ska detta kanske ligga hos en player
        
        self.game.update_board(dict["board"])

        self.current_player = dict["current_player"]
        self.flipps_in_round = dict["flipps_in_round"]

    def is_finished(self) -> bool:
        """Check if the game is finished."""
        return self.game.all_cards_matched()

    def print_summary(self) -> None:
        """
        Prints a summary of the game.

        Displays the winner or winners, along with a list of all players
        and their total number of matched pairs.
        """
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

    def try_flip(self, card_postion:tuple) -> None:
        """
        Try flip a card at the given position.

        If the flip is successful, increments 'flipps_in_round' by 1.

        Args:
            card_position(tuple): The cell coordinates (row, column) of the card to flip.
        """
        if self.game.flip_card(card_postion):
            self.flipps_in_round += 1

    def try_match(self) -> bool:
        """
        Check if the two flipped cards is a pair.

        If two cards has been flipped:
        - Increment the current player's flip count.
        - If its a match, increment the current player's match count.
        - If not a match, switsh player.

        Raises: 
            NotAbleToMatchError: if 'flipps in round' != 2
        """  
        if self.flipps_in_round == 2:
            self.players[self.current_player].add_flip()
            if self.game.check_match():
                self.players[self.current_player].add_match()
                return True
            else:
                self.switch_player()
                return False
        raise NotAbleToMatchError("You need to turn to cards before match is able")

    def switch_player(self) -> None:
        """Increment current_player by 1 or set to 0 if end of players list is reached)"""
        self.current_player = (self.current_player + 1) % len(self.players)

    def set_next_round(self) -> None:
        """Reset all cards to unflipped and reset flipps in round"""
        self.game.prepare_next_round()
        self.flipps_in_round = 0

    def print_board(self) -> None:
        self.game.print_board()

    def to_dict(self) -> dict:
        """
        Return all necessary game information about a game as a dictionary.

        Returns: 
            dict: all data required to save the game state to JSON.
        """
        return {
            "size" : self.size,
            "players": [p.to_dict() for p in self.players],
            "board": self.game.to_dict(),
            "current_player": self.current_player,
            "flipps_in_round": self.flipps_in_round
        }