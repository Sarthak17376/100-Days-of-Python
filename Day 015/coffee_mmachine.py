from database import menu, resources


def refill():  # refilling the resources
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100


def report():  # generating report
    print(f"Water : {resources['water']}")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")


def resource_adjustment(choice_of_coffee):
    resources['water'] -= menu[choice_of_coffee]['ingredients']['water']
    resources['milk'] -= menu[choice_of_coffee]['ingredients']['milk']
    resources['coffee'] -= menu[choice_of_coffee]['ingredients']['coffee']


def coffee_machine():
    choice_of_service = input("Do you want a report/refill/order? ".lower())
    if choice_of_service == "report":
        report()
        coffee_machine()
    elif choice_of_service == "refill":
        refill()
        coffee_machine()
        print("Resources have been refilled!!")
    elif choice_of_service == "order":
        coffee_order = input("What would you like to order(espresso/latte/cappuccino)? ".lower())
        if menu[coffee_order]["ingredients"]["water"] < resources["water"] and \
                menu[coffee_order]["ingredients"]["milk"] < resources["milk"] and \
                menu[coffee_order]["ingredients"]["coffee"] < resources["coffee"]:
            total = int(input("How many Rs. 500 note did you want to give? "))*500 + \
                        int(input("How many Rs. 200 note did you want to give? "))*200 + \
                        int(input("How many Rs. 100 note did you want to give? "))*100 + \
                        int(input("How many Rs. 50 note did you want to give? "))*50 + \
                        int(input("How many Rs.20 note did you want to give? "))*20 + \
                        int(input("How many Rs. 10 note did you want to give? "))*10
            if total < menu[coffee_order]["cost"]:
                print(f"Sorry Sir/Mam, not enough money, you need to give Rs.{menu[coffee_order]['cost'] - total} more")
            else:
                resource_adjustment(coffee_order)
                print(f'''Here is your {coffee_order}, and our change of Rs.{total - menu[coffee_order]['cost']}. Enjoy
                your coffee!!!''')
            coffee_machine()
        else:
            print("Not enough Resources!")
            if(input("Would you like to refill(Y/N)? ".lower())) == "y":
                refill()
            coffee_machine()


coffee_machine()
