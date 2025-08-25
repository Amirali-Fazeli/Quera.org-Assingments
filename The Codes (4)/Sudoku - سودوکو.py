def sudoku_game(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = " ")
        print()
def zero_founded(board, element):
    for row in range(9):
        for col in range(9):
            if (board[row][col] == 0):
                element[0] = row
                element[1] = col
                return True
    return False

def sudoku_row(board, row, number):
    for i in range(9):
        if (board[row][i] == number):
            return True
    return False

def sudoku_col(board, col, number):
    for i in range(9):
        if (board[i][col] == number):
            return True
    return False

def sudoku_3_3(board, row, col, number):
    for i in range(3):
        for j in range(3):
            if (board[i + row][j + col] == number):
                return True
    return False

def correct(board, row, col, number):

    return (not sudoku_row(board, row, number) and
            (not sudoku_col(board, col, number) and (not sudoku_3_3(board, row - row % 3, col - col % 3, number))))

def sudoku(board):
    element = [0, 0]
    if (not zero_founded(board, element)):
        return True
    row = element[0]
    col = element[1]
    for num in range(1, 10):
        if (correct(board, row, col, num)):
            board[row][col] = num
            if (sudoku(board)):
                return True
            board[row][col] = 0

    return False

game_1 = [[0 for a in range(9)] for b in range(9)]
for _ in range(9):
    _ = list(map(int, input().split()))
    game_1.append(_)

if (sudoku(game_1)):
    sudoku_game(game_1)

