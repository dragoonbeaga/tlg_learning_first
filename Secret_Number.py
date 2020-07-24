#This is a guess the number game
import random
import sys

GuessTheNumber = "Welcome to guess the number!!!!!"
print(GuessTheNumber.upper())

print('Hello! What is your name?')
name = str(input("Enter your name: "))

def guessNumber():
    secretnumber=random.randint(1, 100)
    count=1
    guess = int(input(str(name) + ", guess any number between 1 and 100: "))

    while guess !=secretnumber:
        count+=1
        if guess < secretnumber:
            print(str(name) + ", Your guess is too low try again")
        elif guess > secretnumber:
            print(str(name) + ", Your guess is to high try again")

        guess= int(input())

    if guess == secretnumber:
            print("You are the best " + str(name) + "! you got it in", count, "tries")
            return

guessNumber()

again = str(input("Do you want to play again (type yes or no): "))
if again == "yes":
    guessNumber()
else:
    print("Goodbye! " + str(name))
    sys.exit(0)
