def bubble_sort(array):
    for i in range(0,len(array)-1):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
              array[j],array[j+1]=array[j+1],array[j]
    return array
# print bubble_sort([7,2,1])
# print bubble_sort([0,0,0,5,0])
print bubble_sort([21,4,1,3,9,20,25,6,21,14])