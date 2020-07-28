#This is a guess the number game
import random
import sys

GuessTheNumber = "Welcome to guess the number!!!!!"  #varible for next line
print(GuessTheNumber.upper())  #prints above statement

print('Hello! What is your name?')  #asks players name
name = str(input("Enter your name: "))  #player defines there name here

def guessNumber():   #defines the game
    secretnumber=random.randint(1, 100)      #tells python to pick a random number between 1-100
    count=1
    guess = int(input(f"{name}, guess any number between 1 and 100: ")) #ask the player to enter an interger

    while guess !=secretnumber:
        count+=1
        if guess < secretnumber:
            print(f"{name}, Your guess is too low try again")
        elif guess > secretnumber:
            print(f"{name}, Your guess is to high try again")
        #elif guess !=
         #   print(f"{name}, please enter a whole number")

        guess = int(input())
    else:
            print(f"You are the best {name}! You got it in {count}, tries")
            return

guessNumber()

again = str(input(f"Do you want to play again {name}? (type yes or no): "))
if again == "yes":
    guessNumber()
else:
    print("Goodbye! " + str(name))
    sys.exit(0)
