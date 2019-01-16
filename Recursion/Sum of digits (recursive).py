def sum_of_digits(n):
    if n < 10:
        return n
    else:
        small_sum = sum_of_digits(n / 10)
        return n % 10 + small_sum


print sum_of_digits(19900)
