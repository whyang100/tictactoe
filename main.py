def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# 초기화된 빈 보드
board = [[" " for _ in range(3)] for _ in range(3)]
print_board(board)
def player_input(board, player):
    while True:
        try:
            row = int(input(f"플레이어 {player}, 행(0-2)을 입력하세요: "))
            col = int(input(f"플레이어 {player}, 열(0-2)을 입력하세요: "))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("이미 채워진 위치입니다. 다시 선택하세요.")
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 0에서 2 사이의 숫자를 입력하세요.")
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    players = ["X", "O"]
    turn = 0

    while True:
        current_player = players[turn % 2]
        player_input(board, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"플레이어 {current_player}가 승리했습니다!")
            break
        elif all(cell != " " for row in board for cell in row):
            print("무승부입니다!")
            break
        turn += 1

if __name__ == "__main__":
    main()
