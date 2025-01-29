import statistics
from wiki_statistics_merged import get_article
from wiki_statistics_merged import get_statistics
from colorama import Fore, Style, init


def update_scoreboard(player_1_win, player1, player2):
    if player_1_win == True:
        score_board[player1] += 1
    else:
        score_board[player2] += 1


def game(num_rounds, player1, player2):
    global score_board
    score_board = {}
    score_board[player1] = 0
    score_board[player2] = 0
    for num in range(1, num_rounds + 1):
        game_round(num, player1, player2)

    if score_board[player1] > score_board[player2]:
        print(f"The winner is {player1} with {score_board[player1]} points. Congratulations!!!")
        print(f"{player2} scored {score_board[player2]} points. GG")
    else:
        print(f"The winner is {player2} with {score_board[player2]} points. Congratulations!!!")
        print(f"{player1} scored {score_board[player1]} points. GG")



def game_round(num, player1, player2):
    print(f"You are in round {num}")
    title, summary, url = get_article()
    stats = get_statistics(title)
    page_views = stats['views']
    print()
    print("_" * 79)
    print(f'Title: {title}')
    print(f'Summary: {summary}')
    print("_" * 79)
    while True:
        try:
            print()
            answer_player_1 = int(input(Fore.MAGENTA + f"{player1}, how many page views do you guess for this article?\n>>>>> "))
            break
        except ValueError:
            print("Put in a positive number.")
    while True:
        try:
            print()
            answer_player_2 = int(input(Fore.MAGENTA + f"{player2}, how many page views do you guess for this article?\n>>>>> "))
            break
        except ValueError:
            print("Put in a positive number.")

    player_1_win = abs(page_views - int(answer_player_1)) <= abs(page_views - int(answer_player_2))
    update_scoreboard(player_1_win, player1, player2)

    print()
    print(Fore.WHITE + f"Actual page views: {page_views}")

    if player_1_win == True:
        print(f"{player1} wins")
    else:
        print(f"{player2} wins")

    print("_" * 39)
    print("current scores:")
    print(f"{player1}: {score_board[player1]}\n{player2}: {score_board[player2]}")
    print("_" * 39)
    input(Fore.MAGENTA + f"Press enter to continue to round {num + 1}.\n>>>>")

def tutorial(num_rounds, player1, player2):
    print("You entered the tutorial mode.")
    game(num_rounds, player1, player2)
    print(f"You finished the tutorial mode.\n\n --- Game Starting ---")











