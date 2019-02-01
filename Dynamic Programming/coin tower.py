def coin_recursive(n, array1, array2, x, y, turn):
    if n == 0:
        if turn == 'a':
            return 'b'
        else:
            return 'a'
    possible_options = []
    for i in set([x, y, 1]):
        if (n - i) >= 0 and i is not 0:
            possible_options.append(n - i)
    solutions = []
    if turn == 'a':
        if array1[n] is not 0:
            return array1[n]
        else:
            for i in possible_options:
                if array2[i] is 0:
                    val = coin_recursive(i, array1, array2, x, y, 'b')
                    solutions.append(val)
                    array2[i] = val
                else:
                    solutions.append(array2[i])
    else:
        if array2[n] is not 0:
            return array2[n]
        else:
            for i in possible_options:
                if array1[i] is 0:
                    val = coin_recursive(i, array1, array2, x, y, 'a')
                    solutions.append(val)
                    array1[i] = val
                else:
                    solutions.append(array1[i])
                # solutions.append(coin_recursive(i,array1,array2,x,y,'a'))
    if 'a' in solutions:
        if turn == 'a':
            array1[n] = 'a'
        else:
            array2[n] = 'a'
        return 'a'
    else:
        if turn == 'a':
            array1[n] = 'b'
        else:
            array2[n] = 'b'
        return 'b'


def properdp(n, x, y):
    dp = [0 for i in range(n + 1)]
    dp[0] = False
    dp[1] = True
    for i in range(2, n + 1):
        if i - 1 >= 0 and not dp[i - 1]:
            dp[i] = True
        elif (i - x >= 0 and not dp[i - x]):
            dp[i] = True
        elif (i - y >= 0 and not dp[i - y]):
            dp[i] = True

        # Else A loses game.
        else:
            dp[i] = False
    return dp[-1]


n = 3
x = 5
y = 4
array1 = ['b']
for i in range(1, n + 1):
    array1.append(0)
array2 = ['a']
for i in range(1, n + 1):
    array2.append(0)
a = coin_recursive(n, array1, array2, x, y, 'a')
# print a
