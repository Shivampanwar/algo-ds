import sys


def break_word(string):
    words_list = string.strip().split(" ")

    for i in range(len(words_list)):
        length = len(words_list[i])
        if length % 2 == 0 and length >= 4:
            word = words_list[i][:length / 2] + " " + words_list[i][length / 2:]
            words_list[i] = word
    return words_list


print break_word('Helloo shivam world good morniing')
sys.stdout.write()
