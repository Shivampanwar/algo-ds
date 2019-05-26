def min_count(n):
    if n == 1:
        return 1
    else:
        sqrt = int(pow(n, 0.5))
        if sqrt * sqrt == n:
            return 1
        small_output = min_count(n - sqrt * sqrt)
        return 1 + small_output


def min_count_standard(n):
    if n == 1:
        return 1
    else:
        sub_list = []
        i = 1
        while (n - i * i) >= 0:
            if n - i * i == 0:
                return 1
            small_output = min_count_standard(n - i * i)
            i += 1
            sub_list.append(small_output)
        return min(sub_list) + 1


print min_count_standard(6)
