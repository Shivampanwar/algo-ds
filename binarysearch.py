def binsearch_loop(array,value):
    start=array[0]
    end=len(array)-1
    while start<=end:
        mid=(start+end)/2
        if array[mid]==value:
            return mid
        elif array[mid]>value:
            end=mid-1
        else:
            start=mid+1

    return -1

test_list = [1,3,9,11,15]
print binsearch_loop(test_list,6)
print binsearch_loop(test_list,15)#