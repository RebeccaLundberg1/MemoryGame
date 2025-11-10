from game.memory_game import Memory_game
import time
from game.game_board import CardAlreadyFlippedError
from game.game_board import CardAlreadyMatchedError
from game.game_board import PositionIsIncorrect

def main():
    while True:
        print(
            "1. Starta nytt spel\n"
            "Q. Avsluta"
        )
        choice = input("> ").strip().upper()
        match choice:
            case "1":
                start_new_game()
            case "Q":
                print("Spelet avslutas, dina resultat sparas")
                #Spara här?
                break
            case _:
                print(f"{choice} is invalid")
                continue

def start_new_game():
    name = input("Ange spelarens namn:\n> ")
    choice = input(
            "Spelbräde:\n" \
            "1. 2x3(easy)\n" \
            "2. 3x4(medium)\n" \
            "3. 4x5(hard)\n" \
            "4. 5x6(extreme)\n" \
            "> ").strip()
    match choice:
        case "1":
            size = (2, 3)
        case "2":
            size = (3, 4)
        case "3":
            size = (4, 5)
        case "4":
            size = (5, 6)
        case _:
            print("Ogiltigt värde, spelplan 2x3 startas...")
            size = (2, 3)
        
    game = Memory_game(name, size)
    run_game(game)

def run_game(game:Memory_game):
    while not game.is_finished():
        lable = "first" if game.flipps_in_round == 0 else "second"
        print(f"Please flip your {lable} card.")
        game.print_board()
        card_position = choose_position()

        try:
            game.try_flip(card_position)
        except (CardAlreadyMatchedError, CardAlreadyFlippedError, PositionIsIncorrect) as e:
            print(f"Error: {e}")

        if game.flipps_in_round < 2:
            continue
        
        game.print_board()
        if game.try_match():
            print("It's a match!")
        else:
            print("Sorry, not a match!")

        game.set_next_round()
        
        print("-" * 30)
        print(f"Attempts: {game.nbr_of_flipps}")
        print(f"Found pairs: {game.nbr_of_matches}")
        print("-" * 30)        

        time.sleep(2.0) #Kanske fler sleeps genom spelet för läsbarheten? 
        
def choose_position():
    """Ask user for column and row and validate input"""
    while True:
        try:
            col = int(input("Enter column: > ")) -1
            row = int(input("Enter row: > ")) -1
            if col < 0 and row < 0:
               print("Column and row needs to be positive integers")
               continue
            return (row, col)
        except ValueError:
            print("Column and row needs to be positive integers")
            continue

if __name__ == "__main__":
    main()