#This is a random password generator. Select the length of the password you 
# would like and we take guarantee of giving you a strong password

print("Welcome to PyPassword!!")

#Taking inputs
alpha = input("How many Alphabets do you want to include in your password?\n")
num = input("How many Numbers do you want to include in your password?\n")
sym = input("How many Symbols do you want to include in your password?\n")
Pass_temp = ""

#making list of alphabets, numbers and charecters
alphabets = []
for i in range(65,123):
    if (i>=65 and i<=90) or (i>=97 and i<=122):
        alphabets.append(chr(i))

symbols = []
for j in range(33,127):
    if (j>=33 and j<=47) or (j>=58 and j<=64) or (j>=91 and j<=96) or (j>=123 and j<126):
        symbols.append(chr(j))

numbers = []
for k in range(0,10):
    str(numbers.append(k))

#randomizing charecters and numbers individually and concatinating to Password
import random

for l in range(0,int(alpha)):
    rand_alpha = random.choice(alphabets)
    Pass_temp+=rand_alpha

for m in range(0,int(num)):
    rand_num = str(random.choice(numbers))
    Pass_temp+=rand_num

for n in range(0,int(sym)):
    rand_sym = random.choice(symbols)
    Pass_temp+=rand_sym

#randomizing elements of Password
str_pass=[]
i=0
for i in range(0,len(Pass_temp)):
    str_pass.append(Pass_temp[i])

random.shuffle(str_pass)

Password=""
j=0
for j in range(0,len(Pass_temp)):
    Password+=str_pass[j]
    
print(f"Your Password is:\n{Password}")
