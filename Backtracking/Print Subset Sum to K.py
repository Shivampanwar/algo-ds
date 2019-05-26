import sys


def subset_sum(array, k):
    if len(array) == 1:
        main_element = array[0]
        if main_element == k:
            return [array]
        else:
            return []
    else:
        start = array[0]
        if start == k:
            return [[start]] + subset_sum(array[1:], k)
        result_include = subset_sum(array[1:], k - start)  # including start
        result_exclude = subset_sum(array[1:], k)
        if len(result_include) > 0:
            new_list = []
            for i in result_include:
                new_list.append([start] + i)
            return new_list + result_exclude
        return result_exclude


a = "5 12 3 17 1 18 15 3 17 "
arr = list(int(i) for i in a.strip().split(' '))
ans = subset_sum(arr, 6)
print ans
for i in ans:
    for j in i:
        sys.stdout.write(str(j) + " ")
    print ("\n")
