def MinEdits(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return max(len(str1), len(str2))
    if str1[0] == str2[0]:
        return MinEdits(str1[1:], str2[1:])
    else:
        option1 = 1 + MinEdits(str1[1:], str2)  # delete
        option2 = 1 + MinEdits(str1, str2[1:])  # insert
        option3 = 1 + MinEdits(str1[1:], str2[1:])  # replace
        return min(option1, option2, option3)


def min_edits_helper(str1, str2, dp, m, n):
    if m == 0 or n == 0:
        dp[m][n] = max(m, n)
        return dp[m][n]
    if dp[m][n] is not -1:
        return dp[m][n]
    if str1[0] == str2[0]:
        if dp[m - 1][n - 1] is not -1:
            return dp[m - 1][n - 1]
        else:
            result = min_edits_helper(str1[1:], str2[1:], dp, m - 1, n - 1)
            dp[m - 1][n - 1] = result
            return result
    else:
        # case of delete
        option1 = min_edits_helper(str1[1:], str2, dp, m - 1, n)
        option2 = min_edits_helper(str1, str2[1:], dp, m, n - 1)
        option3 = min_edits_helper(str1[1:], str2[1:], dp, m - 1, n - 1)
        dp[m][n] = min(option1, option2, option3) + 1
        return dp[m][n]


def min_edits_recursive(str1, str2):
    m, n = len(str1), len(str2)
    dp = []
    for i in range(m + 1):
        dp.append([])
        for j in range(n + 1):
            dp[i].append(-1)
    return min_edits_helper(str1, str2, dp, m, n)


# print MinEdits('sunday','saturday')
print min_edits_recursive('intention', 'execution')
