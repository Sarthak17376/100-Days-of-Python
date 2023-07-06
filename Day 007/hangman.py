#  _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/                       

#                     ___________.._______
# | .__________))______|
# | | / /      ||
# | |/ /       ||
# | | /        ||.-''.
# | |/         |/  _  \
# | |          ||  `/,|
# | |          (\\`_.'
# | |         .-`--'.
# | |        /Y . . Y\
# | |       // |   | \\
# | |      //  | . |  \\
# | |     ')   |   |   (`
# | |          ||'||
# | |          || ||
# | |          || ||
# | |          || ||
# | |         / | | \
# """"""""""|_`-' `-' |"""|
# |"|"""""""\ \       '"|"|
# | |        \ \        | |
# : :         \ \       : :  
# . .          `'       . .


# Welcome to the Python Coded version of thr classic Hangman Game. Enjoy!!!

import random

animals = ['hamster', 'rabbit', 'horse', 'coyote', 'otter', 'koala', 'walrus', 'chimpanzee']
birds = ['peacock', 'dove', 'sparrow', 'goose', 'stork', 'pigeon', 'turkey', 'hawk', 'flamingo']
fruits = ['pomegranate', 'avocado', 'dragonfruit', 'gooseberry', 'apricot', 'tamarind']
hallow0 = """
  +---+
  |   |
      |
      |
      |
      |
========="""
hallow1 = """
  +---+
  |   |
  O   |
      |
      |
      |
========="""
hallow2 = """
  +---+
  |   |
  O   |
  |   |
      |
      |
========="""
hallow3 = """
  +---+
  |   |
  O   |
 /|   |
      |
      |
========="""
hallow4 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''
hallow5 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
hallow6 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''

hanging_the_man = [hallow0, hallow1, hallow2, hallow3, hallow4, hallow5, hallow6]

# Mode Choice
mode = input("Which Mode do you want to play in?(Type 'A' for animals, 'B' for Birds and 'F' for Fruits:\n").lower()
word = ""
if mode == 'a':
    # word = random.choice(animals)
    word = "rabbit"
elif mode == 'b':
    word = random.choice(birds)
elif mode == 'f':
    word = random.choice(fruits)

print(hanging_the_man[6])
guessed_word = []
for i in range(len(word)):
    guessed_word.append("_")

print("".join(guessed_word))


def blank_fill(ans_word, my_guess, letter_guess):
    letter_list = [*ans_word]
    for index, ele in enumerate(letter_list):
        if ele == letter_guess:
            my_guess[index] = letter_list[index]
            letter_list[index] = "_"

    return my_guess


i = 0
hangman = ""
while hangman != hanging_the_man[6] and "".join(guessed_word) != word:
    letters = input("Enter the letter you want to Guess!!\n")
    if word.find(letters.lower()) == -1:
        i += 1
    else:
        guesses_word = blank_fill(word, guessed_word, letters)
    hangman = hanging_the_man[i]
    print(hangman)
    print("".join(guessed_word))

if "".join(guessed_word) == word:
    print("Congratulations!! You Won")
elif hangman == hanging_the_man[6]:
    print("Game Over!! You lost")
