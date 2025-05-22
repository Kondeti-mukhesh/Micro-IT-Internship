import tkinter as tk
from tkinter import messagebox
import platform

if platform.system() == 'Windows':
    import winsound

current_player = "X"
board = [" "] * 9

def play_sound(frequency=500, duration=100):
    if platform.system() == 'Windows':
        winsound.Beep(frequency, duration)

def check_winner():
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

def update_status():
    status_label.config(text=f"Current Player: {current_player}", fg="pink")

def disable_all_buttons():
    for button in buttons:
        button.config(state="disabled")

def button_click(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player

        # Set fg and bg, also set disabledforeground to keep color visible when disabled
        fg_color = "blue" if current_player == "X" else "yellow"
        buttons[index].config(
            text=current_player,
            fg=fg_color,
            bg="black",
            disabledforeground=fg_color,
            state="disabled"
        )

        play_sound(700, 100)  # click sound

        winner = check_winner()

        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
                play_sound(1000, 300)  # win sound
            disable_all_buttons()  # stop the game, wait for manual restart
        else:
            current_player = "O" if current_player == "X" else "X"
            update_status()

def reset_game():
    global board, current_player
    current_player = "X"
    board = [" "] * 9
    for button in buttons:
        button.config(
            text=" ",
            fg="black",     
            bg="black",
            state="normal",
            disabledforeground="black"
        )
    update_status()

root = tk.Tk()
root.title("Tic-Tac-Toe")

status_label = tk.Label(root, text=f"Current Player: {current_player}", font=("Arial", 16), fg="blue", bg="black")
status_label.grid(row=0, column=0, columnspan=3, pady=10)

buttons = []
for i in range(9):
    button = tk.Button(
        root, text=" ", font=("Arial", 20), width=5, height=2,
        bg="black", fg="black",
        activeforeground="yellow",  
        disabledforeground="black",
        command=lambda i=i: button_click(i)
    )
    button.grid(row=(i // 3) + 1, column=i % 3)
    buttons.append(button)

tk.Button(root, text="Restart Game", bg="sky blue", fg="black", command=reset_game).grid(row=4, column=0, columnspan=3, pady=10)

root.configure(bg="black")  # window bg black

root.mainloop()
