def all_codes(array, size_array):
    if len(array) == 0:
        return 1
    if len(array) == 1:
        return 1
    else:
        length = len(array)
        if size_array[length] is not 0:
            return size_array[length]
        else:
            small_output = all_codes(array[1:], size_array)
            if 10 * array[0] + array[1] < 27:
                small_output += all_codes(array[2:], size_array)
            size_array[length] = small_output
            return small_output


a = str(input())
while int(a) is not 0:
    arr = [int(x) for x in a]
    print arr
    size_array = []
    size_array.append(0)
    for i in range(len(arr) + 1):
        size_array.append(0)
    result = all_codes(arr, size_array)
    print (result)
    a = str(input())

# print all_codes([2,0,3])
