import pytest
from src.game.gameBoard import GameBoard
from src.game.card import Card
from collections import Counter
from src.game.exceptions import GameError

@pytest.fixture
def game_board():
    board = GameBoard((5, 6))
    return board
    
@pytest.mark.parametrize("size", [
    ((2, 3)),
    ((5, 6))
])
def test_create_game_board(size):
    """GameBoard is initialized correctly and all cells contains Card-objects """
    board = GameBoard(size)
    rows, column = size

    assert board.rows == rows
    assert board.columns == column

    for row in board.board:
        for cell in row:
            assert isinstance(cell, Card)


def test_card_id_image_appear_twice_in_board(game_board):
    cards = []
    for row in game_board.board:
        for cell in row:
            cards.append((cell.id, cell.image))

    counter = Counter(cards)

    for key in counter:
        assert counter[key] == 2

@pytest.mark.parametrize("cell, should_raise", [
    ((0, 0), False),
    ((4, 5), False),
    ((8, 3), True)
])
def test_flip_card(game_board, cell, should_raise):
    """Test flipping cards, should raise a GameError if outside board"""
    if should_raise:
        with pytest.raises(GameError):
            game_board.flip_card(cell)
    else:
        row, col = cell
        game_board.flip_card(cell)
        assert game_board.board[row][col].is_flipped

def test_flip_card_that_is_flipped(game_board):
    game_board.board[0][0].is_flipped = True
    with pytest.raises(GameError):
            game_board.flip_card((0, 0))

def test_flip_card_that_is_matched(game_board):
    game_board.board[0][0].is_matched = True
    with pytest.raises(GameError):
            game_board.flip_card((0, 0))

def test_reset_board_clear_flipped_cards(game_board):
    game_board.flip_card((2, 3))
    game_board.flip_card((3, 3))
    game_board.flip_card((2, 4))
    game_board.flip_card((0, 3))

    game_board.prepare_next_round()

    for row in game_board.board:
        for cell in row:
            assert not cell.is_flipped
    assert game_board.flipped_cards == []

@pytest.mark.parametrize("flip_1, flip_2, expected", [
    ((0, 0), (0, 1), True),
    ((0, 0), (1, 0), False)
])
def test_check_matched(game_board, flip_1, flip_2, expected):
    for i, row in enumerate(game_board.board):
        for cell in row:
            cell.id = "100" if i % 2 else "200"

    game_board.flip_card(flip_1)
    game_board.flip_card(flip_2)
    row1, col1 = flip_1
    row2, col2 = flip_2

    assert game_board.check_match() == expected
    assert game_board.board[row1][col1].is_matched == expected
    assert game_board.board[row2][col2].is_matched == expected

@pytest.mark.parametrize("all_cards, expected", [
    (True, True),
    (False, False)
])
def test_is_all_card_matched(game_board, all_cards,  expected):
    if all_cards:
        for row in game_board.board:
            for card in row:
                card.is_matched = True

    assert game_board.all_cards_matched() == expected