def game(num_rounds, username1, username2):
    global score_board
    score_board = {}
    score_board[username1] = 20
    score_board[username2] = 100
    for num in range(1, num_round + 1):
        game_round(num)

    if score_board[username1] > score_board[username2]:
        print(f"The winner is {username1} with {score_board[username1]} points. Congratulations!!!")
        print(f"{username2} scored {score_board[username2]} points. GG")
    else:
        print(f"The winner is {username2} with {score_board[username2]} points. Congratulations!!!")
        print(f"{username1} scored {score_board[username1]} points. GG")


