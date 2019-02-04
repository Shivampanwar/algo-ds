def loot(si, ei, array, value_array):
    for idx in range(si, ei):
        if idx == ei - 1 or idx == ei - 2:
            value_array[idx] = array[idx]
        elif value_array[idx] is not 0:
            pass
        else:
            values = []
            for inner_idx in range(idx + 2, ei):
                if value_array[inner_idx] is not 0:
                    values.append(value_array[inner_idx])
                    pass
                else:
                    loot(inner_idx, ei, array, value_array)
                    values.append(value_array[inner_idx])
            maximum = max(values)
            value_array[idx] = maximum + array[idx]


n = 7
value_array = [0 for i in range(7)]
data = [6, 7, 1, 3, 8, 2, 4]
loot(0, 7, data, value_array)
print value_array


def loot_effective(array):
    dp = []
    dp.append(array[0])
    dp.append(array[1])
    for i in range(2, len(array)):
        dp.append(max(dp[i - 2] + array[i], dp[i - 1]))
    return dp[-1]


print loot_effective(data)


def loot_temp(array):
    dp = []
    dp.append(array[0])
    dp.append(array[1])
    for i in range(1, n):
        dp.append(max(dp[i - 2]) + array[i])
    return max(dp)
def loot_recursive(array):
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return max(array)
    else:
        include = array[0] + loot_recursive(array[2:])
        exclude = loot_recursive(array[1:])
        return max(include, exclude)


print loot_recursive(data)
