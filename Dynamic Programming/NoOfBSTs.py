def bst(n):
    MOD = 1000000007
    dp = []
    dp.append(1)
    dp.append(1)
    dp.append(2)
    for i in range(3, n + 1):
        k = 0
        for j in range(1, i + 1):
            left_no = j - 1
            right_no = i - j
            k += dp[left_no] * dp[right_no]
        dp.append(k)
    return dp[-1]


print bst(8)
