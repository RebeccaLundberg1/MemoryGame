from game.memory_game import Memory_game

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
        game.print_board()
        row = int(input("Enter row for card to flip: > ")) -1
        col = int(input("Enter row for card to flip: > ")) -1
        game.flip(row, col)
        

if __name__ == "__main__":
    main()