import numpy as np


def lcs(array):
    dict = {}
    for i in array:
        dict[i] = False
    count = 0
    big_array = []
    for key in dict.keys():
        if dict[key] != True:
            i = key + 1
            temp = 0
            dict[key] = True
            while i in dict and dict[i] == False:
                dict[i] = True
                temp += 1
                i += 1
            if temp >= count:
                count = temp
                big_array = np.arange(key, key + temp + 1, 1)
    return big_array, count + 1


print lcs([1, 3, 4, 5, 5, 6, 8])
