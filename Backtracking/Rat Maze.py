import sys


def print_solution(soln, n):
    print ("Solution is ")
    for i in range(n):
        for j in range(n):
            sys.stdout.write(str(soln[i][j]) + " ")
        print ("\n")


def hasPath(data, x, y, n, soln):
    if x == n - 1 and y == n - 1:
        print_solution(soln, n)
        return
    if x < 0 or y < 0 or x >= n or y >= n or data[x][y] == 0 or soln[x][y] == 1:
        return
    soln[x][y] = 1
    hasPath(data, x - 1, y, n, soln)
    hasPath(data, x, y - 1, n, soln)
    hasPath(data, x + 1, y, n, soln)
    hasPath(data, x, y + 1, n, soln)
    soln[x][y] = 0
    return


n = 3
soln = []
for i in range(n):
    soln.append([0 for j in range(n)])
# soln[0][0]=1
soln[n - 1][n - 1] = 1
x = [[1, 1, 0], [0, 1, 1], [0, 1, 1]]
hasPath(x, 0, 0, n, soln)
