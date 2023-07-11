import random

logo = ''' 
 _____                                       _____                          _  _   ___  
/  __ \                                     |  __ \                        (_)| | |__ \ 
| /  \/  __ _  _ __    _   _   ___   _   _  | |  \/ _   _   ___  ___  ___   _ | |_   ) |
| |     / _` || '_ \  | | | | / _ \ | | | | | | __ | | | | / _ \/ __|/ __| | || __| / / 
| \__/\| (_| || | | | | |_| || (_) || |_| | | |_\ \| |_| ||  __/\__ \\__ \ | || |_ |_|  
 \____/ \__,_||_| |_|  \__, | \___/  \__,_|  \____/ \__,_| \___||___/|___/ |_| \__|(_)  
                        __/ |                                                           
                       |___/                                                           '''

answer = random.randint(1, 100)


def guessing_game():
    print(logo)
    mode = input("Type 'E' for easy mode and 'H' for hard mode: ").lower()

    for count in range(1, 11):
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > answer:
            print("Try a smaller number maybe...")
        elif guess < answer:
            print("No no...go higher!!")
        else:
            break
        if mode == "h":
            print(f"You have {5 - count} Guesses left!!")
            if count == 5:
                break
        elif mode == "e":
            print(f"You have {10 - count} Guesses left!!")

    if guess == answer:
        print("Yaaaaay!! You guessed it correctly")
    else:
        print(f"Oops :( The answer is {answer}")

    if input("Do you want to play again?(Y/N)\n").lower() == "y":
        guessing_game()


guessing_game()
