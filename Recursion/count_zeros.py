def count_zeros(number):
    if number < 10:
        if number == 0:
            return 1
        else:
            return 0
    else:
        small_output = count_zeros(number / 10)
        if number % 10 == 0:
            return small_output + 1
        else:
            return small_output


print count_zeros(30056)
