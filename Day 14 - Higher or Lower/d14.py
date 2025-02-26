from art import logo, versus
import random
from game_data import data

def format_data(person):
    return f"{person['name']}, a {person['description']} from {person['country']}"

print(logo)
print('Welcome to the Higher or Lower Game!')
score = 0
person_b = ""
person_a = random.choice(data)

while True:
    print ('*' * 50)
    if score > 0:
        person_a = person_b
        print("You're right! Current score:", score)
    print(f"Compare A: {format_data(person_a)}")
    print(versus)
    person_b = random.choice(data)
    while person_a == person_b:
        person_b = random.choice(data)
    print(f"Against B: {format_data(person_b)}")

    guess = ""
    while guess not in ['A', 'B']:
        guess = input('Who has more followers? Type "A" or "B": ').upper()
        if guess not in ['A', 'B']:
            print('Invalid answer, try again.')

    if person_b['follower_count'] > person_a['follower_count']:
        answer = 'B'
    else:
        answer = 'A'

    if guess == answer:
        score += 1

    else:
        print("Sorry, you're wrong. Final score:", score)
        break