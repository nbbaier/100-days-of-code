from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True
while is_on:
    order = input(f"What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        machine.report()
        money_machine.report()

    else:
        drink = menu.find_drink(order)
        if machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                machine.make_coffee(drink)