def unique_substring(arr):
    print len(arr)
    currentIndex = startIndex = count = fi = li = 0
    dict = {}
    while currentIndex < len(arr):
        while (currentIndex < len(arr)) and (arr[currentIndex] not in dict or dict[arr[currentIndex]] < startIndex):
            dict[arr[currentIndex]] = currentIndex
            currentIndex += 1
        if currentIndex - startIndex > count:
            fi = startIndex
            li = currentIndex
            count = currentIndex - startIndex
        if currentIndex < len(arr):
            startIndex = dict[arr[currentIndex]] + 1
            dict[arr[currentIndex]] = currentIndex
        currentIndex += 1
    return arr[fi:li]


print unique_substring("uhuchwucdshhdbhjcdchbbdhdb")
