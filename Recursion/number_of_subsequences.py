def num_subsequences(string):
    if len(string) == 1:
        return [string]
    else:
        smaller_subsequences = num_subsequences(string[1:])
        new_subsequences = [string[0] + i for i in smaller_subsequences]
        new_subsequences.append(string[0])
        smaller_subsequences.extend(new_subsequences)
        return smaller_subsequences


print len(num_subsequences('abcd'))
