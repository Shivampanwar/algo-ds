def min_squares(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        min = dp[i - 1]
        for j in range(2, i):
            k = i - j * j
            if k is 0:
                min = 0
                break
            elif k > 0:
                if min > dp[k]:
                    min = dp[k]

            else:
                break
        dp.append(min + 1)
    return dp[-1]


print min_squares(9)
