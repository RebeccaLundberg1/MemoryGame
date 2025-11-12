import pytest
from src.game.memoryGame import MemoryGame
from src.game.player import Player
from src.game.exceptions import GameError


@pytest.fixture
def memory_game():
    """ create a new game to use in test below"""
    players = [Player(f"name{i}") for i in range(4)]
    game = MemoryGame((5,6), players)
    return game


#def test_create_game(): ska inte gå om man inte har några players? Eller kanske  
# i main som det inte ska gå köra run_game utifall players är 0??

@pytest.mark.parametrize("cell, should_raise", [
    ((0, 0), False),
    ((8, 8), True)
])
def test_flip_card(memory_game, cell, should_raise):
    """ when a card is flipped. flipps_in_round should increase by 1, if card 
        is unable to flip exception is raised """
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
def test_match_card(memory_game, flip_1, flip_2, is_match):
    """ manipulate card_id for every card att board to only two diffret id numbers,
        then flip two cards and try to match. If is_match try_match should
        return True, and current player should now have 1 match and flip."""
    for i, row in enumerate(memory_game.game.board):
        for cell in row:
            cell.id = "100" if i % 2 else "200"

    memory_game.try_flip(flip_1)
    memory_game.try_flip(flip_2)
    start_player_index = memory_game.current_player

    if is_match:
        current_player = memory_game.players[memory_game.current_player]
        assert memory_game.try_match()
        assert current_player.nbr_of_matches == 1
        assert current_player.nbr_of_flipps == 1
    else:
        assert not memory_game.try_match()

@pytest.mark.parametrize("current_index, expected", [
    (0, 1),
    (3, 0),
])
def test_switch_player(memory_game, current_index, expected):
    """ try switch_player, current_player should increase by one until last index
        in players, then current_player equals 0 again"""
    memory_game.current_player = current_index
    memory_game.switch_player() 
    assert memory_game.current_player == expected



