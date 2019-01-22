def makelistofstrings(word, before, alphabet):
    '''
    :param word: main word in wich we need to insert alphabet
    :param before: alphabet to be inserted vefore this word
    :param alphabet: main alphabet to be inserted
    :return:
    '''
    index = word.find(before)
    if index is not -1:
        listofwords = []
        pos = 0
        while pos <= index:
            temp_word = word[:pos] + alphabet + word[pos:]
            pos += 1
            listofwords.append(temp_word)
        return listofwords
    else:
        listofwords = []
        pos = 0
        while pos <= len(word):
            temp_word = word[:pos] + alphabet + word[pos:]
            pos += 1
            listofwords.append(temp_word)
        return listofwords


# def interleaves(str1,str2):
#     if len(str1)==1:
#         temp_list=makelistofstrings(str2,str1,str1)
#         return temp_list
#     else:
#         small_output=interleaves(str1[-1],str2)
#         print "HII"+str(small_output)
#         new_list=[]
#         for i in small_output:
#             new_list.extend(makelistofstrings(i,str1[-1],str1[-2]))
#         return new_list

def interleaves(str1, str2):
    if len(str1) == 1:
        return makelistofstrings(str2, str1, str1)
    else:
        alphabet = str1[0]
        before = str1[1]
        small_output = interleaves(str1[1:], str2)
        new_list = []
        for i in small_output:
            new_list.extend(makelistofstrings(i, before, alphabet))
        return new_list


a = interleaves('ac', 'f')
print a
