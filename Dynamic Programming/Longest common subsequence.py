def lcs(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return 0
    else:
        if str1[0] == str2[0]:
            return 1 + lcs(str1[1:], str2[1:])
        else:
            return max(lcs(str1[1:], str2), lcs(str1, str2[1:]))


def lcs2helper(str1, str2, first, second, dp):
    if len(str1) == 0 or len(str2) == 0:
        dp[first][second] = 0
        return 0
    if dp[first][second] is not -1:
        return dp[first][second]
    else:
        if str1[0] == str2[0]:
            result = lcs2helper(str1[1:], str2[1:], first - 1, second - 1, dp)
            result += 1
            dp[first][second] = result
            return result
        else:
            option1 = lcs2helper(str1[1:], str2, first - 1, second, dp)
            option2 = lcs2helper(str1, str2[1:], first, second - 1, dp)
            result = max(option1, option2)
            dp[first][second] = result
            return result


def lcs2(str1, str2):
    m, n = len(str1), len(str2)
    dp = []
    for i in range(m + 1):
        dp.append([])
        for j in range(n + 1):
            dp[i].append(-1)
    print lcs2helper(str1, str2, m, n, dp)


def lcsdp(str1, str2):
    m, n = len(str1), len(str2)
    dp = []
    for i in range(m + 1):
        dp.append([])
        for j in range(n + 1):
            dp[i].append(-1)

    for i in range(n + 1):
        dp[0][i] = 0
    for i in range(m + 1):
        dp[i][0] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[-i] == str2[-j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                val = max(dp[i][j - 1], dp[i - 1][j])
                dp[i][j] = val
    return dp[m][n]


print lcsdp('ABCDGH', 'AEDFHR')
