def merge(array, start, mid, end):
    temp_array = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if array[i] <= array[j]:
            temp_array.append(array[i])
            i += 1
        else:
            temp_array.append(array[j])
            j += 1
    while i <= mid:
        temp_array.append(array[i])
        i += 1
    while j <= end:
        temp_array.append(array[j])
        j += 1
    array[start:end + 1] = temp_array
    return array


def merge_sort(array, start_index, end_index):
    if end_index - start_index == 0:
        return array
    else:
        mid = int((start_index + end_index) / 2)
        merge_sort(array, start_index, mid)
        merge_sort(array, mid + 1, end_index)
        return merge(array, start_index, mid, end_index)


print merge_sort([9, 1, 2, 4, 56, 77, 44, -1], 0, end_index=7)
