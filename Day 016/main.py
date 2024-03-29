from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

print("Available Resources : ")
money_machine.report()
coffee_maker.report()

is_on = True

while is_on:
    options = menu.get_items()
    order = input(f"What would you like? ({options}) : ").lower()
    if order == "off":
        is_on = False
        break
    elif order == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print("Sorry!! Not enough Resources :(")
            continue

