def NoofAPs(array):
    if len(array) == 1:
        return [array]
    else:
        small_output = NoofAPs(array[1:])
        temp_list = []
        for i in small_output:
            if len(i) == 1:
                temp_list.append([array[0]] + i)
            else:
                if i[1] - i[0] == i[0] - array[0]:
                    temp_list.append([array[0]] + i)
            temp_list.append(i)
        temp_list.append([array[0]])
        return temp_list


print  NoofAPs([2, 4, 2])
# {}, {2}, {4}, {2}, {2, 4}, {4,2}, {2, 2}
