import heapq
from game.memoryGame import MemoryGame, update_latest_game
import time
from game.player import Player
from game.exceptions import GameError, NotAbleToMatchError
import os
from services.file_service import FileType, read_db, write_db

def main():
    start_menu()

def start_menu() -> None:
    """
    Print start menu and handle the user selection
    
    The user can start new game, continue the latest game (if one exists),
    or view single-player high scores for each game level
    """
    while True:
        print(
            "1. Start new game\n"
            "2. Continue latest game\n"
            "3. View single-player high scores\n"
            "Q. Exit"
        )
        choice = input("> ").strip().upper()

        match choice:
            case "1":
                players = add_players()
                print()
                size = choose_board_size()
                game = MemoryGame(size, players)
                run_game(game)

            case "2":
                saved_game = read_db(FileType.SAVE)
                if saved_game:
                    game = update_latest_game(saved_game)
                    players_in_game = " & ".join([p.name for p in game.players])
                    clear_screen()
                    print(f"Welcome back {players_in_game}!")
                    time.sleep(2.0)
                    run_game(game)
                else:
                    print("No saved game is found")
                    continue

            case "3":
                toplist = read_db(FileType.TOPLIST)
                for key in toplist:
                    print(f"{key}: ")
                    for i, (flipps, player) in enumerate(sorted(toplist[key], reverse=False), start = 1):
                        print(f"{i}. {player} - {flipps} attempts")
                    print()

            case "Q":
                print("Program exits")
                break

            case _:
                print(f"{choice} is invalid")
                continue

def add_players() -> list:
    """
    Add chosen number of players to game
    
    The user selects the number of players in game (1-4), enters name to each 
    player and a Player object in created and appended to list, which is returned
    """
    while True:
        try:
            nbr_of_players = int(input("Number of players, 1-4?: "))
            if not (1 <= nbr_of_players <= 4):
                print("1-4 players is allowed, please enter a valid number")
                continue
        except ValueError:
            print("Input an integer from 1 to 4")
            continue
        else:
            print("Enter name of players")
            players = []
            for i in range(nbr_of_players):
                while True:
                    try:
                        player = Player(input(f"Player {i+1}: ").strip().title())
                    except ValueError as e:
                        print(f"Error: {e}")
                    else: 
                        players.append(player)
                        break
            return players

def choose_board_size() -> tuple:
    """
    Show available board sizes and let the user to select one
    
    Returns:
        tuple[int, int]: the chosen board size as (rows, columns)
    """
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
                return (2, 3)
            case "2":
                return (3, 4)
            case "3":
                return (4, 5)
            case "4":
                return (5, 6)
            case _:
                print("Invalid value, choose between 1-4")
                continue

def run_game(game:MemoryGame) -> None:
    """
    Guide the player through the game until it is finished or exited.

    Handles flipping cards, checks if it is a match, view current state of the board
    between each move and print out pairs and attempts of current player for each
    round.

    Args:
        game(MemoryGame): a MemoryGame object
    """
    while not game.is_finished():
        clear_screen()
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
            time.sleep(1.5)

        if game.flipps_in_round < 2:
            continue
        
        clear_screen()
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
        print()    

        time.sleep(2.5)
    end_game(game)

def choose_position() -> tuple:
    """
    Handle column and row input from user
    
    The user enters column and row using 1-based indices.
    
    Returns: 
        tuple[int, int]: the selected cell coordinates (row, column). """
    while True:
        try:
            col = int(input("Enter column: > ")) - 1
            row = int(input("Enter row: > ")) - 1               
        except ValueError:
            print("Column and row needs to be positive integers")
            continue

        return (row, col)
    
def end_game(game: MemoryGame) -> None:
    """
    Handles the end of MemoryGame.
    
    If game is finished:
        Single-player game result will updated to the toplist. 
        Summary of the results print out
    If game is not completed:
        Player will be given the choice of saving their game to next time. 
        (Only the most recent saved game can be resumed)

    Args:
        game(MemoryGame): a MemoryGame object
    """
    if game.is_finished():
        if len(game.players) == 1:
            if update_toplist(game):
                print("***Check the highscore to see if you made the list!***")
        game.print_summary()
    else:
        while True:
            save = input("The game is unfinished, would you like to save "  
                         "it for next time (YES/NO)?: ").strip().upper()
            if save == "YES":
                write_db(game.to_dict(), FileType.SAVE)
                print("The game is saved, welcome back!")
                break
            elif save == "NO":
                print("See you next time!")
                break
            else:
                print("Invalid choice, please enter 'YES' or 'NO'")

def update_toplist(game: MemoryGame) -> bool:
    """
    Update toplist if it's a finished single-player game

    Loads the toplist, determines the size of completed game, and uses heapq  to
    add player and result if it's among the top 3 score. The updated list is then saved. 

    Returns: 
        bool: True if toplist was updated and saved, False otherwise.    
    """
    if not game.is_finished():
        return False
    
    if len(game.players) != 1:
        return False
    
    toplist = read_db(FileType.TOPLIST)

    match game.size:
        case (2, 3):
            level = "easy"
        case (3, 4):
            level = "medium"            
        case (4, 5):
            level = "hard"
        case (5, 6):
            level = "extreme"
    
    current_toplist = toplist[level]
    nbr_of_flipps = game.players[0].nbr_of_flipps
    player_name = game.players[0].name

    current_toplist.append([nbr_of_flipps, player_name])
    current_toplist.sort()
    toplist[level] = current_toplist[:3]
        
    write_db(toplist, FileType.TOPLIST)
    return True

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()