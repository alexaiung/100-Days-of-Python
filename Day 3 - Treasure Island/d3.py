from treasure_island_art import logo, treasure, death

print(logo)

choice = ""
game_over = False
print("*" * 50)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
while choice not in ['left', 'right']:
    choice = input("\tType 'left' or 'right'\n").lower()
    if choice not in ['left', 'right']:
        print("Invalid answer, try again")
if choice == 'right':
    print("Oh, no! There are bandits looking for the treasure and they do not want competitors or survivors!")
    game_over = True

if not game_over:
    print("You've come to a lake. There is an island "
          "in the middle of the lake")
    while choice not in ['wait', 'swim']:
        choice = input("\t Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
        if choice not in ['wait', 'swim']:
            print("Invalid answer, try again")
if choice == 'swim':
    print("Did you even care to check the water? There are crocodiles! They swiftly get to you!")
    game_over = True

if not game_over:
    print('You arrive at the island unharmed. There is a house with 3 doors.')
    while choice not in ['red', 'yellow', 'blue']:
        choice = input('\tOne red, one yellow and one blue. Which colour do you choose? ')
        if choice not in ['red', 'yellow', 'blue']:
            print("Invalid answer, try again")
if choice != 'yellow':
    if choice == 'red':
        print('A towering rage of fire flows to you! It burns you!')
    elif choice == 'blue':
        print('As you touch the doorknob, you are electrocuted to death!')
    game_over = True

if not game_over:
    print("Congratulations! You found the treasure! Rejoice!")
    print(treasure)
else:
    print("I'm sorry, but you died! Game Over!")
    print(death)