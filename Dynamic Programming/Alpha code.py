def all_codes(array, size_array):
    if len(array) == 0:
        return 1
    if len(array) == 1:
        return 1
    else:
        length = len(array)
        if size_array[length] is not 0:
            return size_array[length]
        else:
            small_output = all_codes(array[1:], size_array)
            if 10 * array[0] + array[1] < 27:
                small_output += all_codes(array[2:], size_array)
            size_array[length] = small_output
            return small_output


def all_codes_proper_dp(array):
    if len(array) == 1:
        return 1
    if len(array) == 0:
        return 1
    else:
        temp_array = []
        temp_array.append(1)
        temp_array.append(1)
        for i in range(2, len(array) + 1):
            temp = temp_array[i - 1]
            numbers = array[-i:]
            k = numbers[0] * 10 + numbers[1]
            if k < 27:
                temp += temp_array[i - 2]
            temp_array.append(temp)
        return temp_array[-1]


# a = str(input())
# while int(a) is not 0:
#     arr = [int(x) for x in a]
#     size_array = []
#     size_array.append(0)
#     for i in range(len(arr) + 1):
#         size_array.append(0)
#     result = all_codes(arr, size_array)
#     print (result)
#     a = str(input())
a = str(input())
while int(a) is not 0:
    arr = [int(x) for x in a]
    result = all_codes_proper_dp(arr)
    print (result)
    a = str(input())
# inp=str(input())
# list_word=inp.split(" ")
# for i in list_word:
#     if int(i)==0:
#         break
#     else:
#         arr = [int(x) for x in i]
#         size_array = []
#         size_array.append(0)
#         for i in range(len(arr) + 1):
#             size_array.append(0)
#         result = all_codes(arr, size_array)
#         print (result)
