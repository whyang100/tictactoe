def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# 초기화된 빈 보드
board = [[" " for _ in range(3)] for _ in range(3)]
print_board(board)
