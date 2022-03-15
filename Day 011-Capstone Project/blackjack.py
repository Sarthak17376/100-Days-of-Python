logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

        
def hand_generator(hand):
    temp_card = random.choice(deck)
    hand.append(temp_card)
    deck.remove(temp_card)
    temp_card = random.choice(deck)
    hand.append(temp_card)
    deck.remove(temp_card)

def list_counter(lst,x):
    count=0
    for ele in lst:
        if ele==x:
            count+=1
    return count

def sum_cards(any_list):
    sum=0
    if "A" in any_list:
        count_A = list_counter(any_list,"A")
        sum += (11*count_A)
    if "K" in any_list:
        count_K = list_counter(any_list,"K")
        sum += (10*count_K)
    if "Q" in any_list:
        count_Q = list_counter(any_list,"Q")
        sum += (10*count_Q)
    if "J" in any_list:
        count_J = list_counter(any_list,"J")
        sum += (10*count_J)
    if "A" in any_list:
        while sum>21:
            sum-=10
    
    for i in range(0,len(any_list)):
        if type(any_list[i])==int:
            sum+=any_list[i]
    return sum
    
A = 11
K = 10
Q = 10
J = 10
print(logo) 
deck = [2,3,4,5,6,7,8,9,10,"A","K","Q","J",2,3,4,5,6,7,8,9,10,"A","K","Q","J",2,3,4,5,6,7,8,9,10,"A","K","Q","J",2,3,4,5,6,7,8,9,10,"A","K","Q","J"]
my_hand = []
computers_hand = []
my_score = 0
computers_score = 0
import random
random.shuffle(deck)

hand_generator(my_hand)
hand_generator(computers_hand)

my_score = sum_cards(my_hand)
computers_score = sum_cards(computers_hand)

print(f"Your Hand: {my_hand}, Current Score: {my_score}")
print(f"Computer's First Card is: {computers_hand[0]}")

flag = 0
while computers_score<=21 or my_score<=21:
    if my_score<=21 and input("Do you want to draw a card?(y/n): ")=="y":
        temp_num=random.choice(deck)
        my_hand.append(temp_num)
        deck.remove(temp_num)
        my_score = sum_cards(my_hand)
        print(f"Your Hand: {my_hand}, Current Score: {my_score}")
        print(f"Computer's First Card is: {computers_hand[0]}")
    else:
        while computers_score<=21:
            if computers_score<17:
                temp_num=random.choice(deck)
                computers_hand.append(temp_num)
                deck.remove(temp_num)
                computers_score = sum_cards(computers_hand)
            else:
                if my_score>computers_score:
                    flag=1
                break;
        if computers_score>21:
            flag=1
        break

print(f"Your Final Hand is: {my_hand}, Final Score: {my_score}")
print(f"Computer's Final Hand is: {computers_hand}, Final Score: {computers_score}")
if my_score<21:
    if flag==1:
        print("You Win!!!!")
    else:
        print("You Lost!!!!")
elif my_score==computers_score:
    print("OMG! A Draw!!!")
else:
    print("You Lost!!!!")
        