def find_possible_options(available, col, n):
    possible_options = []
    row = 0
    while row < n:
        if available[row][col] == 0:
            possible_options.append((row, col))
        row += 1
    return possible_options


def change_matrix(available, row, col, n):
    for i in range(n):
        available[row][i] == 1
    for i in range(n):
        available[i][col] == 1
    i = row - 1
    j = col + 1


def NQueen(available, row, col, n):
    pass


board = [[0, 0, 0, 1],
         [0, 0, 1, 0],
         [0, 1, 0, 0],
         [1, 0, 0, 0]]
print find_possible_options(board, 1, 4)
