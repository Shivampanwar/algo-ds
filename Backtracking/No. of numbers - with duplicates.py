import math


def count_digits(array, freq_array, n):
    if len(array) == 1 or len(array) == 0:
        return 0
    else:
        start = array[0]
        freq_array[start] += -1
        res = count_digits(array[1:], freq_array, n - 1)
        print str(start) + " " + str(res)
        freq_array[start] += 1
        start = array[0]
        count = 0
        for i in range(start + 1, len(freq_array)):
            if freq_array[i] > 0:
                temp = math.factorial(n - 1)
                freq_array[i] += -1
                for j in freq_array:
                    if j is not 0:
                        temp /= j
                freq_array[i] += 1
                count += temp

        return res + count


a = str(input())
array = []
for digit in a:
    array.append(int(digit))
freq_array = []
for i in range(10):
    freq_array.append(0)
for i in array:
    freq_array[i] += 1

# print freq_array

# print count_digits(array,freq_array,len(array))
start = array[0]
count = 0
print freq_array
for i in range(start + 1, len(freq_array)):
    if freq_array[i] > 0:
        temp = math.factorial(5)
        freq_array[i] += -1
        print freq_array
        for j in freq_array:
            if j is not 0:
                print j
                temp /= j
            freq_array[i] += 1
            count += temp
print count
