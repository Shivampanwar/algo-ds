def combination_of_words(word):
    '''

    :param word: makes all the possible combination from word
    :return:
    '''
    word_list = []
    i = 1
    while i < len(word):
        if word[i] == 'b':
            i += 2
        else:
            word_list.append(word[:i] + 'b' + word[i:])
            i += 1
    if word[0] == 'w':
        word_list.append('r' + word)
    else:
        word_list.append('w' + word)
    if word[-1] == 'r':
        word_list.append(word + 'w')
    else:
        word_list.append(word + 'r')
    return word_list



def possible_flags(n):
    if n == 1:
        return ['r', 'w']
    else:
        main_list = []
        small_output = possible_flags(n - 1)
        for i in small_output:
            main_list.extend(combination_of_words(i))
        return list(set(main_list))


print len(possible_flags(4))
#
