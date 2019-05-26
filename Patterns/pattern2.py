import sys
def pattern(n):
    for i in range(1,n+1):

        for j in range(1,n-i+1):
            sys.stdout.write(" ")
        for j in range(i,2*i):
            sys.stdout.write(str(j))
        print "\n"
pattern()