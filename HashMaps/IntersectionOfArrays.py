from collections import OrderedDict


def intersection(array1, array2):
    dictionary = OrderedDict()
    for i in array1:
        if i not in dictionary.keys():
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    array = []
    for i in array2:
        if i in dictionary.keys():
            if dictionary[i] > 0:
                array.append(i)
                dictionary[i] += -1
    return array
# filename = raw_input("input1.txt: ")
# with open(filename, 'r') as f:
#     line = f.read()
