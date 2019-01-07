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
