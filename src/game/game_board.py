from .card import Card
from .exceptions import PositionIsIncorrect, CardAlreadyFlippedError, CardAlreadyMatchedError
import random

class Game_board:
    def __init__(self, size:tuple):
        self.rows, self.columns = size
        self.board = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        self.flipped_cards = [] #Till en kölista? så man lägger till och tar bort en för att bara spara två samtidigt?
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

    def update_board(self, latest_board_status):
        for r in range(self.rows):
            for c in range(self.columns):
                card_status = latest_board_status[r][c]
                self.board[r][c].id = card_status["id"]
                self.board[r][c].image = card_status["image"]
                self.board[r][c].is_matched = card_status["matched"]
                self.board[r][c].is_flipped = card_status["flipped"]
        
    def print_board(self):
        """ Prints the board with a top and left row/colmun with index numbers for
            a more playerfriendly look"""
        for i in range(self.columns + 1):
            print(f"{i:^5}", end="")
        print()

        for r in range(self.rows):
            for c in range(self.columns):
                if c == 0:
                    print(f"{r+1:^5}", end="")
                card = self.board[r][c]
                print(f"{card.image:^5}" if card.is_matched or card.is_flipped else f"{'[ ]':^5}" , end="")
                if c == self.columns - 1:
                    print()

    def all_cards_matched(self) -> bool:
        """ iterate through cards in board to see if all card is matched
            return true if all cards is matched, else return false"""
        for row in self.board:
            for card in row:
                if not card.is_matched:
                    return False
        return True

    def flip_card(self, card_postion:tuple):
        """ first verify that card that is flipping is a valid card to flip 
            (not already matched or flipped), then flip card and return True """
        if not self.is_position_valid(card_postion):
            raise PositionIsIncorrect("You entered a position outside the board")
        
        if self.is_card_already_matched(card_postion):
            raise CardAlreadyMatchedError("Can't choose a card that is already matched")
        
        if self.is_card_already_flipped(card_postion):
            raise CardAlreadyFlippedError("Can't choose a card that is already flipped") 
        
        row, column = card_postion
        self.board[row][column].flip_card()
        self.flipped_cards.append(card_postion)
        return True
    
    def is_position_valid(self, card_postion:tuple):
        """Check if position is on the board, """
        row, col = card_postion
        if row < 0 or row >= self.rows:
            return False
        elif col < 0 or col >= self.columns:
            return False
        return True

    def is_card_already_matched(self, card_postion:tuple):
        """Check if card in position is already matched"""
        row, col = card_postion
        return self.board[row][col].is_matched
    
    def is_card_already_flipped(self, card_postion:tuple):
        """Check if card in position is already flipped"""
        row, col = card_postion
        return self.board[row][col].is_flipped
    
    def set_cards_to_not_flipped(self):
        """Iterate through board and sets all cards to: is_flipped = False"""
        for row in self.board:
            for card in row:
                card.is_flipped = False
    
    def check_match(self):
        """ Takes the two latest saved card positions in self.flipped_cards[]
            to see if the id is equal. If equal, then it is a match."""
        row1, col1 = self.flipped_cards[-2]
        row2, col2 = self.flipped_cards[-1]
        
        card1 = self.board[row1][col1]
        card2 = self.board[row2][col2]
        
        if card1.id == card2.id:
            self.set_card_to_is_matched(card1)
            self.set_card_to_is_matched(card2)
            return True
        return False

    def set_card_to_is_matched(self, card:Card):
        card.is_matched = True

    def to_list(self):
        return [
                [{"id": card.id, 
                  "image": card.image, 
                  "matched": card.is_matched, 
                  "flipped": card.is_flipped} 
                for card in row] 
               for row in self.board]