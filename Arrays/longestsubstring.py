def substring(array):
    max = 0
    main_string = ""
    i = 0
    while i < len(array) - 1:
        j = i + 1
        temp = 0
        tempstring = array[i]
        while array[j] != array[i] and j < len(array):
            print tempstring
            temp += 1
            j += 1
            tempstring += array[j]
        if temp > max:
            main_string = tempstring
            max = temp
        i += 1
    return main_string


print substring("abcdd")
