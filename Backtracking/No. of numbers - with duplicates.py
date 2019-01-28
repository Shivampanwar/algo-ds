import math


def count_digits(array, freq_array, n):
    if len(array) == 1 or len(array) == 0:
        return 0
    else:
        start = array[0]
        freq_array[start] += -1
        res = count_digits(array[1:], freq_array, n - 1)
        freq_array[start] += 1
        start = array[0]
        count = 0
        possible_candidate = []
        for i in range(len(freq_array)):
            if freq_array[i] is not 0 and i > start:
                possible_candidate.append(i)
        for candidate in possible_candidate:
            temp = math.factorial(n - 1)
            for i in range(len(freq_array)):
                if freq_array[i] is not 0 and i is not candidate:
                    temp = temp / math.factorial(freq_array[i])
            val = freq_array[candidate]
            if val > 1:
                val += -1
                temp = temp / math.factorial(val)
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

print count_digits(array, freq_array, len(array))
