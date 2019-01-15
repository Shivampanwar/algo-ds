import sys

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


b = rotate_matrix(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 3)
for i in range(3):
    for j in range(3):
        sys.stdout.write(str(b[i][j]))
        sys.stdout.write(" ")
    print ("\n")
x = [1, 2, 3, 4, 5, 6]
print np.reshape(x, (3, 2))
