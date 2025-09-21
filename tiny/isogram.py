# while True:
#     str = input("word: ")

#     for val, letter in enumerate(str):
#         if letter in str[val+1:]:
#             print('no')
#             break
#     else:
#         print('yes')

def Isogram(word):
    letter_count = {}

    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1

        else: 
            letter_count[letter] = 1

    for count in letter_count.values():
        if count > 1:
            return False
    return True

word = input('Enter a word: ')
if Isogram(word):
    print(f'{word} is an isogram')
else:
    print(f'{word} is not an isogram')