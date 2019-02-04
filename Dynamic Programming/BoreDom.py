def boredom(array):
    freq_array = [0 for i in range(0, 1001)]
    for i in array:
        freq_array[i] += 1
    dp = [0]
    dp.append(freq_array[1])
    for i in range(2, len(freq_array)):
        include = i * freq_array[i] + dp[i - 2]
        exclude = dp[i - 1]
        dp.append(max(include, exclude))
    return dp[-1]


def boredom2(array):
    if len(array) == 1:
        return array[0]
    if len(array) == 0:
        return 0
    else:
        exclude = boredom2((array[1:]))
        if array[1] - array[0] == 1:
            idx = 1
            while idx < len(array) and array[idx] - array[0] is 1:
                idx += 1
            include = boredom2(array[idx:]) + array[0]
        else:
            include = boredom2(array[1:]) + array[0]
        return max(exclude, include)


# print boredom([1,2,3,4])
print boredom2([1, 2, 3, 4, 4, 6, 6])


def BoreDom(array):
    dp = []
    dp.append(0)
    freq_array = [0 for i in range(0, 1001)]
    for i in array:
        freq_array[i] += 1
    dp.append(freq_array[1])
    for i in range(2, 1001):
        if freq_array[i] is not 0:
            val_include = i * freq_array[i] + max(dp[:i - 1])
            dp.append(val_include)
        else:
            dp.append(0)
    return max(dp)


print "dhfdfd"
print BoreDom([999, 1000, 998])
