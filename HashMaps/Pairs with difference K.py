import sys


def find_permutations(array1, array2):
    permutations = []
    for i in array1:
        for j in array2:
            if i < j:
                permutations.append((i, j))
            else:
                permutations.append((j, i))
    return permutations


def find_pairs(array, k):
    dict = {}
    for i in array:
        if i in dict:
            dict[i].append(i)
        else:
            print i
            dict[i] = [i]
    new_array = []
    if k == 0:
        for key in dict.keys():
            n = len(dict[key]) - 1
            count = n * (n + 1) / 2
            new_array.extend([(key, key)] * count)
    else:
        for key in dict.keys():
            if key - k in dict:
                new_array.extend(find_permutations(dict[key], dict[key - k]))
    return new_array


ans = find_pairs([4, 4, 4, 4, 2, 2], 0)
for i in ans:
    sys.stdout.write(str(i[0]))
    sys.stdout.write(" ")
    sys.stdout.write(str(i[1]))
    print ("\n")
