# Welcome to the CAESAR CIPHER. Encode or Decode your secret message here

#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
#             88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
#               88                                             


alphabets = []
for i in range(26):
    alphabets.append(chr(ord("a") + i))


def encrypt(to_hide, shift_no, alphabet_list):
    encoded_text = ""
    for j in range(len(to_hide)):
        new_index = (ord(to_hide[j]) - ord("a") + shift_no) % 26
        encoded_text += alphabet_list[new_index]
    print(f"Your Encoded message is : {encoded_text}")


def decrypt(to_show, shift_no, alphabet_list):
    decoded_text = ""
    for k in range(len(to_show)):
        new_index = (ord(to_show[k]) - ord("a") - shift_no + 26) % 26
        decoded_text += alphabet_list[new_index]
    print(f"Your Decoded message is : {decoded_text}")


while True:
    direction = input("Type 'encode' to Encrypt and 'decode' to Decrypt: ")
    text = input("Type your Message here: ").lower()
    shift = int(input("How much shift do you want?\n"))
    text_list = [*text]

    if direction == "encode":
        encrypt(text, shift, alphabets)
    elif direction == "decode":
        decrypt(text, shift, alphabets)
    else:
        print("Invalid Direction!!")

    again = input("Do you want to go Again?(Y/N)\n").lower()
    if again == "n":
        break
