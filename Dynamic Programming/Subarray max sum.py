def max_array(array):
    temp_array = []
    temp_array.append(array[0])
    for i in range(1, len(array)):
        sum = temp_array[i - 1] + array[i]
        print sum
        if sum < array[i]:
            temp_array.append(array[i])
        else:
            temp_array.append(sum)
    temp = 0
    maximum = max(temp_array)
    idx = temp_array.index(maximum)
    start = idx
    while temp is not maximum:
        temp += temp_array[start]
        start += -1
    return array[start:idx + 1]


print max_array([2, -4, 5, 9])
