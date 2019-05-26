def make_dict(str2):
    dict = {}
    for i in str2:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    dict[" "] = 1
    return dict


def checkifnull(dict):
    dict[" "] = 0
    for key in dict:
        if dict[key] is not 0:
            return False
    return True


def checksub(str1, str2):
    dict = make_dict(str2)
    temp = ""
    list = []
    for i in range(len(str1)):
        if str1[i] in dict:
            dict[str1[i]] += -1
            temp += str1[i]
            if checkifnull(dict):
                return temp
        else:
            dict = make_dict(str2)
            temp = ""
    count = 1000
    temp_word = ""
    for i in list:
        if len(i) < count:
            temp_word = i
            count = len(i)
    return temp_word


print checksub('gjhtywoocjledxsfexehpfgywjpcvllbsmxkpfqlgoampuqngsxv', 'oav')
