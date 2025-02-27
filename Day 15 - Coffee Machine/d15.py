from main import resources, MENU

def get_report(machine):
    for key, item in machine.items():
        print(key.capitalize(), '-', item)

def calculate_money(pennies=0, nickels=0, dimes=0, quarters=0):
    money = 0
    money += pennies * 0.01
    money += nickels * 0.05
    money += dimes * 0.10
    money += quarters * 0.25
    return money

def generate_coffee(current_resources, beverage):
    if 'water' in beverage['ingredients'].keys():
        current_resources['water'] -= beverage['ingredients']['water']
    if 'coffee' in beverage['ingredients'].keys():
        current_resources['coffee'] -= beverage['ingredients']['coffee']
    if 'milk' in beverage['ingredients'].keys():
        current_resources['milk'] -= beverage['ingredients']['milk']

    if current_resources['water'] < 0:
        return False, 'water'
    elif current_resources['coffee'] < 0:
        return False, 'coffee'
    elif current_resources['milk'] < 0:
        return False, 'milk'
    else:
        return True, current_resources

machine = resources
keep_going = True

while keep_going:
    required_beverage = input('What would you like? (espresso, latte, cappuccino) ').lower()
    if required_beverage == 'off':
        keep_going = False
        print('Shutting off...')
    elif required_beverage in ['espresso', 'latte', 'cappuccino', 'report']:
        if required_beverage == 'report':
            get_report(machine)
        else:
            print('Please insert coins.')
            quarters, dimes, nickels, pennies = '', '', '', ''
            while not quarters.isdecimal():
                quarters = input('How many quarters? ')
                if not quarters.isdecimal():
                    print('Invalid value, please try again.')
            while not dimes.isdecimal():
                dimes = input('How many dimes? ')
                if not dimes.isdecimal():
                    print('Invalid value, please try again.')
            while not nickels.isdecimal():
                nickels = input('How many nickels? ')
                if not nickels.isdecimal():
                    print('Invalid value, please try again.')
            while not pennies.isdecimal():
                pennies = input('How many quarters? ')
                if not pennies.isdecimal():
                    print('Invalid value, please try again.')
            money = calculate_money(int(pennies), int(nickels), int(dimes), int(quarters))
            cost = MENU[required_beverage]['cost']
            if money >= cost:
                if money > cost:
                    enough_resources, new_resources =  generate_coffee(machine.copy(), MENU[required_beverage])
                    if enough_resources:
                        change = money - cost
                        print(f'Here is ${change:.2f} in change.')
                        machine = new_resources
                        print(f'Here is your {required_beverage}. Enjoy!')
                    else:
                        print(f"Sorry, there isn't enough {new_resources} for this beverage in the machine. Refunding money...")
            else:
                print("Sorry, that's not enough money. Refunding...")
    else:
        print('Invalid answer, please try again.')