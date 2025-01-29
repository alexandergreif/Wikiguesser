from wiki_guess_display_menu import display_menu
from wiki_guess_game_function import game


def replay_game(num_rounds, player1, player2):
    """Replay the game with the same players and rounds."""
    print("\nReplaying the game with the same players...")
    game(num_rounds, player1, player2)


def new_game():
    """Start a new game with new players."""
    print("\nStarting a new game...")
    settings = display_menu()
    game(settings['num_rounds'], settings['player1'], settings['player2'])


def quit_game():
    """Quit the game."""
    print("\nThanks for playing Wikiguesser! Goodbye!")
    exit()


if __name__ == "__main__":
    # Display the menu and collect initial settings
    settings = display_menu()
    game(settings['num_rounds'], settings['player1'], settings['player2'])

    # Define the function dictionary
    func_dict = {
        "1": lambda: replay_game(settings['num_rounds'], settings['player1'], settings['player2']),
        "2": new_game,
        "3": quit_game
    }

    # Loop to offer replay options
    while True:
        print("_" * 39)
        choice = input("\nChoose an option:\n1 to replay with the same players.\n2 for a new game.\n3 to quit the game.\nEnter your choice: ").strip()
        if choice in func_dict:
            func_dict[choice]()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
