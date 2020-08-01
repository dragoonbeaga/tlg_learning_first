#!/usr/bin/env python3
import random

insult = open("\Users\peter\OneDrive\Desktop\New folder\insult.txt", "r")

num= str(input("How many Shakespearean insults would you like?"))

def insult_generator(num):
    print("You are a", end="")
    for x in num:
      print(random.choice(num))

insult_generator(num)
