def steps(n):
    '''
    Without dynamic programming

    :param n:
    :return:
    '''
    list_of_values = []
    if n < 1:
        return
    if n == 1:
        return 0
    else:
        if n % 2 == 0:
            list_of_values.append(steps(n / 2))
        if n % 3 == 0:
            list_of_values.append(steps(n / 3))
        list_of_values.append(steps(n - 1))
    temp = 10000
    for i in list_of_values:
        if i < temp:
            temp = i
    return temp + 1


def stepswithdp(n, array):
    if n == 1:
        return 0
    if n < 1:
        return
    if array[n] is not -1:
        return array[n]
    else:
        print n
        min = stepswithdp(n - 1, array)
        if n % 2 == 0:
            k = stepswithdp(n / 2, array)
            if min > k:
                min = k
        if n % 3 == 0:
            k = stepswithdp(n / 3, array)
            if k < min:
                min = k
        array[n] = min + 1
        return min + 1


n = 1000
array = []
for i in range(n + 1):
    array.append(-1)


def stepswithdpfinal(n):
    array = []
    array.append(0)
    array.append(0)
    for i in range(2, n + 1):
        min = array[i - 1]
        if i % 2 == 0:
            temp = array[int(i / 2)]
            if temp < min:
                min = temp
        if i % 3 == 0:
            k = array[int(i / 3)]
            if k < min:
                min = k
        array.append(min + 1)
    return array[-1]


print stepswithdpfinal(100)
