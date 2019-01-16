def check_number(array, k):
    if len(array) == 1:
        if array[0] == k:
            return True
        else:
            return False
    else:
        if array[0] == k:
            return True
        else:
            return check_number(array[1:], k)


print str(check_number([1, 5, 8, 2], 6)).lower()
