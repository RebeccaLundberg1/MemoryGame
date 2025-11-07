from .card import Card
import random

class Game_board:
    def __init__(self, size:tuple):
        self.rows, self.columns = size
        self.board = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        self.setup_board()

    def setup_board(self):
        """create list of cards, shuffle cards and add them to board"""
        cards = []
        cards_dubblets = []
        image = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"] #Detta borde kanske vara en lista av bilder någon annanstans som importeras? 
        for i in range((self.rows * self.columns) // 2):
            cards.append(Card(i, image[i]))
            cards_dubblets.append(Card(i, image[i]))
        cards = cards + cards_dubblets
        random.shuffle(cards)

        index = 0
        for row in range(self.rows):
            for column in range(self.columns):
                self.board[row][column] = cards[index]
                index += 1
        
    def print_board(self):
        for i in range(self.columns + 1):
            print(f"{i:^5}", end="")
        print()

        for r in range(self.rows):
            for c in range(self.columns):
                if c == 0:
                    print(f"{r+1:^5}", end="")
                card = self.board[r][c]
                print(f"{card.image:^5}" if card.is_flipped else f"{'[ ]':^5}" , end="")
                if c == self.columns - 1:
                    print()

    def all_cards_matched(self) -> bool:
        """ iterate through cards in board to see if all card is matched
            return true if all cards is matched, else return false"""
        for r in range(self.rows):
            for c in range(self.columns):
                if not self.board[r][c].is_matched:
                    return False
        return True

    def flip_card(self, row, column):
        self.board[row][column].flip_card()
        pass

    def check_match(self, pos1:tuple, pos2:tuple):
        row1, col1 = pos1
        row2, col2 = pos2
        if pos1 == pos2:
            return False
        
        card1 = self.board[row1][col1]
        card2 = self.board[row2][col2]
        
        if card1.id == card2.id:
            self.set_card_to_is_matched(card1)
            self.set_card_to_is_matched(card2)
            return True
        return False

    def set_card_to_is_matched(self, card:Card):
        card.is_matched = True