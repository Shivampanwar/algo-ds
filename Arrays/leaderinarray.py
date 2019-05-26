def leader(array):
    temp_list = []
    temp_list.append(array[-1])
    max = array[-1]
    for i in range(len(array) - 2, -1, -1):
        if array[i] >= max:
            temp_list.append(array[i])
            max = array[i]
    return temp_list


print leader([3, 12, 34, 2, 0, -1])
