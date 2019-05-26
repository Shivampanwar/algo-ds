'''

    Given an array of integers of size n which contains
    numbers from 0 to n - 2. Each number is present at least once.
    That is, if n = 5, numbers from 0 to 3 is present in the given array at
    least once and one number is present twice. You need to find and return
    that duplicate number present in the array.
    Assume, duplicate number is always present in the array.
'''



import sys

n = int(input())
array = input().split(" ")
print ("\n")
for i in array:
    sys.stdout.write(str(i))
    sys.stdout.write(" ")
new_array = [0] * n
for element in array:
    if new_array[int(element)] == 1:
        print ("\n")
        print (element)
        break
    else:
        new_array[int(element)] = 1
