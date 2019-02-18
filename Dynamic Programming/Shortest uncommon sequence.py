def ShortestSequence(str1, str2):
    if len(str1) == 0:
        return 10000
    if len(str2) == 0:
        return 1
    if str1[0] not in str2:
        return 1
    not_incude = ShortestSequence(str1[1:], str2)
    include = ShortestSequence(str1[1:], str2[str2.find(str1[0]) + 1:]) + 1
    return min(include, not_incude)


# print ShortestSequence('banana','anbnaanbaan')
# print ShortestSequence('abc','ac')

print ShortestSequence('abc', 'ac')


def shortest_seq_helper(str1, str2, si1, si2, dp):
    if dp[si1][si2] is not -1:
        return dp[si1][si2]
    if si1 == len(str1):
        return 100000
    if si2 == len(str2):
        return 1
    if str1[si1] not in str2[si2:]:
        return 1

    k = str2[si2:].find(str1[si1]) + si2 + 1
    include = shortest_seq_helper(str1, str2, si1 + 1, k, dp) + 1
    not_incude = shortest_seq_helper(str1, str2, si1 + 1, si2, dp)
    dp[si1][si2] = min(include, not_incude)
    return dp[si1][si2]


def shortest_sequence_dp(str1, str2):
    dp = []
    for i in range(len(str1) + 1):
        temp = []
        for j in range(len(str2) + 1):
            temp.append(-1)
        dp.append(temp)
    x = shortest_seq_helper(str1, str2, 0, 0, dp)
    print x


shortest_sequence_dp('babab', 'babba')
shortest_sequence_dp('banana', 'anbnaanbaan')
# shortest_sequence_dp('abc','acb')
