import random
def numberGame():
    secret_number = random.randint(1,10)
    print("Secret number was: " + str(secret_number))
    guess=0
    while guess != secret_number:
        guess = int(input("Please guess secret number: "))
        if guess > secret_number:
            print("Secret is lower than you guess, try again. ",end='')
        elif guess < secret_number:
            print("Secret is greater than you guess, try again. ",end='')
        else:
            print("Great!")
            break
    print("Secret number was: "+ str(secret_number))

numberGame()