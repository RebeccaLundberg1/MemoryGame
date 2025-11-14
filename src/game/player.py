def update_players(players_info: list):
    """" Reconstruct players from saved game """
    players = []
    for p in players_info:
        player = Player(p["name"])
        player.nbr_of_matches = p["nbr_of_matches"]
        player.nbr_of_flipps = p["nbr_of_flipps"]
        players.append(player)
    
    return players


class Player:
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Name can't be empty")
        self.name = name
        self.nbr_of_matches = 0
        self.nbr_of_flipps = 0

    def add_match(self):
        self.nbr_of_matches += 1

    def add_flip(self):
        self.nbr_of_flipps += 1

    def to_dict(self):
        """
        Return all necessary information about the player as a dictionary.

        Returns: 
            dict: all board data required to later restore the board state from JSON.
        """
        return {"name": self.name,
                "nbr_of_matches": self.nbr_of_matches, 
                "nbr_of_flipps": self.nbr_of_flipps}