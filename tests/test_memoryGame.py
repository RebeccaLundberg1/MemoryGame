import pytest
from src.game.memoryGame import MemoryGame
from src.game.player import Player
from src.game.exceptions import GameError


@pytest.fixture
def memory_game():
    players = [Player(f"name{i}") for i in range(4)]
    game = MemoryGame((5,6), players)
    return game

def test_start_game_without_players(memory_game):
    memory_game.players = []
    assert not memory_game.is_game_ready_to_start()

@pytest.mark.parametrize("cell, should_raise", [
    ((0, 0), False),
    ((8, 8), True)
])
def test_increment_flipps_in_round_when_flip_card(memory_game, cell, should_raise):
    if should_raise:
        with pytest.raises(GameError):
            memory_game.try_flip(cell)
    else:
        memory_game.try_flip(cell)
        assert memory_game.flipps_in_round == 1

@pytest.mark.parametrize("flip_1, flip_2, is_match", [
    ((0, 0), (0, 1), True),
    ((0, 0), (1, 0), False)
])
def test_match_cards(memory_game, flip_1, flip_2, is_match):
    """Flips two cards and checks if match and player stats update correctly."""
    for i, row in enumerate(memory_game.game.board):
        for cell in row:
            cell.id = "100" if i % 2 else "200"

    memory_game.try_flip(flip_1)
    memory_game.try_flip(flip_2)
    start_player_index = memory_game.current_player

    current_player = memory_game.players[memory_game.current_player]
    if is_match:
        assert memory_game.try_match()
        assert current_player.nbr_of_matches == 1
        assert current_player.nbr_of_flipps == 1
    else:
        assert not memory_game.try_match()
        assert current_player.nbr_of_flipps == 1

@pytest.mark.parametrize("current_index, expected", [
    (0, 1),
    (3, 0),
])
def test_switch_player(memory_game, current_index, expected):
    """Test that current_player switches correctly, back to 0 after the last player."""
    memory_game.current_player = current_index
    memory_game.switch_player() 
    assert memory_game.current_player == expected



