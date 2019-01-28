import sys


def subset(array):
    if len(array) == 1:
        return [array]
    else:
        result = subset(array[1:])
        start = array[0]
        new_list = []
        for i in result:
            new_list.append(i)
            new_list.append([start] + i)
        new_list.append([start])
        return new_list


answer = subset([15, 20, 12])
for i in answer:
    for j in i:
        sys.stdout.write(str(j) + " ")
    print ("\n")
