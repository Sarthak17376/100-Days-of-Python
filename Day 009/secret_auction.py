#      ___________
#      \         /
#       )_______(
#       |"""""""|_.-._,.---------.,_.-._
#       |       | | |               | | ''-.
#       |       |_| |_             _| |_..-'
#       |_______| '-' `'---------'` '-'
#       )"""""""(
#      /_________\\
#    .-------------.
#   /_______________\\


import os

auction_list = {}
highest = 0
highest_key = ""

while True:
    name = input("What is your Name?\n")
    bid = int(input("What is your bid?\n$"))
    auction_list[name] = bid
    if highest < bid:
        highest = bid
        highest_key = name
    next_one = input("Is there anyone else?(Y/N)\n".lower())
    print(next_one)
    if next_one == "y":
        os.system('cls')
    elif next_one == "n":
        os.system('cls')
        break


print(f"The winner is {highest_key} with a bid of {highest}")
