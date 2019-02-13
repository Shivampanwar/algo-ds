def Coin_change(count, array):
    # base case left
    if count == 0:
        return
    num = array[0]
    num_possible = count / num
    value = 0
    for i in range(num_possible):
        res = Coin_change(count - i * num, array[1:])
        if res < 0:
            value
    return value
