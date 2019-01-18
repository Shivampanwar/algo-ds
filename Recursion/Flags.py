def combination_of_words(word):
    '''

    :param word: makes all the possible combination from word
    :return:
    '''
    word_list = []
    if len(word) == 2:
        return [word[0] + 'b' + word[1]]
    for i in range(1, len(word)):
        if word[i] == 'b':
            pass
        else:
            if word[i - 1] == 'b':
                pass
            else:
                word_list.append(word[:i] + 'b' + word[i:])
    return word_list


print combination_of_words('rbwrwbr')


def possible_flags(n):
    if n == 1:
        return ['r', 'w']
    else:
        main_list = []
        small_output = possible_flags(n - 1)
        for i in small_output:
            main_list.extend(combination_of_words(i))
        # print main_list
        return list(set(main_list))
# print possible_flags(4)
