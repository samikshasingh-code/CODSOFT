import tkinter as tk
from tkinter import messagebox
import math

# Track the scores of the player, AI, and draw count
player_score = 0
ai_score = 0
draw_score = 0

# Setting up the board - 9 empty slots
board = [' ' for _ in range(9)]

# Function to check if a player has won
def check_winner(b, player):
    # Possible winning positions (rows, columns, diagonals)
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    # Check each position to see if all three values match the player's symbol
    for pos in win_positions:
        if all(b[i] == player for i in pos):
            return True
    return False

# Function to check if the board is full (draw situation)
def is_draw(b):
    return ' ' not in b

# Get a list of available moves (empty spots)
def get_available_moves(b):
    return [i for i in range(9) if b[i] == ' ']

# Minimax algorithm to determine the best move for the AI
def minimax(b, depth, is_maximizing):
    # Check if the game is over (win or draw)
    if check_winner(b, 'O'):  # AI wins
        return 1
    elif check_winner(b, 'X'):  # Player wins
        return -1
    elif is_draw(b):  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        # Try every possible move for the AI
        for move in get_available_moves(b):
            b[move] = 'O'
            score = minimax(b, depth + 1, False)
            b[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        # Try every possible move for the player
        for move in get_available_moves(b):
            b[move] = 'X'
            score = minimax(b, depth + 1, True)
            b[move] = ' '
            best_score = min(score, best_score)
        return best_score

# Get AI's best move based on minimax
def ai_move():
    best_score = -math.inf
    best_move = None
    for i in get_available_moves(board):
        board[i] = 'O'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            best_move = i
    return best_move

# Function that gets called when the player clicks a button
def button_click(index):
    global player_score, ai_score, draw_score

    # Check if the spot is empty
    if board[index] == ' ':
        board[index] = 'X'  # Player makes a move
        buttons[index]['text'] = 'X'
        buttons[index]['state'] = 'disabled'

        # Check if player has won
        if check_winner(board, 'X'):
            player_score += 1
            update_score()
            messagebox.showinfo("Game Over", "You win! 🎉")
            reset_game()
            return
        # Check if the game is a draw
        elif is_draw(board):
            draw_score += 1
            update_score()
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
            return

        # AI makes a move
        ai_index = ai_move()
        board[ai_index] = 'O'
        buttons[ai_index]['text'] = 'O'
        buttons[ai_index]['state'] = 'disabled'

        # Check if AI has won
        if check_winner(board, 'O'):
            ai_score += 1
            update_score()
            messagebox.showinfo("Game Over", "AI wins! 💻")
            reset_game()
        # Check if the game is a draw
        elif is_draw(board):
            draw_score += 1
            update_score()
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()

# Reset the game and board for a new round
def reset_game():
    global board
    board = [' ' for _ in range(9)]  # Clear the board
    for btn in buttons:
        btn['text'] = ' '
        btn['state'] = 'normal'  # Enable all buttons

# Function to update and display the current score
def update_score():
    score_label.config(text=f"Player: {player_score}  |  AI: {ai_score}  |  Draws: {draw_score}")

# GUI setup with theme customization
root = tk.Tk()
root.title("Tic Tac Toe with Custom Theme")
root.config(bg="#f0f0f0")  # Set background color for window

# Custom font and styles
button_font = ('Helvetica', 18, 'bold')
score_font = ('Helvetica', 16, 'italic')

button_style = {
    "font": button_font,
    "bg": "#4CAF50",  # Green background
    "fg": "white",  # White text color
    "activebackground": "#45a049",  # Darker green on click
    "activeforeground": "white",
    "width": 5,
    "height": 2,
    "bd": 5,
    "relief": "raised"
}

# Create buttons for each spot on the board
buttons = []
for i in range(9):
    btn = tk.Button(root, text=' ', **button_style,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3, padx=10, pady=10)
    buttons.append(btn)

# Score label to display the ongoing scores
score_label = tk.Label(root, text="Player: 0  |  AI: 0  |  Draws: 0", font=score_font, bg="#f0f0f0", fg="#333")
score_label.grid(row=3, column=0, columnspan=3, pady=20)

# Start the GUI loop
root.mainloop()
