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
                            

#Welcome to the Python Coded version of thr classic Hangman Game. Enjoy!!!

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


import random

mode = input("Which Mode do you want to play in?(Type 'A' for animals, 'B' for Birds and 'F' for Fruits:\n")
if mode == 'A' or mode == 'a':
    word = random.choice(animals)
elif mode == 'B' or mode == 'b':
    word = random.choice(birds)
elif mode == 'F' or mode == 'f':
    word = random.choice(fruits)

print(hanging_the_man[6])
guessed_word = ""
for i in range(len(word)):
    guessed_word+="_"
print(guessed_word)

i = 0
hangman =""

def blank_fill():
    global guessed_word
    list_word = []
    for j in range(0,len(word)):
      list_word.append(word[j])
    blanks_list =[]
    for k in range(0,len(word)):
      blanks_list.append(guessed_word[k])

    for index,ele in enumerate(list_word):
      if ele == letters:
        blanks_list[index] = word[index]
    
    guessed_word = ""
    for l in range(0,len(word)):
      guessed_word+=blanks_list[l]

while (not hangman == hanging_the_man[6]) or not guessed_word==word:
    hangman = hanging_the_man[i]
    letters = input("Enter the letter you want to Guess!!\n")
    if word.find(letters.lower())==-1:
      i+=1
      print(hangman)
      print(guessed_word)
    else:
      blank_fill()
      print(hangman)
      print(guessed_word)
    if guessed_word == word:
      break

if hangman == hanging_the_man[6]:
  print("Game Over!! You lost")
elif guessed_word==word:
  print("Congratulations!! You Won")