import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring  # 이름 설정을 위해 추가
import random  # AI를 위한 랜덤 선택

root = tk.Tk()
root.title("틱택토 게임")
root.geometry("400x500")

current_player = "X"
BOARD_SIZE = 3  # 기본 보드 크기
board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
scores = {"X": 0, "O": 0}  # X와 O의 점수 기록
player_names = {"X": "플레이어 1", "O": "플레이어 2"}  # 플레이어 이름 기록
theme = {"dark_mode": False}  # 기본 테마는 밝은 모드

def click_button(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col]["text"] = current_player
        if check_winner(current_player):
            scores[current_player] += 1  # 점수 업데이트
            messagebox.showinfo(
                "게임 종료", 
                f"{player_names[current_player]} 승리!\n점수: {player_names['X']} = {scores['X']}, {player_names['O']} = {scores['O']}"
            )
            reset_board()
        elif all(board[r][c] != "" for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)):
            messagebox.showinfo("게임 종료", "무승부!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            if current_player == "O":
                ai_move()

def ai_move():
    global current_player
    empty_cells = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = current_player
        buttons[row][col]["text"] = current_player
        if check_winner(current_player):
            scores[current_player] += 1  # 점수 업데이트
            messagebox.showinfo(
                "게임 종료", 
                f"{player_names[current_player]} 승리!\n점수: {player_names['X']} = {scores['X']}, {player_names['O']} = {scores['O']}"
            )
            reset_board()
        elif all(board[r][c] != "" for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)):
            messagebox.showinfo("게임 종료", "무승부!")
            reset_board()
        else:
            current_player = "X"

def reset_board():
    global board, current_player
    board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = "X"
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            buttons[r][c]["text"] = ""

def reset_scores():
    global scores
    scores = {"X": 0, "O": 0}  # 점수 초기화
    messagebox.showinfo("점수 초기화", "점수가 초기화되었습니다.")

def set_player_names():
    global player_names
    player_1 = askstring("플레이어 이름 설정", "플레이어 1의 이름을 입력하세요:")
    player_2 = askstring("플레이어 이름 설정", "플레이어 2의 이름을 입력하세요:")
    if player_1:
        player_names["X"] = player_1
    if player_2:
        player_names["O"] = player_2
    messagebox.showinfo("이름 설정 완료", f"플레이어 1: {player_names['X']}, 플레이어 2: {player_names['O']}")

def toggle_theme():
    global theme
    theme["dark_mode"] = not theme["dark_mode"]  # 테마 상태 전환
    if theme["dark_mode"]:
        root.configure(bg="black")
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                buttons[r][c].configure(bg="gray", fg="white")
        reset_btn.configure(bg="gray", fg="white")
        reset_score_btn.configure(bg="gray", fg="white")
        back_btn.configure(bg="gray", fg="white")
        messagebox.showinfo("테마 변경", "다크 모드가 활성화되었습니다.")
    else:
        root.configure(bg="white")
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                buttons[r][c].configure(bg="lightblue", fg="black")
        reset_btn.configure(bg="lightblue", fg="black")
        reset_score_btn.configure(bg="lightblue", fg="black")
        back_btn.configure(bg="lightblue", fg="black")
        messagebox.showinfo("테마 변경", "밝은 모드가 활성화되었습니다.")

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

    global reset_btn, reset_score_btn, back_btn

    reset_btn = tk.Button(root, text="게임 리셋", font=("Arial", 14), command=reset_board)
    reset_btn.grid(row=BOARD_SIZE, column=0, columnspan=BOARD_SIZE)

    reset_score_btn = tk.Button(root, text="점수 초기화", font=("Arial", 14), command=reset_scores)
    reset_score_btn.grid(row=BOARD_SIZE + 1, column=0, columnspan=BOARD_SIZE)

    back_btn = tk.Button(root, text="뒤로가기", font=("Arial", 14), command=go_back)
    back_btn.grid(row=BOARD_SIZE + 2, column=0, columnspan=BOARD_SIZE)

    # 다크 테마 버튼 추가
    theme_btn = tk.Button(root, text="다크 모드 전환", font=("Arial", 14), command=toggle_theme)
    theme_btn.grid(row=BOARD_SIZE + 3, column=0, columnspan=BOARD_SIZE)

    # 초기 점수 표시
    messagebox.showinfo("현재 점수", f"{player_names['X']} = {scores['X']}, {player_names['O']} = {scores['O']}")

def create_size_selection():
    tk.Label(root, text="보드 크기를 선택하세요", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="플레이어 이름 설정", font=("Arial", 14), command=set_player_names).pack(pady=5)
    tk.Button(root, text="3x3 보드", font=("Arial", 14), command=lambda: select_board_size(3)).pack(pady=5)
    tk.Button(root, text="4x4 보드", font=("Arial", 14), command=lambda: select_board_size(4)).pack(pady=5)
    tk.Button(root, text="5x5 보드", font=("Arial", 14), command=lambda: select_board_size(5)).pack(pady=5)

    # 다크 테마 버튼 추가
    tk.Button(root, text="다크 모드 전환", font=("Arial", 14), command=toggle_theme).pack(pady=5)

create_size_selection()
root.mainloop()
