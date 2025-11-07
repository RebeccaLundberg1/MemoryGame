from game.memory_game import Memory_game

def main():
    print(
        "1. Starta nytt spel\n"
        "Q. Avsluta"
    )
    choice = input("> ")
    match choice:
        case "1":
            name = input("Ange spelarens namn:\n> ")
            game_choice = input(
                "Spelbräde:\n" \
                "1. 2x3(easy)\n" \
                "2. 3x4(medium)\n" \
                "3. 4x5(hard)\n" \
                "4. 6x5(extreme)\n" \
                "> ")
            if game_choice == "1":
                size = (2, 3)
            elif game_choice == "2":
                size = (3, 4)
            elif game_choice == "3":
                size = (4, 5)
            elif game_choice == "4":
                size = (5, 6)
            else:
                size = (2, 3)
            
            game = Memory_game(name, size)
            run_game(game)

        case "Q":
            print("Spelet avslutas, dina resultat sparas")
            #Spara här?
            exit()
        case _:
            print(f"{choice} is invalid")


def run_game(game:Memory_game):
    pass





if __name__ == "__main__":
    main()