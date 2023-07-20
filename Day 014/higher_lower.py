from database import data
import random
import os

# Welcome to the Higher Lower Game
game_logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def higher_lower(Database):
    def format_of_data(account):
        name = account['name']
        info = account['description']
        nationality = account['country']

        return f"{name}, is {info} from {nationality}"

    random_account = random.choice(Database)
    follower_Count_A = random_account['follower_count']
    print(game_logo)
    A = f"Compare A: {format_of_data(random_account)}, Follower Count: {follower_Count_A}"
    print(A)
    correct = True
    count = 0

    while correct:
        print(vs)
        random_account = random.choice(Database)
        follower_Count_B = random_account['follower_count']
        B = f"{format_of_data(random_account)}"
        print(f"Against B: {B}")
        answer = input("Who has more followers, A or B?\n")
        if (answer == "A" and follower_Count_A > follower_Count_B) or (
                answer == "B" and follower_Count_A < follower_Count_B):
            count += 1
            A = f"Compare A: {B}, Follower Count: {follower_Count_B}"
            os.system('cls')
            print(game_logo)
            print(f"Your Score is: {count}")
            print(A)
        else:
            correct = False
            os.system('cls')
            print(game_logo)
            print(f"Game Over!!! Your Final Score is: {count}")

    if input("Do you want to play again(Y/N)? ") == "Y":
        os.system('cls')
        higher_lower(Database)


higher_lower(data)
