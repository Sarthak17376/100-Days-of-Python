from menu import MenuItem, Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


money_machine.report()
coffee_maker.report()

turned_on = True

while turned_on:
    options = menu.get_items()
    choice = input(f"What would you like to do? ({options}report/Off) ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "Off":
        turned_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
