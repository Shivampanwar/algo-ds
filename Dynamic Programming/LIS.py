def lis(array, start_index, end_index, max_array):
    for index in range(start_index, end_index):
        if max_array[index] is not 0:
            pass
        else:
            bigger_array = []
            start = array[index]
            for i in range(index, end_index):
                if start < array[i]:
                    bigger_array.append(i)
            if len(bigger_array) == 0:
                max_array[index] = 1
            else:
                bigger_values = []
                for big in bigger_array:
                    if max_array[big] is not 0:
                        bigger_values.append(max_array[big])
                    else:
                        lis(array, big, end_index, max_array)
                        bigger_values.append(max_array[big])
                max_array[index] = max(bigger_values) + 1


max_array = [0, 0, 0, 0, 0, 0]
lis([5, 4, 11, 1, 16, 8], 0, 6, max_array)
print max_array
