def partition(Array, low, up):
    i = low + 1
    j = up
    pivot = Array[low]
    while (i <= j):
        while (Array[i] < pivot and i < up):
            i = i + 1
        while (Array[j] > pivot):
            j = j - 1
        if (i < j):
            Array[i], Array[j] = Array[j], Array[i]
            i = i + 1
            j = j - 1
        else:
            i = i + 1
    Array[low] = Array[j]
    Array[j] = pivot
    return j


def quick(Array, low, up):
    if (low >= up):
        return
    piv_loc = partition(Array, low, up)
    quick(Array, low, piv_loc - 1)
    quick(Array, piv_loc + 1, up)


a = [14, 15, 16, 17]
quick(a, 0, 3)
print a
