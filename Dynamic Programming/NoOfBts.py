def bts(n):
    MOD = 1000000007
    dp = []
    dp.append(1)
    dp.append(1)
    for i in range(2, n + 1):
        val = (dp[i - 1] * ((2 * dp[i - 2]) % MOD + dp[i - 1]) % MOD) % MOD
        dp.append(val)
    return dp[-1]


print bts(100)


def num_bts(n, array):
    MOD = 1000000007
    if n == 1:
        return 1
    if n == 0:
        return 1
    else:
        if array[n] is not 0:
            return array[n]
        else:
            small = (num_bts(n - 1, array) * ((2 * num_bts(n - 2, array)) % MOD + num_bts(n - 1, array)) % MOD) % MOD
            array[n] = small
            return small


n = int(input())
dp_array = []
dp_array.append(1)
dp_array.append(1)
dp_array.extend([0 for i in range(2, n + 1)])
print (num_bts(n, dp_array))
