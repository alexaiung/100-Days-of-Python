from random import choice

rock_ascii = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper_ascii = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
ascii_dict = {'rock': rock_ascii, 'paper': paper_ascii, 'scissors': scissors_ascii}
print("Welcome to the World Tournament of Rock, Paper, Scissors! This is the final match!")
print("What do you choose?")
player_choice = ""
options = ['rock', 'paper', 'scissors']
while player_choice not in options:
    player_choice = input('Type your choice (rock, paper, or scissors): ').lower()
    if player_choice not in options:
        print('Please, type a valid answer!')
computer_choice = choice(options)
print(f'Player chooses: {player_choice}')
print(ascii_dict[player_choice])
print()
print(f'Computer chooses: {computer_choice}')
print(ascii_dict[computer_choice])
if player_choice == computer_choice:
    print('Draw!')
    win = 'na'
elif player_choice == 'rock':
    if computer_choice == 'paper':
        win = False
    else:
        win = True
elif player_choice == 'paper':
    if computer_choice == 'rock':
        win = True
    else:
        win = False
else:
    if computer_choice == 'paper':
        win = True
    else:
        win = False

if win != 'na':
    if win:
        print(f'Player wins! {player_choice.capitalize()} beats {computer_choice}')
    else:
        print(f'Sorry, the computer wins! {computer_choice.capitalize()} beats {player_choice}!')
