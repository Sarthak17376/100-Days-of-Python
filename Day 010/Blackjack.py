import random

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


def hand_generator(deck_of_cards, hand, A_large, A_small):
    temp_card = random.choice(deck_of_cards)
    hand.append(temp_card)
    deck_of_cards.remove(temp_card)
    temp_card = random.choice(deck_of_cards)
    hand.append(temp_card)
    deck_of_cards.remove(temp_card)
    value = sum(hand)
    print(value)
    if A_large in hand:
        while value > 21:
            hand.remove(A_large)
            hand.append(A_small)
            value -= 10

    return value


A = 11
A1 = 1
K = Q = J = 10


def game():
    print(logo)
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, A, K, Q, J, 2, 3, 4, 5, 6, 7, 8, 9, 10, A, K, Q, J, 2, 3, 4, 5, 6,
            7, 8, 9, 10, A, K, Q, J, 2, 3, 4, 5, 6, 7, 8, 9, 10, A, K, Q, J]
    my_hand = []
    computers_hand = []
    computers_score = hand_generator(deck, computers_hand, A, A1)
    my_score = hand_generator(deck, my_hand, A, A1)

    print(f"Your Hand: {my_hand}, Current Score: {my_score}")
    print(f"Computer's First Card is: {computers_hand[0]}")

    while my_score <= 21 and input("Do you want to draw a card?(y/n): ").lower() == "y":
        temp_num = random.choice(deck)
        my_hand.append(temp_num)
        deck.remove(temp_num)
        my_score += temp_num
        if A in my_hand and my_score > 21:
            my_hand.remove(A)
            my_hand.append(A1)
            my_score -= 10
        print(f"Your Hand: {my_hand}, Current Score: {my_score}")
        print(f"Computer's First Card is: {computers_hand[0]}")

    print(f"Your Hand: {my_hand}, Current Score: {my_score}")
    print(f"Computer's Hand is: {computers_hand}")

    while computers_score < 17:
        temp_num = random.choice(deck)
        computers_hand.append(temp_num)
        deck.remove(temp_num)
        computers_score += temp_num
        if A in computers_hand and computers_score > 21:
            computers_hand.remove(A)
            computers_hand.append(A1)
            computers_score -= 10
        print(f"Your Hand: {my_hand}, Current Score: {my_score}")
        print(f"Computer's Hand is: {computers_hand}")  # check for showing computer hand for total < 17

    print(f"Your Final Hand is: {my_hand}, Final Score: {my_score}")
    print(f"Computer's Final Hand is: {computers_hand}, Final Score: {computers_score}")

    if my_score > 21:
        print("You Lost!! Better Luck next time")
    elif computers_score > 21:
        print("Congrats!! You Won")
    elif my_score > computers_score:
        print("Congrats!! You Won")
    elif my_score < computers_score:
        print("You Lost!! Better Luck next time")
    elif my_score == computers_score:
        print("OMG!! Its a draw")


while input("Do you want to play(Y/N)".lower()) == 'y':
    game()
