# This is a random password generator. Select the length of the password you
# would like, and we take guarantee of giving you a strong password
import random

print("Welcome to PyPassword!!")

# Taking inputs
alpha = input("How many Alphabets do you want to include in your password?\n")
num = input("How many Numbers do you want to include in your password?\n")
sym = input("How many Symbols do you want to include in your password?\n")
Pass_temp = []

# making list of alphabets, numbers and characters
alphabets = []
for i in range(ord('a'), ord('z')+1):
    alphabets.append(chr(i))
for i in range(0, 26):
    alphabets.append(chr(ord('A')+i))

print(alphabets)

symbols = []
for j in range(33, 127):
    if (33 <= j <= 47) or (58 <= j <= 64) or (91 <= j <= 96) or (123 <= j < 126):
        symbols.append(chr(j))

numbers = []
for k in range(0, 10):
    str(numbers.append(k))

# randomizing characters and numbers individually and concatenating to Password

for l in range(0, int(alpha)):
    Pass_temp.append(random.choice(alphabets))

for m in range(0, int(num)):
    Pass_temp.append(str(random.choice(numbers)))

for n in range(0, int(sym)):
    Pass_temp.append(random.choice(symbols))

random.shuffle(Pass_temp)
Password = ''.join(Pass_temp)

print(f"Your Password is:\n{Password}")
