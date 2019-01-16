def array_sum(array):
    if len(array) == 1:
        return array[0]
    else:
        small_sum = array_sum(array[1:])
        return array[0] + small_sum


print array_sum([9, 9, 9])
