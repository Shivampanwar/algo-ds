possible_options = [i for i in range(1, 10)]


def find_possible_options(matrix, row, col, n):
    temp_list = []
    for i in range(n):
        temp_list.append(matrix[row][i])
        temp_list.append(matrix[i][row])
    lower_bound_i = row - row % 3
    lower_bound_j = col - col % 3
    upper_bound_i = lower_bound_i + 2
    upper_bound_j = lower_bound_j + 2
    for i in range(lower_bound_i, upper_bound_i + 1):
        for j in range(lower_bound_j, upper_bound_j + 1):
            temp_list.append(matrix[i][j])
    return list(set(possible_options) - set(temp_list))


def findNexValOption(matrix, row, col, n):
    for i in range(row, n):
        for j in range(col, n):
            if matrix[i][j] == 0:
                return i, j


def sudoku(matrix, row, col, n):
    if row >= n - 1 and col >= n - 1:
        return True
    else:
        if matrix[row][col] == 0:
            possible = find_possible_options(matrix, row, col, n)
            print possible
            if len(possible) == 0:
                return False
            for i in possible:
                matrix[row][col] = i
                val_option = findNexValOption(matrix, row, col, n)
                print val_option
                sub_result = sudoku(matrix, val_option[0], val_option[1], n)
                if sub_result:
                    return True
            matrix[row][col] = 0
            return False
        else:
            val_option = findNexValOption(matrix, row, col, n)
            return sudoku(matrix, val_option[0], val_option[1], n)


input = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
         [2, 8, 9, 0, 0, 4, 0, 0, 0],
         [3, 4, 6, 2, 0, 5, 0, 9, 0],
         [6, 0, 2, 0, 0, 0, 0, 1, 0],
         [0, 3, 8, 0, 0, 6, 0, 4, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 7, 8],
         [7, 0, 3, 4, 0, 0, 5, 6, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
print sudoku(input, 0, 0, 9)
