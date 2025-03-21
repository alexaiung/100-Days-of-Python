from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True
while is_on:
    order_name = input(f'What drink would you like? {menu.get_items()} ')
    if order_name == 'off':
        is_on = False
    elif order_name == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
