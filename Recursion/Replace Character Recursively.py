import re


def replaceChar(inval, old, new):
    if inval == '':
        return ''
    if inval[0] == old:
        return new + replaceChar(inval[1:], old, new)
    return inval[0] + replaceChar(inval[1:], old, new)


print replaceChar('abac', 'a', 'x')
s = "abbac"
replaced = re.sub('a', 'x', s)
print  replaced
