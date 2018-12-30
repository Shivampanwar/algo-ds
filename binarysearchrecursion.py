def binary_search_rec(array,value,start,end):
    if start<=end:
        mid=(start+end)/2
        if array[mid]<value:
            start=mid+1
            return binary_search_rec(array,value,start,end)
        elif array[mid]>value:
            end=mid-1
            return binary_search_rec(array,value,start,end)
        else:
            return mid
    else:
        return -1

test_list = [1,3,9,11,15]
print binary_search_rec(test_list,6,0,len(test_list)-1)
print binary_search_rec(test_list,15,0,len(test_list)-1)#
print binary_search_rec(test_list,1,0,len(test_list)-1)#
