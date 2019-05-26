import sys
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            sys.stdout.write(' ')
        temp=[]
        for j in range(i,2*i):
            sys.stdout.write(str(j))
        for j in range(2*i-2,i-1,-1):
            sys.stdout.write(str(j))
        for j in range(1,n-i+1):
            sys.stdout.write(' ')

n=input()
pattern(int(n))