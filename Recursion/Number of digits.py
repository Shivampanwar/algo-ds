def count_digits(n):
    if n < 10:
        return 1
    else:
        small_output = count_digits(n / 10)
        return 1 + small_output


print count_digits(1234555)
