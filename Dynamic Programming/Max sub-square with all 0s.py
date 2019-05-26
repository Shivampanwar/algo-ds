def max_sub_square(array):
    row = len(array)
    col = len(array[0])
    dp = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(-1)
        dp.append(temp)
    for i in range(col):
        if array[0][i] == 0:
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    for i in range(row):
        if array[i][0] == 1:
            dp[i][0] = 0
        else:
            dp[i][0] = 1
    for i in range(1, row):
        for j in range(1, col):
            if array[i][j] == 0:
                minimum = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = minimum + 1
            else:
                dp[i][j] = 0
    print max(max(dp))


max_sub_square([[1, 0, 0], [0, 0, 0], [1, 1, 1]])

n, m = int(input().strip().split(" ")[0]), int(input().strip().split(" ")[1])
big_array = []
for i in range(0, m):
    temp = [int(j) for j in input().strip().split(" ")]
    big_array.append(temp)
    temp.clear()

print (big_array)
