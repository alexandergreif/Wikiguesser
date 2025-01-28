def game_round(num):
    num = 3
    print(f"You are in round {num}")
    title, summary, url = statistics.get_article()
    get_statistics(url)
    print(title)
    print(summary)
    answer_player_1 = input(f"{username1}, how many page views do you guess for this article?")
    answer_player_2 = input(f"{username2}, how many page views do you guess for this article?")
    player_1_win = abs(page_views - int(answer_player_1)) <= abs(page_views - int(answer_player_2))
    update_scoreboard(player_1_win)

    if player_1_win == True:
        print(f"{username1} wins")
    else:
        print(f"{username2} wins")

    print(score_board)
