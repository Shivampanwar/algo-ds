def index_numbers(array, start_index, end_index, k):
    if start_index == end_index:
        if array[start_index] == k:
            return start_index
        else:
            return -1
    else:
        small_problem_index = index_numbers(array, start_index + 1, end_index, k)
        if small_problem_index is not -1:
            return small_problem_index
        else:
            if array[start_index] == k:
                return start_index
            else:
                return -1

        # if array[start_index]==k:
        #     return start_index
        # else:
        #     return index_numbers(array,start_index+1,end_index,k)


print index_numbers([1, 4, 3, 7, 9, 7, 8], 0, 6, 10)
