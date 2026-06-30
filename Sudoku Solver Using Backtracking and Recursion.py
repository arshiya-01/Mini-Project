# Sudoku Solver Using Backtracking and Recursion

def print_board(board):
    print("\nSolved Sudoku Puzzle:\n")
    for row in board:
        print(" ".join(str(num) for num in row))


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve(board):
    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            # Backtracking
            board[row][col] = 0

    return False


def main():

    sudoku = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]

    print("========== SUDOKU SOLVER ==========\n")
    print("Input Puzzle (0 = Empty Cell)\n")

    for row in sudoku:
        print(row)

    if solve(sudoku):
        print_board(sudoku)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()