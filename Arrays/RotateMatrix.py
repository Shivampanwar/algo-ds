import numpy as np


def rotate_matrix(a, n):
    i = 0
    for j in range(n - 1):
        next_index_i = n - j - 1
        next_index_j = i
        temp = a[i][j]
        for k in range(4):
            temp, a[next_index_i][next_index_j] = a[next_index_i][next_index_j], temp
            next_index_i, next_index_j = n - next_index_j - 1, next_index_i
    return a


x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print x
b = rotate_matrix(x, 4)
print b
