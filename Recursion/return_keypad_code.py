dict = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'], 9: ['x', 'y', 'z'], 0: [""], 1: [""]}


def return_keypad(array):
    if len(array) == 1:
        return dict[array[0]]
    else:
        small_output = return_keypad(array[1:])
        new_list = []
        for i in dict[array[0]]:
            for j in small_output:
                new_list.append(i + j)
        return new_list


a = 50
arr = []
while a > 10:
    arr.insert(0, a % 10)
    a /= 10
arr.insert(0, a)
print return_keypad(arr)
