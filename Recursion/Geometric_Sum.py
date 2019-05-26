def geometric_sum(n):
    if n == 0:
        return 1
    else:
        small_sum = geometric_sum(n - 1)
        return small_sum + pow(1 / float(2), n)


print round(geometric_sum(3), 5)
