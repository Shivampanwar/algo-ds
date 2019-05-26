# def count_pallindromes(word):
#     count =0
#     for i in range(len(word)):
#         for j in range(i+1,len(word)):
#             if word[i:j+1]==word[i:j+1][::-1]:
#                 print word[i:j+1]
#                 count+=1
#     return count+len(word)
def count_pallindromes(word):
    count = 0
    for i in range(len(word)):
        count += 1
        mid = i
        left = mid - 1
        right = mid + 1
        while left >= 0 and right <= len(word) - 1:
            if word[left] == word[right]:
                count += 1
                left += -1
                right += 1
            else:
                break
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
            left = i - 1
            right = i + 2
            while left >= 0 and right <= len(word) - 1:
                if word[left] == word[right]:
                    count += 1
                    left += -1
                    right += 1
                else:
                    break
    return count


print count_pallindromes('abaab')
