from collections import OrderedDict


def find_maximum(array):
    bucket_array = OrderedDict()
    for i in array:
        try:
            bucket_array[i] += 1
        except:
            bucket_array[i] = 1
    print bucket_array
    main_key = None
    value = 0
    for key in bucket_array.keys():
        if bucket_array[key] > value:
            main_key = key
            value = bucket_array[key]
    return main_key


print find_maximum([1, 1, 2, 2, 4, 4, 3, 3, 3, 1])
