from game.memory_game import Memory_game
import time
from game.player import Player
from game.exceptions import GameError, NotAbleToMatchError
import os
import json

def main():
    while True:
        print(
            "1. Start new game\n"
            "2. Open latest game\n"
            "Q. Exit"
        )
        choice = input("> ").strip().upper()
        match choice:
            case "1":
                start_new_game()
            case "2":
                if os.path.exists("savegame.json"):
                    with open("savegame.json", "r") as f:
                        data = json.load(f)
                else:
                    print("Ingen sparad fil hittades.")
                    continue
                game = Memory_game(data["size"])
                game.update_latest_game(data)
                run_game(game) 
            case "Q":
                print("Game exit")
                break
            case _:
                print(f"{choice} is invalid")
                continue

def start_new_game():
    players = add_players()

    while True:
        print()
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
        
    game = Memory_game(size, players)
    run_game(game)

def run_game(game:Memory_game):
    clear_screen()
    while not game.is_finished():
        lable = "first" if game.flipps_in_round == 0 else "second"
        player = game.players[game.current_player]
        print()
        print(f"{player.name}, pleace flip your {lable} card. (Select column 0, and row 0 to save and exit game)")
        game.print_board()
        card_position = choose_position()

        if card_position == (-1, -1):
            break
        
        try:
            game.try_flip(card_position)
        except (GameError) as e:
            print(f"Error: {e}")

        clear_screen() 

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

        time.sleep(3.0)
        clear_screen()

    if game.is_finished():
        game.print_summary()
        # Spara resultat? Om en spelare till någon topplista? Om flera spelare, inte spara alls om spelet är slut?
    else:
        with open("savegame.json", "w") as f:
            json.dump(game.to_dict(), f, indent=4)
        print("The game is saved, welcome back!")
        
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
    """Ask user for column and row"""
    while True:
        try:
            col = int(input("Enter column: > ")) -1
            row = int(input("Enter row: > ")) -1               
        except ValueError:
            print("Column and row needs to be positive integers")
            continue

        return (row, col)
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()