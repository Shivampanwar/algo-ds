import sys


def print_sequence(n):
    if n <= 0:
        # sys.stdout.write(str(n)+" ")
        return
    else:
        print_sequence(n - 1)
        sys.stdout.write(str(n) + " ")


print_sequence(6)
