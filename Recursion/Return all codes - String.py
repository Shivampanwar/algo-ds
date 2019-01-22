dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
        14: 'n'
    , 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}


def all_codes(a):
    if len(a) == 1:
        return [dict[int(a[0])]]
    if len(a) == 0:
        return []
    else:
        temp = []
        small_values = all_codes(a[1:])
        first = a[0]
        for i in small_values:
            temp.append(dict[int(first)] + i)
        small2 = []
        count = 10 * first + a[1]
        if count < 27:
            small2 = all_codes(a[2:])
            if len(small2) is 0:
                temp.append(dict[int(count)])
        for i in small2:
            temp.append(dict[int(count)] + i)
        return temp


a = int(input())
arr = []
while a >= 10:
    arr.append(a % 10)
    a /= 10
arr.append(a)
result = all_codes(arr[::-1])
for i in result:
    print (i)
