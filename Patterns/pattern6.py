import sys


def pattern(n):
    if n % 2 == 1:
        end_list = []
        i = 1
        while i <= n:
            end_list.append(i)
            i += 2
        i = n - 1

        while i >= 2:
            end_list.append(i)
            i += -2
        for element in end_list:
            start = n * element - n + 1
            end = n * element
            for i in range(start, end + 1):
                sys.stdout.write(str(i))
                sys.stdout.write(" ")
            print ("\n")
    if n % 2 == 0:
        end_list = []
        i = 1
        while i < n:
            end_list.append(i)
            i += 2
        i = n
        while i >= 2:
            end_list.append(i)
            i += -2
        for element in end_list:
            start = n * element - n + 1
            end = n * element
            for i in range(start, end + 1):
                sys.stdout.write(str(i))
                sys.stdout.write(" ")
            print ("\n")


pattern(4)
