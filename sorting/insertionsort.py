def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i - 1, -1, -1):
            if array[j + 1] >= array[j]:
                break
            else:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array


print insertion_sort([14, 7, 3, 12, 9, 11, 6, 2])
