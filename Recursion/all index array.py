import sys


def all_index_array(array, start_index, end_index, k):
    if start_index == end_index:
        if array[start_index] == k:
            sys.stdout.write(str(start_index) + " ")
            return start_index
        else:
            return
    else:
        if array[start_index] == k:
            sys.stdout.write(str(start_index) + " ")
        return all_index_array(array, start_index + 1, end_index, k)


all_index_array([1, 3, 5, 3, 4, 3, 3, 3], 0, 7, 13)
