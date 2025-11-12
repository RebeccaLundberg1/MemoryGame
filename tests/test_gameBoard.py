import pytest
from src.game.gameBoard import GameBoard
from src.game.card import Card
from collections import Counter
from src.game.exceptions import GameError

@pytest.fixture
def game_board():
    """ create a new Game_board to use in test below"""
    board = GameBoard((5, 6))
    return board

@pytest.mark.parametrize("size", [
    ((2, 3)),
    ((5, 6))
])
def test_create_game_board(size):
    """ create an instance of Game_board. See if size is correct and iterate
        over board to see if the cell contains a Card object"""
    board = GameBoard(size)
    rows, column = size

    assert board.rows == rows
    assert board.columns == column

    for row in board.board:
        for cell in row:
            assert isinstance(cell, Card)


def test_card_id_image_appear_twice_in_board(game_board):
    """ create a list with all card(id, image) and by Counter validate that every
        card appears twice in board"""
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
    """ try flip card, should raise exception if cell is outside board, otherwise
        card is_flipped should be true"""
    if should_raise:
        with pytest.raises(GameError):
            game_board.flip_card(cell)
    else:
        row, col = cell
        game_board.flip_card(cell)
        assert game_board.board[row][col].is_flipped

def test_flip_card_that_is_flipped(game_board):
    """ flip a card that is already flipped should raise exception """
    game_board.board[0][0].is_flipped = True
    with pytest.raises(GameError):
            game_board.flip_card((0, 0))

def test_flip_card_that_is_matched(game_board):
    """ flip a card that is already matched should raise exception """
    game_board.board[0][0].is_matched = True
    with pytest.raises(GameError):
            game_board.flip_card((0, 0))

def test_make_all_cards_not_flipped(game_board):
    """ try set_cards_to_not_flipped by flipp some of the cards and then iterate
        over board to verify that all cards in cells is set to is_flipped, false"""
    game_board.flip_card((2, 3))
    game_board.flip_card((3, 3))
    game_board.flip_card((2, 4))
    game_board.flip_card((0, 3))

    game_board.set_cards_to_not_flipped()

    for row in game_board.board:
        for cell in row:
            assert not cell.is_flipped

@pytest.mark.parametrize("flip_1, flip_2, expected", [
    ((0, 0), (0, 1), True),
    ((0, 0), (1, 0), False)
])
def test_check_matched(game_board, flip_1, flip_2, expected):
    """ manipulate the cards id that every row got the same id, then try flip cards
        on same/diffrent row to try match and cards matched status"""
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
    """ first set all cards to matched if all_cards"""
    if all_cards:
        for row in game_board.board:
            for card in row:
                card.is_matched = True

    assert game_board.all_cards_matched() == expected