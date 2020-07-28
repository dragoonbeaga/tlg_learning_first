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
    #guess = int(input(f"{name}, guess any number between 1 and 100: ")) #ask the player to enter an interger      #this line would return an error if not a whole number
                                                                                                                   #added in the while true statement below to solve it

    while True:
        try:
            guess = int(input(f"{name}, guess any number between 1 and 100: ")) #ask the player to enter an interger
            break
        except ValueError:
            print(f"{name}, That is not a whole number. Try again.")

    while guess !=secretnumber:     #while loop.  as long as number is not equal to the random number.
        count+=1                    #defines and makes it add one as the loop repeats
        if guess < secretnumber:    #if stament for less than
            print(f"{name}, Your guess is too low try again")
        elif guess > secretnumber:  #ifstatment for greater than
            print(f"{name}, Your guess is to high try again")
        #elif guess !=
         #   print(f"{name}, please enter a whole number")       BROKEN test

        guess = int(input())   #stops infite loop and asks for input again after testing above statement
    else:                     #if not less than or greater than. Thne user got the right number.
            print(f"You are the best {name}! You got it in {count}, tries")
            return

guessNumber()   #excutes the game.

again = str(input(f"Do you want to play again {name}? (type yes or no): "))    #asks if user wants to play again
if again == "yes":                 #input for above question. if yes. repeasts the game.   all other values eixts the script
    guessNumber()
else:
    print("Goodbye! " + str(name))
    sys.exit(0)
