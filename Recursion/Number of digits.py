def array_sum(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + array_sum(array[1:])


print(array_sum([1, 2, 3]))
