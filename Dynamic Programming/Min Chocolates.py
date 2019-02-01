def chocolates(array):
    dp = []
    dp.append(1)
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            dp.append(dp[i - 1] + 1)
        else:
            dp.append(1)
    print dp
    for i in range(len(array) - 2, -1, -1):
        if array[i] > array[i + 1] and dp[i] <= dp[i + 1]:
            dp[i] = 1 + dp[i + 1]
    print dp
    return sum(dp)


print chocolates([2, 1, 4, 4, 6])
