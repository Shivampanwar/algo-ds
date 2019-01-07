import sys

import numpy as np


def wave(new_array):
    row, column = new_array.shape[0], new_array.shape[1]
    count = 0  # for columns
    i = 0  ##for row
    while count < column:
        counter = False
        if not counter:
            if i == 0:
                counter = True
                while i < row:
                    sys.stdout.write(str(new_array[i][count]))
                    sys.stdout.write(" ")
                    i += 1
                i += -1
        if not counter:
            if i == row - 1:
                while i > -1:
                    sys.stdout.write(str(new_array[i][count]))
                    sys.stdout.write(" ")
                    i += -1
                i += 1
        count += 1


n = int(input())
m = int(input())
arr = list(int(i) for i in input().strip().split(' '))

newarr = np.array(arr).reshape((n, m))
print newarr
wave(newarr)
