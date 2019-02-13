def mcm(array):
    '''
         Simple recursive function
    '''
    if len(array) == 2:
        return 0, array
    else:
        length_word = len(array) - 1
        value = []
        for i in range(1, length_word):
            left_result, left_shape = mcm(array[:i + 1])
            right_result, right_shape = mcm(array[i:])
            result = left_result + right_result
            result += left_shape[0] * left_shape[1] * right_shape[1]
            value.append(result)
        return min(value), [array[0], array[-1]]


print mcm([10, 20, 30, 40, 30])


def mcm_recursive(array, si, ei):
    if ei - si == 1:
        return 0
    values = []
    for k in range(si + 1, ei):
        left_result = mcm_recursive(array, si, k)
        right_result = mcm_recursive(array, k, ei)
        result = left_result + right_result + array[si] * array[k] * array[ei]
        values.append(result)
    return min(values)


def mcm_helper(array, si, ei, dp):
    if dp[si][ei] is not -1:
        return dp[si][ei]
    if ei - si == 1:
        dp[si][ei] = 0
        return 0
    values = []
    for k in range(si + 1, ei):
        left_result = mcm_helper(array, si, k, dp)
        right_result = mcm_helper(array, k, ei, dp)
        result = left_result + right_result + array[si] * array[k] * array[ei]
        values.append(result)
    dp[si][ei] = min(values)
    return dp[si][ei]


def mcm_dp(array, si, ei):
    dp = []
    for i in range(len(array)):
        temp = []
        for j in range(len(array)):
            temp.append(-1)
        dp.append(temp)
    print mcm_helper(array, si, ei, dp)


# print mcm_recursive([10, 20, 30 , 40,30], 0, 4)
arr = [10, 15, 20, 25]
print len(arr)
mcm_dp(arr, 0, len(arr) - 1)
