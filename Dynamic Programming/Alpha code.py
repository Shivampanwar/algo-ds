'''

    Alice and Bob need to send secret messages to each other and are discussing ways to encode their messages:
Alice: “Let’s just use a very simple code: We’ll assign ‘A’ the code word 1, ‘B’ will be 2, and so on down to ‘Z’ being assigned 26.”

Bob: “That’s a stupid code, Alice. Suppose I send you the word ‘BEAN’ encoded as 25114. You could decode that in many different ways!”

Alice: “Sure you could, but what words would you get? Other than ‘BEAN’, you’d get ‘BEAAD’, ‘YAAD’, ‘YAN’, ‘YKD’ and ‘BEKD’. I think you would be able to figure out the correct decoding. And why would you send me the word ‘BEAN’ anyway?”

Bob: “OK, maybe that’s a bad example, but I bet you that if you got a string of length 5000 there would be tons of different decodings and with that many you would find at least two different ones that would make sense.”

Alice: “How many different decodings?”

Bob: “Jillions!”
For some reason, Alice is still unconvinced by Bob’s argument, so she requires a program that will determine how many decodings there can be for a given string using her code.
Input
Input will consist of multiple input sets. Each set will consist of a single line of at most 5000 digits representing a valid encryption (for example, no line will begin with a 0). There will be no spaces between the digits. An input line of ‘0’ will terminate the input and should not be processed.
Output
For each input set, output the number of possible decodings for the input string. Print your answer taking modulo "10^9+7"
'''

'''
    Sample Input:
25114
1111111111
3333333333
0
Sample Output:
6
89
1
'''

def all_codes(array, size_array):
    if len(array) == 0:
        return 1
    if len(array) == 1:
        return 1
    else:
        length = len(array)
        if size_array[length] is not 0:
            return size_array[length]
        else:
            small_output = all_codes(array[1:], size_array)
            if 10 * array[0] + array[1] < 27:
                small_output += all_codes(array[2:], size_array)
            size_array[length] = small_output
            return small_output


def all_codes_proper_dp(array):
    if len(array) == 1:
        return 1
    if len(array) == 0:
        return 1
    else:
        temp_array = []
        temp_array.append(1)
        temp_array.append(1)
        for i in range(2, len(array) + 1):
            temp = temp_array[i - 1]
            numbers = array[-i:]
            k = numbers[0] * 10 + numbers[1]
            if k < 27:
                temp += temp_array[i - 2]
            temp_array.append(temp)
        return temp_array[-1]


# a = str(input())
# while int(a) is not 0:
#     arr = [int(x) for x in a]
#     size_array = []
#     size_array.append(0)
#     for i in range(len(arr) + 1):
#         size_array.append(0)
#     result = all_codes(arr, size_array)
#     print (result)
#     a = str(input())
a = str(input())
while int(a) is not 0:
    arr = [int(x) for x in a]
    result = all_codes_proper_dp(arr)
    print (result)
    a = str(input())
# inp=str(input())
# list_word=inp.split(" ")
# for i in list_word:
#     if int(i)==0:
#         break
#     else:
#         arr = [int(x) for x in i]
#         size_array = []
#         size_array.append(0)
#         for i in range(len(arr) + 1):
#             size_array.append(0)
#         result = all_codes(arr, size_array)
#         print (result)
