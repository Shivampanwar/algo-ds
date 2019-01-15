# You are given with an array (of size N) consisting of positive and
# negative integers that contain numbers in random order.
# Write a program to return true if there exists a sub-array
# whose sum is zero else, return false.

# Logic: consider an array, for each element you are calculating the sum the sum till this point say for array[5]
# is 50 now between, arr[5] and arr[8] sum is zero. now again for arr[9] sum will be same as arr[5]

def find_zero_in_array(array):
    has_zero = False
    dict = {}
    sum = 0
    for i in range(len(array)):
        sum += array[i]
        if sum in dict or sum == 0:
            has_zero = True
            break
        dict[sum] = 1
    return has_zero


print find_zero_in_array([1, 3, -4, 5, 1])
