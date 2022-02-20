"Welcome to the Rock Paper Scissor game. Enjoy"

your_choice = int(input("Enter 1 for Rock, 2 for Paper and 3 for Scissors:\n"))
import random
computers_choice = random.randint(1,3)

rocks = '''You Selected Rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''You Selected Paper!
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''You Selected Scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Computer's Choices
rocks_c = '''Computer Selected Rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_c = '''Computer Selected Paper!
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors_c = '''Computer Selected Scissors!
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if your_choice==1:
    print(rocks)
elif your_choice==2:
    print(paper)
elif your_choice==3:
    print(scissors)

if computers_choice==1:
    print(rocks_c)
elif computers_choice==2:
    print(paper_c)
elif computers_choice==3:
    print(scissors_c)

if your_choice == computers_choice:
    print("Congratulations!! You Win.")
else:
    print("Oops!! You Loose.")