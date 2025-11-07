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
        image = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"] #Detta borde kanske vara en lista av bilder någon annanstans som importeras? 
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
        for r in range(self.rows):
            for c in range(self.columns):
                card = self.board[r][c]
                print(f"{card.image:^5}" if card.is_flipped else f"{'o':^5}" , end="")
                if c == self.columns - 1:
                    print()
        
game = Game_board((2,3))
game.print_board()