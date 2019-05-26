import sys
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            sys.stdout.write(str(j))
        for j in range(1,2*n-2*i+1):
            sys.stdout.write(" ")
        for j in range(i,0,-1):
            sys.stdout.write(str(j))
        print "\n"
pattern(4)