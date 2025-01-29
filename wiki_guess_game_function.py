import statistics
from wiki_statistics_merged import get_article
from wiki_statistics_merged import get_statistics

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
    print(title)
    print(summary)
    while True:
        try:
            answer_player_1 = int(input(f"{player1}, how many page views do you guess for this article?"))
            break
        except ValueError:
            print("Put in a positive number.")
    while True:
        try:
            answer_player_2 = int(input(f"{player2}, how many page views do you guess for this article?"))
            break
        except ValueError:
            print("Put in a positive number.")

    player_1_win = abs(page_views - int(answer_player_1)) <= abs(page_views - int(answer_player_2))
    update_scoreboard(player_1_win, player1, player2)

    if player_1_win == True:
        print(f"{player1} wins")
    else:
        print(f"{player2} wins")
    print(f"Actual page views: {page_views}")
    print(score_board)
    input("Press enter to continue")

def tutorial(num_rounds, player1, player2):
    print("You entered the tutorial mode.")
    game(num_rounds, player1, player2)
    print(f"You finished the tutorial mode.\n\n --- Game Starting ---")











