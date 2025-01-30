
# 📖 Wikiguesser - Technical Documentation

## 🚀 Overview
**Wikiguesser** is a Python-based game where players guess how many views a randomly selected Wikipedia article has. This documentation provides a detailed overview of the project's structure, as well as inputs, outputs, and function descriptions.

---

## 📂 Project Structure
```
wikiguesser/
│── main.py                        # Main control of the game
│── wiki_guess_display_menu.py     # User interaction menu
│── wiki_guess_game_function.py    # Game logic and scoring system
│── wiki_statistics_merged.py      # Wikipedia data queries
│── README.md                      # Technical documentation
```

---

## 🔧 Function Descriptions

### **1️⃣ main.py**
#### **Function: `new_game()`**
- **Description**: Starts a new game with new players and settings.
- **Inputs**:
  - Calls `display_menu()` to get player and game settings.
- **Outputs**:
  - Passes the settings to `game()` in `wiki_guess_game_function.py`.

#### **Function: `replay_game(num_rounds, player1, player2)`**
- **Description**: Replays the game with the same players and round settings.
- **Inputs**:
  - `num_rounds` (int): Number of rounds.
  - `player1` (str): Name of the first player.
  - `player2` (str): Name of the second player.
- **Outputs**:
  - Calls `game()` again with the same players and settings.

#### **Function: `quit_game()`**
- **Description**: Quits the game.
- **Inputs**: None.
- **Outputs**: Closes the program.

---

### **2️⃣ wiki_guess_display_menu.py**
#### **Function: `display_menu()`**
- **Description**: Displays the game's main menu and collects user inputs.
- **Inputs**:
  - Player names (str): Nicknames of the players.
  - Number of rounds (int): Odd number of rounds.
  - Tutorial option (bool): Whether the tutorial should be played.
- **Outputs**:
  ```python
  {
      "player1": (str),
      "player2": (str),
      "num_rounds": (int),
      "tutorial": (bool)
  }
  ```

---

### **3️⃣ wiki_guess_game_function.py**
#### **Function: `game(num_rounds, player1, player2)`**
- **Description**: Runs the entire game, manages rounds, and calculates the winner.
- **Inputs**:
  - `num_rounds` (int): Number of rounds.
  - `player1` (str): Name of the first player.
  - `player2` (str): Name of the second player.
- **Outputs**:
  - Displays the game results and the winner.

#### **Function: `update_scoreboard(player_1_win, player1, player2)`**
- **Description**: Updates the scoreboard based on the round results.
- **Inputs**:
  - `player_1_win` (bool): Indicates if player 1 won the round.
  - `player1` (str): Name of the first player.
  - `player2` (str): Name of the second player.
- **Outputs**:
  - Updated scoreboard.

#### **Function: `game_round(num, player1, player2)`**
- **Description**: Conducts a single round of the game.
- **Inputs**:
  - `num` (int): Current round number.
  - `player1` (str): Name of the first player.
  - `player2` (str): Name of the second player.
- **Outputs**:
  - Player scores are updated.
  - Round results are displayed in the console.

---

### **4️⃣ wiki_statistics_merged.py**
#### **Function: `get_article()`**
- **Description**: Fetches a random Wikipedia article.
- **Inputs**: None.
- **Outputs**:
  ```python
  (title: str, summary: str, url: str)
  ```

#### **Function: `get_statistics(title)`**
- **Description**: Retrieves page views and edit history of an article.
- **Inputs**:
  - `title` (str): Title of the Wikipedia article.
- **Outputs**:
  ```python
  {
      "views": (int),
      "edits": (int)
  }
  ```

---

## 🛠️ Installation & Execution

### **Requirements**
- **Python 3.x** must be installed.
- **Dependencies**:
  ```sh
  pip install wikipedia-api colorama requests
  ```

### **Start the Game**
1. Clone the repository:
   ```sh
   git clone https://github.com/alexandergreif/Wikiguesser
   cd wikiguesser
   ```
2. Run the game:
   ```sh
   python main.py
   ```

---

## 🌟 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
