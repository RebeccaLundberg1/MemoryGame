from game.memory_game import Memory_game
import time
from game.player import Player
from game.game_board import CardAlreadyFlippedError
from game.game_board import CardAlreadyMatchedError
from game.game_board import PositionIsIncorrect
from game.memory_game import NotAbleToMatchError

def main():
    while True:
        print(
            "1. Start new game\n"
            "Q. Exit"
        )
        choice = input("> ").strip().upper()
        match choice:
            case "1":
                start_new_game()
            case "Q":
                print("Game exit")
                break
            case _:
                print(f"{choice} is invalid")
                continue

def start_new_game():
    players = add_players()

    while True:
        choice = input(
                "Size of board:\n" 
                "1. 2x3(easy)\n" 
                "2. 3x4(medium)\n" 
                "3. 4x5(hard)\n" 
                "4. 5x6(extreme)\n" 
                "> ").strip()
        match choice:
            case "1":
                size = (2, 3)
                break
            case "2":
                size = (3, 4)
                break
            case "3":
                size = (4, 5)
                break
            case "4":
                size = (5, 6)
                break
            case _:
                print("Invalid value, choose between 1-4")
                continue
        
    game = Memory_game(players, size)
    run_game(game)

def run_game(game:Memory_game):
    while not game.is_finished():
        lable = "first" if game.flipps_in_round == 0 else "second"
        player = game.players[game.current_player]
        print()
        print(f"{player.name}, pleace flip your {lable} card.")
        game.print_board()
        card_position = choose_position()

        try:
            game.try_flip(card_position)
        except (PositionIsIncorrect,
                CardAlreadyMatchedError, 
                CardAlreadyFlippedError
                ) as e:
            print(f"Error: {e}")

        if game.flipps_in_round < 2:
            continue
        
        print()
        game.print_board()
        try:
            if game.try_match():
                print("It's a match!")
            else:
                print("Sorry, not a match!")
        except NotAbleToMatchError as e:
            print(f"Error: {e}")

        game.set_next_round()
        
        print("-" * 30)
        if len(game.players) == 1:
            print(f"Attempts: {player.nbr_of_flipps}")
            print(f"Found pairs: {player.nbr_of_matches}")
        else:  
            print(f"{player.name}: {player.nbr_of_matches} pairs right now")
        print("-" * 30)        

        time.sleep(2.0)

    game.print_summary()
        
def add_players():
    while True:
        try:
            nbr_of_players = int(input("Number of players, 1-4?: "))
            if nbr_of_players < 0 or nbr_of_players > 4:
                print("1-4 players is allowed, please enter a valid number")
                continue
        except ValueError:
            print("Input an integer from 1 to 4")
            continue
        else:
            print("Enter name of players")
            players = []
            for i in range(nbr_of_players):
                player = Player(input(f"Player {i+1}: "))
                players.append(player)
            return players

def choose_position():
    """Ask user for column and row and validate input"""
    while True:
        try:
            col = int(input("Enter column: > ")) -1
            row = int(input("Enter row: > ")) -1
        except ValueError:
            print("Column and row needs to be positive integers")
            continue

        return (row, col)



if __name__ == "__main__":
    main()