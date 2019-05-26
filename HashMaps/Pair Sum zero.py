import sys


def findsumtozero(array):
    dictionary = {}
    for i in array:
        if i in dictionary.keys():
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    print dictionary
    for i in dictionary.keys():
        if -1 * i in dictionary.keys():
            pairs = abs(dictionary[i] * dictionary[-i])
            dictionary[i] = 0
            for j in range(pairs):
                a = abs(i)
                sys.stdout.write(str(-a))
                sys.stdout.write(" ")
                sys.stdout.write(str(a))
                print ("\n")


findsumtozero([-4, 4, 25, -25, 50, 4, 25, 12, -12])
