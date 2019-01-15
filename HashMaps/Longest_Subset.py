def count_longest_subset(array):
    dict = {}
    num_zeros = 0
    num_ones = 0
    sum = 0
    for i in range(len(array)):
        sum += array[i]
        dict[i] = sum
        if array[i]:
            num_ones += 1
        else:
            num_zeros += 1
    subarray_size = 2 * min(num_zeros, num_ones)
    if subarray_size == 0:
        return 0
    else:
        while subarray_size > 0:
            req_sum = subarray_size / 2
            subarrays = []
            i = 0
            while i + subarray_size - 1 < len(array):
                subarrays.append((i, i + subarray_size - 1))
                i += 1

            for j in subarrays:
                if j[0] == 0:
                    temp = dict[j[1]]
                else:
                    temp = dict[j[1]] - dict[j[0] - 1]
                if temp == req_sum:
                    return j[1] - j[0] + 1

            subarray_size += -2


print count_longest_subset([1, 0, 1, 1, 1, 0, 0])
