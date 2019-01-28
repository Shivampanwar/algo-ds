import sys


def combination(array, k):
    if array[0] > k:
        return [[]]
    if array[0] == k:
        return [[k]]
    if k == 0:
        return [[k]]
    temp_list = []
    for i in range(len(array)):
        start = array[i]
        if start == k:
            temp_list.append([k])
        else:
            small_result = combination(array[i:], k - start)
            if len(small_result) > 0:
                if len(small_result[0]) > 0:
                    for i in small_result:
                        temp_list.append([start] + i)
    return temp_list


array = [5, 6]
array.sort()
result = combination(array, 11)
for i in result:
    for j in i:
        sys.stdout.write(str(j) + " ")
    print "\n"


def comb(n, k):
    if n > k:
        return
    else:
        print n
        for j in range(0, 10):
            comb(10 * n + j, k)


for i in range(1, 10):
    comb(i, 20)
