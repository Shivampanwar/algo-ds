import sys
from collections import defaultdict


def sortarray(array):
    dict = defaultdict()
    count = 0
    for i in array:
        if i in dict.keys():
            dict[i] += 1
            count += 1
        else:
            dict[i] = 1
    ptr = 0
    for key in range(3):
        if key in dict.keys():
            for j in range(ptr, ptr + dict[key]):
                array[j] = key
            ptr += dict[key]
    return array

n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
ans = sortarray(arr)
for i in ans:
    sys.stdout.write(str(i))
    sys.stdout.write(" ")
