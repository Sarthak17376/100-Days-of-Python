
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



alphabets = [" "]
for i in range(97,123):
    alphabets.append(chr(i))

direction = input("Type 'encode' to Encrypt and 'decode' to Decrypt: ")
text = input("Type your Message here: ").lower()
shift = int(input("How much shift do you want?\n"))
text_list = []
for i in range(len(text)):
    text_list.append(text[i])

def encrypt():
    encoded_text=""
    for j in text_list:
        text_index = alphabets.index(j)
        if(text_index>=1 and text_index<=26-shift):
            text_index+=shift
        elif(text_index>(26-shift) and text_index<=26):
            text_index=text_index+shift-26
        encoded_text+=alphabets[text_index]
    print(f"Your Encoded message is : {encoded_text}")

def decrypt():
    decoded_text=""
    for k in text_list:
        text_index = alphabets.index(k)
        if(text_index>=1+shift and text_index<=26):
            text_index-=shift
        elif(text_index>=1 and text_index<1+shift):
            text_index=text_index-shift+26
        decoded_text+=alphabets[text_index]
    print(f"Your Decoded message is : {decoded_text}")

if(direction=="encode"):
    encrypt()
elif(direction=="decode"):
    decrypt()
else:
    print("Invalid Direction!!")
