import sys
def pattern(n):
    big_array=[]
    for i in range(1,n+1):
        array=[0]*(2*n-1)
        num_unique=i
        index=0
        value=n
        while num_unique>1:
            array[index]=value
            array[len(array)-1-index]=value
            value+=-1
            index+=1
            num_unique+=-1
        for j in range(index,len(array)-index):
            array[j]=value
        big_array.append(array)
    index+=-1
    while index!=-1:
        big_array.append(big_array[index])
        index+=-1
    for i in big_array:

        for j in i:
            sys.stdout.write(str(j))
        print ("\n")
    # return big_array

pattern(5)