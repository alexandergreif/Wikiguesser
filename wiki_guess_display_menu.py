from colorama import Fore, Style, init

import wiki_guess_game_function

init(autoreset=True)


def display_menu():
    """
    prints info texts to screen, start and end screen.
    """
    print(Fore.MAGENTA + "\n\nWelcome to Wikiguesser!")
    print("How good do you know the interests of other Wikipedia users? Let's have a try!")
    print("Whoever estimates better, how many views a random Wikipedia page has, wins the round.")
    print("Try to guess better than the other player and become a master Wikiguesser!")
    print("If Player 2 enters the same estimation as Player 1, Player 1 will win the point.")
    print(Fore.MAGENTA + "\nSo, how do you play Wikiguesser? Here you are:\n")
    print("Chose an uneven amount of rounds you want to compete against each other.")
    print("The Players take turns giving their estimates.")
    print("Pay close attention to when it's your turn and estimate better than your fellow player to win!")
    print("If you are new to Wikiguesser - just start a tutorial round to try it out!")

    #player setup
    player1 = input(Fore.MAGENTA + "\nPlayer 1, please insert your nickname:\n>>>> ")
    player2 = input(Fore.MAGENTA + "Player 2, please insert your nickname:\n>>>>  ")

    # Setup amount of rounds
    while True:
        try:
            num_rounds = int(input("Chose an uneven amount of rounds you want to play:\n>>>> "))
            if num_rounds > 0 and num_rounds % 2 == 1:
                print(f"Great! Lets play {num_rounds} rounds Wikiguesser.")
                break
            else:
                print("Please put in a uneven number of rounds greater than 0.\n>>>> ")
        except ValueError:
            print("Please choose a whole number as input.")

    while True:
        tutorial_choice = input(
            "Do you want to play the tutorial before starting? Enter Y for yes or N for no: ").strip().upper()
        if tutorial_choice == "Y":
            wiki_guess_game_function.tutorial(num_rounds, player1, player2)

            pass
            break
        elif tutorial_choice == "N":
            print("\nHoly! You are already a pro! Have fun with Wikiguesser!")
            break
        else:
            print("Sorry, invalid input! Pleas chose only Y or N and confirm with enter.")

    return {
        "player1": player1,
        "player2": player2,
        "num_rounds": num_rounds,
        "tutorial": tutorial_choice == "Y"
    }


if __name__ == "__main__":
    game_settings = display_menu()
    print("\nLet's go, Wikiguessers!:")
    print(game_settings)
