def pushToEnd(array):
    ptr = None
    for i in range(len(array)):
        if array[i] == 0:
            if ptr == None:
                ptr = i
        else:
            if ptr == None:
                pass
            else:
                array[ptr], array[i] = array[i], array[ptr]
                ptr += 1
    return array


print pushToEnd([1, 2, 3, 4, 0, 0, 1, 0])
