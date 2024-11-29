import tkinter as tk
from tkinter import messagebox

# Tkinter 창 생성
root = tk.Tk()
root.title("틱택토 게임")
root.geometry("300x300")  # 창 크기 설정

# 실행 루프
root.mainloop()
current_player = "X"  # 현재 플레이어
board = [["" for _ in range(3)] for _ in range(3)]  # 보드 초기화

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

def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = ""

def check_winner(player):
    # 가로, 세로, 대각선 확인
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# 버튼 생성
buttons = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text="", font=("Arial", 20), height=2, width=5,
                                  command=lambda row=r, col=c: click_button(row, col))
        buttons[r][c].grid(row=r, column=c)
def add_reset_button():
    reset_btn = tk.Button(root, text="게임 리셋", font=("Arial", 14), command=reset_board)
    reset_btn.grid(row=3, column=0, columnspan=3)

# 게임 리셋 버튼 추가
add_reset_button()
buttons[r][c] = tk.Button(root, text="", font=("Arial", 20), height=2, width=5,
                          bg="lightblue", command=lambda row=r, col=c: click_button(row, col))
