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


auction_list = {}
import os
clear = lambda: os.system('cls')

for list in range(100):
    name = input("What is your Name?\n")
    bid = int(input("What is your bid?\n$"))
    auction_list[name] = bid
    next_one = input("Is there anyone else?(Y/N)\n")
    if next_one=="Y":
        clear()
    elif next_one=="N":
        clear()
        break

highest = 0
highest_key = ""

for keys in auction_list:
    if auction_list[keys]>highest:
        highest = auction_list[keys]
        highest_key = keys

print(f"The winner is {highest_key} with a bid of {highest}")
