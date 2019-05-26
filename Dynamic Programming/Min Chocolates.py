'''
     Noor is a teacher. She wants to give some chocolates to the students in her class. All the students sit in a line and each of them has a score according to performance. Noor wants to give at least 1 chocolate to each student. She distributes chocolates to them such that If two students sit next to each other then the one with the higher score must get more chocolates. Noor wants to save money, so she wants to minimise the total number of chocolates.
    Note that when two students have equal score they are allowed to have different number of chocolates.
    Sample Input:
    4
    1 4 4 6
    sample Output:
    6
'''
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
