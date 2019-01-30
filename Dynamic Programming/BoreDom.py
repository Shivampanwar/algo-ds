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


print boredom([1, 2, 3, 4])
