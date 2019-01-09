def find_permutations(array1, array2):
    permutations = []
    for i in array1:
        for j in array2:
            if i < j:
                permutations.append((i, j))
            else:
                permutations.append((j, i))
    return permutations
