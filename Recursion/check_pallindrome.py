def is_pallindrome(array):
    if len(array) == 1:
        return True
    if len(array) == 2:
        if array[0] == array[1]:
            return True
        else:
            return False
    else:
        short_pallindrome = is_pallindrome(array[1:-1])
        return array[0] == array[-1] and short_pallindrome


print is_pallindrome('nijhin')
