def find_repition(array):
    dict = {}
    count = float("inf")
    for i in range(len(array)):
        if array[i] in dict:
            temp = abs(dict[array[i]] - i)
            if temp < count:
                count = temp
            dict[array[i]] = i
        else:
            dict[array[i]] = i
    return count


print find_repition([5, 47, 82, 4, 4, 6, 2
                     ])
