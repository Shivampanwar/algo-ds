def countplatforms(array1, array2):
    temp_array = []
    temp_array.append(array2[0])
    for i in range(1, len(array1)):
        inserted = False
        for j in range(len(temp_array)):
            if temp_array[j] < array1[i]:
                temp_array[j] = array2[i]
                inserted = True
                break
        if inserted:
            pass
        else:
            temp_array.append(array2[i])
    return len(temp_array)


arr1 = [0310, 2329, 2358, 995]
arr2 = [0315, 2338, 2359, 1018]
dict = {}
for i in range(len(arr1)):
    dict[arr1[i]] = arr2[i]
arr1.sort()
for i in range(len(arr1)):
    arr2[i] = dict[arr1[i]]
print countplatforms(arr1, arr2)
