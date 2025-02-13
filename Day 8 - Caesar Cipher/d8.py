from string import ascii_lowercase

def apply_caesar_cipher(word, shift):
    ciphered_word = []
    for letter in list(word.lower()):
        new_letter_position = list(ascii_lowercase).index(letter) + int(shift)
        if new_letter_position >= len(ascii_lowercase):
            new_letter_position -= len(ascii_lowercase)
        ciphered_word += list(ascii_lowercase)[new_letter_position]
    return ''.join(ciphered_word)

word = ""
shift = ""
while not word.isalpha():
    word = input("Insert the word you'd like to ciphered: ")
    if not word.isalpha():
        print('Please insert a valid word')
while not shift.isnumeric():
    shift = input("Insert how shifted you would want: ")
    if not shift.isnumeric():
        print('Please insert a valid number')
print(apply_caesar_cipher(word, shift))

