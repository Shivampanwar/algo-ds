import sys

import numpy as np


def spiralPrint(m, n, a):
    k = 0;
    l = 0

    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''

    while (k < m and l < n):

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            # print(a[k][i], end = " ")
            sys.stdout.write(str(a[k][i]))
            sys.stdout.write(" ")

        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            # print(a[i][n - 1], end = " ")
            sys.stdout.write(str(a[i][n - 1]))
            sys.stdout.write(" ")

        n -= 1

        # Print the last row from
        # the remaining rows
        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                # print(a[m - 1][i], end = " ")
                sys.stdout.write(str(a[m - 1][i]))
                sys.stdout.write(" ")

            m -= 1

        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                # print(a[i][l], end = " ")
                sys.stdout.write(str(a[i][l]))
                sys.stdout.write(" ")

            l += 1


# Driver Code
# spiralPrint()


arr = list(int(i) for i in input().strip().split(' '))
row = arr[0] - 1
col = arr[1] - 1
new_arr = np.array(arr[2:]).reshape((row + 1, col + 1))
spiralPrint(row + 1, col + 1, new_arr)
