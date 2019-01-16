def is_sorterd(array):
    if len(array) == 0 or len(array) == 1:
        return True
    else:
        if array[0] <= array[1]:
            return is_sorterd(array[1:])
        else:
            return False


print is_sorterd([5])
