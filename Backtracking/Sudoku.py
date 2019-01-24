possible_options = [i for i in range(1, 10)]
def find_possible_options(matrix, row, col, n):
    temp_list = []
    temp_list.extend(matrix[row])
    for i in range(n):
        temp_list.append(matrix[i][col])
    lower_bound_i = row - row % 3
    lower_bound_j = col - col % 3
    upper_bound_i = lower_bound_i + 2
    upper_bound_j = lower_bound_j + 2
    for i in range(lower_bound_i, upper_bound_i + 1):
        for j in range(lower_bound_j, upper_bound_j + 1):
            temp_list.append(matrix[i][j])
    return list(set(possible_options) - set(temp_list))


def findNexValOption(matrix, row, col, n):
    for i in range(col, n):
        if matrix[row][i] == 0:
            return row, i
    for i in range(row + 1, n):
        for j in range(0, n):
            if matrix[i][j] == 0:
                return i, j
    return -1, -1


def sudoku(matrix, row, col, n):
    val_i, val_j = findNexValOption(matrix, row, col, n)
    if val_i >= n - 1 and val_j >= n - 1:
        return True
    if val_i == -1 and val_j == -1:
        return True
    else:
        options = find_possible_options(matrix, val_i, val_j, n)
        if len(options) == 0:
            return False
        else:
            for i in options:
                matrix[val_i][val_j] = i
                x, y = findNexValOption(matrix, val_i, val_j, n)
                result = sudoku(matrix, x, y, n)
                if result:
                    return True
            matrix[val_i][val_j] = 0
            return False


# big_array=[]
# for i in range(9):
#     arr = list(int(i) for i in input().strip().split(' '))
#     big_array.append(arr)
# print (sudoku(big_array,0,0,9))

data1 = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
         [2, 8, 9, 0, 0, 4, 0, 0, 0],
         [3, 4, 6, 2, 0, 5, 0, 9, 0],
         [6, 0, 2, 0, 0, 0, 0, 1, 0],
         [0, 3, 8, 0, 0, 6, 0, 4, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 7, 8],
         [7, 0, 3, 4, 0, 0, 5, 6, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
#
data = "9 0 0 0 2 0 7 5 0 6 0 0 0 5 0 0 4 0 0 2 0 4 0 0 0 1 0 2 0 8 0 0 0 0 0 0 0 7 0 5 0 9 0 6 0 0 0 0 0 0 0 4 0 1 0 1 0 0 0 5 0 8 0 0 9 0 0 7 0 0 0 4 0 8 2 0 4 0 0 0 6"
arr = list(int(i) for i in data.strip().split(' '))
new_list = []
j = 0
for i in range(9):
    new_list.append(arr[j:j + 9])
    j += 9

print sudoku(new_list, 0, 0, 9)
# print find_possible_options(grid,8,8,9)
