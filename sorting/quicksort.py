def partition(array, start, end):
    pivot = array[end]
    main_pointer = start
    bigarray_pointer = start
    while main_pointer != end:
        if array[main_pointer] <= pivot:
            array[main_pointer], array[bigarray_pointer] = array[bigarray_pointer], array[main_pointer]
            main_pointer += 1
            bigarray_pointer += 1
        else:
            main_pointer += 1
    array[main_pointer] = array[bigarray_pointer]
    array[bigarray_pointer] = pivot
    return array


print partition([1, 3, 5, 16, 4, 10, 17, -1, 9], 0, 8)
