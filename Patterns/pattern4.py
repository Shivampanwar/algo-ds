import sys
def pattern(n):
    for i in range(1,n/2+2):
        initial_space=i-1
        for j in range(1,initial_space+1):
            sys.stdout.write(" ")
        for j in range(1,2*i+1):
            if j%2!=0:
                sys.stdout.write("*")
            else:
                sys.stdout.write(" ")
        print "\n"
    initial_space=n/2-1
    num_stars=n/2
    for i in range(n/2+2,n+1):
        for j in range(1,initial_space+1):
            sys.stdout.write(" ")
        for j in range(1,2*num_stars+1):
            if j%2!=0:
                sys.stdout.write("*")
            else:
                sys.stdout.write(" ")
        num_stars-=1
        initial_space-=1
        print ("\n")
n=input()
pattern(int(n))