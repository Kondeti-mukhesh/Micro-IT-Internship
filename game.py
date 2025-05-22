import tkinter as tk
from tkinter import messagebox

current_palyer="X"
board=[" "]*9

def check_winner():
    win_combos=[
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)]
    
    for a,b,c in win_combos:
        if board[a]==board[b]==board[c] and board[a]!=" ":
            return board[a]
        
    if " " not in board:
        return "Draw"
    
    return None
def button_click(index):
    global current_palyer
    if board[index] ==" ":
        board[index] =current_palyer
        buttons[index].config(text=current_palyer, state="disabled")
        winner=check_winner()

        if winner:
            if winner =="Draw":
                messagebox.showinfo("Tic,Tac,Toe", "Its a draw!")
            else:
                messagebox.showinfo("Tic,Tac,Toe", f"Player {winner} wins!")
            reset_game()

        else:
            current_palyer ="O" if current_palyer =="X" else "X"

def reset_game():
    global board, current_palyer
    current_palyer="X"
    board=[" "]*9
    
    for button in buttons:
        button.config(text=" ", state="normal")

#for gui
root = tk.Tk()                               
root.title("Tic-Tac-Toe")                   

buttons = []                                 
for i in range(9):                          
    button = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)    
    buttons.append(button)                   

tk.Button(root, text="Restart Game", command=reset_game).grid(row=3, column=0, columnspan=3, pady=10)


root.mainloop() 

