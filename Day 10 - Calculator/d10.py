def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

should_continue = False
result = 0

while True:
    n2 = ''
    operation = ''
    if not should_continue:
        n1 = ""
        while not n1.isdecimal():
            n1 = input('Insert the first number: ')
            if not n1.isdecimal():
                print('Invalid value, please try again')
        n1 = float(n1)
    while not n2.isdecimal():
        n2 = input('Insert the second number: ')
        if not n2.isdecimal():
            print('Invalid value, please try again')
    n2 = float(n2)
    while operation not in ['+', '-', '*', '/']:
        operation = input('Insert the operation: ')
        if operation not in ['+', '-', '*', '/']:
            print('Invalid operation, please try again')
    result = operations[operation](n1, n2)
    print('Result:', result)

    while should_continue not in ['y', 'n', 't']:
        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 't' to terminate the calculator: ").lower()
        if should_continue not in ['y', 'n', 't']:
            print('Invalid answer, please try again')
    if should_continue == 'y':
        n1 = result
        should_continue = True
    elif should_continue == 't':
        break
    else:
        should_continue = False

