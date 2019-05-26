def bubble_sort_recusrion(array,start,end):
    ''''
        start is the start index of array
        end is the end index of array
    '''
    if start==end:
        return array
    else:
        for i in range(start,end):
            if array[i]>array[i+1]:
              array[i],array[i+1]=array[i+1],array[i]
        return bubble_sort_recusrion(array,start,end-1)

print bubble_sort_recusrion([7,2,1,11,20,5],0,5)