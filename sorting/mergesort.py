def merge(array, start, mid, end):
    p = start
    q = mid + 1
    new_array = []
    while p < mid + 1 and q < end + 1:
        if array[p] <= array[q]:
            new_array.append(array[p])
            p += 1
        else:
            new_array.append(array[q])
            q += 1
    while p < mid + 1:
        new_array.append(array[p])
        p += 1
    while q < end + 1:
        new_array.append(array[q])
        q += 1
    array[start:end + 1] = new_array
    return array


def mergesort(array, start, end):
    if start == end:
        return array[start]
    else:
        mid = (start + end) / 2
        mergesort(array, start, mid)
        mergesort(array, mid + 1, end)
        return merge(array, start, mid, end)


print mergesort([14, 7, 3, 12, 9, 11, 6, 2], 0, 7)
print mergesort([-1, 12, -100, -99, 88], 0, 4)
