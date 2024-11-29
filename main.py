import tkinter as tk
from tkinter import messagebox
import random  # 랜덤 선택을 위해 추가

def ai_move():
    global current_player
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = current_player
        buttons[row][col]["text"] = current_player
        if check_winner(current_player):
            messagebox.showinfo("게임 종료", f"플레이어 {current_player} 승리!")
            reset_board()
        elif all(board[r][c] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("게임 종료", "무승부!")
            reset_board()
        else:
            current_player = "X"  # AI가 끝난 후 플레이어로 전환


root = tk.Tk()
root.title("틱택토 게임")
root.geometry("300x350")

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

def click_button(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col]["text"] = current_player
        if check_winner(current_player):
            messagebox.showinfo("게임 종료", f"플레이어 {current_player} 승리!")
            reset_board()
        elif all(board[r][c] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("게임 종료", "무승부!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            if current_player == "O":
                ai_move()  # AI가 자동으로 움직임


def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = ""

def check_winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

buttons = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text="", font=("Arial", 20), height=2, width=5,
                                  bg="lightblue", command=lambda row=r, col=c: click_button(row, col))
        buttons[r][c].grid(row=r, column=c)

reset_btn = tk.Button(root, text="게임 리셋", font=("Arial", 14), command=reset_board)
reset_btn.grid(row=3, column=0, columnspan=3)

root.mainloop()
