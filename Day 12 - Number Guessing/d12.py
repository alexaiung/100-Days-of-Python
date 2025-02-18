from random import randint
from logo import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty(difficulty):
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def play_game():
    print(logo)
    print('Welcome to the number guessing game!')
    print("I'm thinking on a number between 1 and 100.")
    answer = randint(1, 100)
    print(f'Psst, the correct answer is {answer}')
    difficulty = ''
    while difficulty not in ['easy', 'hard']:
        difficulty = input('Choose a difficulty. Type "easy" or "hard": ').lower()
        if difficulty not in ['easy', 'hard']:
            print('Invalid answer, try again')
    turns = set_difficulty(difficulty)

    while turns > 0:
        print(f'You have {turns} attempts left to guess the number.')
        guess = 0
        while guess not in [str(i) for i in list(range(1, 101))] or not guess.isdecimal():
            guess = input('Make a guess: ')
            if guess not in [str(i) for i in list(range(1, 101))] or not guess.isdecimal():
                print('Invalid answer, try again')
        guess = int(guess)
        if guess == answer:
            print('Oh my! You guessed correctly!')
            break
        else:
            turns -= 1
            if guess > answer:
                print('Too high.')
            else:
                print('Too low.')
        if turns == 0:
            print('You lost.')

play_game()