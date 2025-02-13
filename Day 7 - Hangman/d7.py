from random_word import RandomWords
from hangman_art import hangman

# Define the word to be guessed
r = RandomWords()
word = r.get_random_word()
trials_left = 6
printed_word = len(word) * '_'

print('Welcome to the Hangman Game!')
print('-' * 50)
print(hangman[trials_left])
while trials_left > 0:
    print(printed_word)
    letter = ""
    while len(letter) != 1 or not letter.isalpha():
        letter = input('Please insert a letter: ').lower()
        if not letter.isalpha():
            print('Invalid value, please insert a valid letter')
        elif len(letter) == 0:
            print('Please insert a letter')
    if letter in word:
        if letter in printed_word:
            print('You already chose this letter! Please, choose another one')
        else:
            print('Alright!')
            positions = [i for i, x in enumerate(list(word)) if str(x) == letter]
            printed_word = list(printed_word)
            for position in positions:
                printed_word[position] = letter
            printed_word = ''.join(printed_word)
    else:
        trials_left -= 1
        print(hangman[trials_left])
        if trials_left == 0:
            print('You lost :(')
            print('The word was', word)

    if word == printed_word:
        print(printed_word)
        print('Congratulations, you discovered the word and escaped!')
        break
    print('-' * 50)
