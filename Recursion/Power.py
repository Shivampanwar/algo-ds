def power(x, n):
    if n == 1 or n == 0:
        return x
    else:
        small_output = power(x, n - 1)
        return x * small_output


print power(0, 1)
