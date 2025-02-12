import string
import random

symbols = ['!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '_', '=', '+', '°',
           '§', '?', '/', '\\', ',', '.', '<', '>', 'º', 'ª', '{', '}', '[', ']', '`', '´', '^', '~', "'", '"',
           '¹', '²', '³', '£', '¢', '¬']
letters = list(string.ascii_letters)
numbers = list(string.digits)

n_letters = ""
n_symbols = ""
n_numbers = ""

print('Welcome to the PyPassword Generator!')

while not n_letters.isnumeric():
    n_letters = input('How many letters would you like in your password?\n')
    if not n_letters.isnumeric():
        print('Invalid value, please try again.')
n_letters = int(n_letters)
print(n_letters)

while not n_symbols.isnumeric():
    n_symbols = input('How many symbols would you like in your password?\n')
    if not n_symbols.isnumeric():
        print('Invalid value, please try again.')
n_symbols = int(n_symbols)

while not n_numbers.isnumeric():
    n_numbers = input('How many numbers would you like in your password?\n')
    if not n_numbers.isnumeric():
        print('Invalid value, please try again.')
n_numbers = int(n_numbers)

password = []
for i in range(n_letters):
    password.append(random.choice(letters))
for i in range(n_numbers):
    password.append(random.choice(numbers))
for i in range(n_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
print('Your password is:', ''.join(password))