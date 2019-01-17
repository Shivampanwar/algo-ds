def replacepi(array):
    if len(array) == 1 or len(array) == 0:
        return array
    else:
        if array[:2] == 'pi':
            small_output = replacepi(array[2:])
            return '3.14' + small_output
        else:
            small_output = replacepi(array[1:])
            return array[0] + small_output


print replacepi('pipi')
