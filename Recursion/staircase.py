def num_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return num_stairs(n - 1) + num_stairs(n - 2) + num_stairs(n - 3)


print num_stairs(10)
