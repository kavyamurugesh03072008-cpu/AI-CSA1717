def solve_queens(board, row):
    if row == 8:
        return True

    for col in range(8):
        safe = True

        for r in range(row):
            if (board[r] == col or
                abs(board[r] - col) == abs(r - row)):
                safe = False
                break

        if safe:
            board[row] = col

            if solve_queens(board, row + 1):
                return True

    return False


board = [-1] * 8

if solve_queens(board, 0):
    for row in range(8):
        print(" ".join(
            "Q" if board[row] == col else "-"
            for col in range(8)
        ))
else:
    print("No solution exists")
