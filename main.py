import tkinter as tk
from tkinter import messagebox
import random  # AI를 위한 랜덤 선택

root = tk.Tk()
root.title("틱택토 게임")
root.geometry("400x400")

current_player = "X"
BOARD_SIZE = 3  # 기본 보드 크기
board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def click_button(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col]["text"] = current_player
        if check_winner(current_player):
            messagebox.showinfo("게임 종료", f"플레이어 {current_player} 승리!")
            reset_board()
        elif all(board[r][c] != "" for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)):
            messagebox.showinfo("게임 종료", "무승부!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            if current_player == "O":  # AI 차례
                ai_move()

def ai_move():
    global current_player
    empty_cells = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = current_player
        buttons[row][col]["text"] = current_player
        if check_winner(current_player):
            messagebox.showinfo("게임 종료", f"플레이어 {current_player} 승리!")
            reset_board()
        elif all(board[r][c] != "" for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)):
            messagebox.showinfo("게임 종료", "무승부!")
            reset_board()
        else:
            current_player = "X"  # AI가 동작 후 플레이어 차례로 전환

def check_winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True
    return False

def reset_board():
    global board, current_player
    board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = "X"
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            buttons[r][c]["text"] = ""

def go_back():
    for widget in root.winfo_children():
        widget.destroy()
    create_size_selection()

def select_board_size(size):
    global BOARD_SIZE, board, buttons
    BOARD_SIZE = size
    board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for widget in root.winfo_children():
        widget.destroy()
    create_game_board()

def create_game_board():
    global buttons
    buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            buttons[r][c] = tk.Button(root, text="", font=("Arial", 20), height=2, width=5,
                                      bg="lightblue", command=lambda row=r, col=c: click_button(row, col))
            buttons[r][c].grid(row=r, column=c)

    reset_btn = tk.Button(root, text="게임 리셋", font=("Arial", 14), command=reset_board)
    reset_btn.grid(row=BOARD_SIZE, column=0, columnspan=BOARD_SIZE)

    back_btn = tk.Button(root, text="뒤로가기", font=("Arial", 14), command=go_back)
    back_btn.grid(row=BOARD_SIZE + 1, column=0, columnspan=BOARD_SIZE)

def create_size_selection():
    tk.Label(root, text="보드 크기를 선택하세요", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="3x3 보드", font=("Arial", 14), command=lambda: select_board_size(3)).pack(pady=5)
    tk.Button(root, text="4x4 보드", font=("Arial", 14), command=lambda: select_board_size(4)).pack(pady=5)
    tk.Button(root, text="5x5 보드", font=("Arial", 14), command=lambda: select_board_size(5)).pack(pady=5)

create_size_selection()
root.mainloop()
