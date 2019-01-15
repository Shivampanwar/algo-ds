def count_deletions(array1, array2):
    dict1 = {}
    dict2 = {}
    for i in array1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in array2:
        if i in dict2:
            dict2[i] += 1
        else:
            dict2[i] = 1
    count = 0
    for key in dict1.keys():
        if key in dict2.keys():
            count += abs(dict1[key] - dict2[key])
            dict1[key] = 0
            dict2[key] = 0
        else:
            count += dict1[key]
    for key in dict2.keys():
        if key in dict1.keys():
            count += abs(dict1[key] - dict2[key])
            dict2[key] = 0
            dict1[key] = 0
        else:
            count += dict2[key]
    return count
# print count_deletions("bcadeh","hea")
