# "Welcome to the Rock Paper Scissor game. Enjoy"

import random

your_choice = int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissors:\n"))

computers_choice = random.randint(0, 2)

rocks = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____ 
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rocks, paper, scissors]
print(f"Your Choice:\n{choices[your_choice]}\n")
print(f"Computer's Choice:\n{choices[computers_choice]}\n")

if your_choice == computers_choice:
    print("Its a Draw!!\n")
elif your_choice == (computers_choice+1)%3:
    print("Congrats!! You Win!!\n")
else:
    print("You Lost!!\n")
