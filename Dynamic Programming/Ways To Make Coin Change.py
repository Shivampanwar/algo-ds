def Coin_change(n, array):
    if n == 0:
        return 1
    if len(array) == 1:
        if n % array[0] is not 0:
            return 0
        else:
            return 1
    possible_values = n / array[0]
    total_values = 0
    for i in range(possible_values + 1):
        result = Coin_change(n - (i * array[0]), array[1:])
        # print result
        total_values += result
    return total_values


# print Coin_change(4,[4, 3, 2, 1])
# print Coin_change(1,[6])

def coin_change_helper(n, array, start_index, dp):
    if dp[n][start_index] is not -1:
        return dp[n][start_index]
    if n == 0:
        dp[n][start_index] = 1
        return 1
    if len(array) - start_index == 1:
        if n % array[start_index] is not 0:
            dp[n][start_index] = 0
            return 0
        else:
            dp[n][start_index] = 1
            return 1
    possible_values = n / array[start_index]
    total_values = 0
    for i in range(possible_values + 1):
        result = coin_change_helper(n - (i * array[start_index]), array, start_index + 1, dp)
        # print result
        total_values += result
    dp[n][start_index] = total_values
    return total_values


def coin_change_dp(n, array):
    dp = []
    for i in range(n + 1):
        temp = []
        for j in range(len(array)):
            temp.append(-1)
        dp.append(temp)
    print coin_change_helper(n, array, 0, dp)


coin_change_dp(5, [1, 2, 5])
