def remove_duplicates(array):
    if len(array) == 1:
        return array
    else:
        array[1:] = remove_duplicates(array[1:])
        if array[0] == array[1]:
            i = 0
            while i < len(array) - 1:
                array[i] = array[i + 1]
                i += 1
            del array[i]
        return array


print remove_duplicates([1, 1, 2, 2, 32, 33, 3, 3, 4, 4])
