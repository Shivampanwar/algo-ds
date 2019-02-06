def Min_cost_wo_dp(input, si, sj, ei, ej):
    '''
    Does not use dp
    '''
    if si == ei and sj == ej:
        return input[si][sj]
    if si > ei or sj > ej:
        return 10000000
    option1 = Min_cost_wo_dp(input, si, sj + 1, ei, ej)
    option2 = Min_cost_wo_dp(input, si + 1, sj + 1, ei, ej)
    option3 = Min_cost_wo_dp(input, si + 1, sj, ei, ej)
    return input[si][sj] + min(option1, option2, option3)


def Min_cost_with_dp(input, si, sj, ei, ej, dp):
    '''
     use dp
    '''
    if dp[si][sj] is not -1:
        return dp[si][sj]
    if si == ei and sj == ej:
        dp[si][sj] = input[si][sj]
        return input[si][sj]
    if si > ei or sj > ej:
        return 10000000
    if dp[si][sj + 1] is not -1:
        option1 = dp[si][sj + 1]
    else:
        option1 = Min_cost_wo_dp(input, si, sj + 1, ei, ej)
    if dp[si + 1][sj + 1] is not -1:
        option2 = dp[si + 1][sj + 1]
    else:
        option2 = Min_cost_wo_dp(input, si + 1, sj + 1, ei, ej)
    if dp[si + 1][sj] is not -1:
        option3 = dp[si + 1][sj]
    else:
        option3 = Min_cost_wo_dp(input, si + 1, sj, ei, ej)
    dp[si][sj] = input[si][sj] + min(option1, option2, option3)
    return dp[si][sj]


def Min_cost_iterative(input):
    row, col = len(input), len(input[0])
    dp = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(0)
        dp.append(temp)
    dp[row - 1][col - 1] = input[row - 1][col - 1]

    for i in range(row - 2, -1, -1):
        dp[i][col - 1] = dp[i + 1][col - 1] + input[i][j]

    for i in range(col - 2, -1, -1):
        dp[row - 1][i] = dp[row - 1][i + 1] + input[i][j]
    for i in range(row - 2, -1, -1):
        for j in range(col - 2, -1, -1):
            temp = min(dp[i + 1][j], dp[i][j + 1])
            temp += input[i][j]
            dp[i][j] = temp
    return dp[0][0]


cost = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
dp = [[-1, -1, -1],
      [-1, -1, -1],
      [-1, -1, -1]]

print Min_cost_iterative(cost)
print(Min_cost_with_dp(cost, 0, 0, 2, 2, dp))
