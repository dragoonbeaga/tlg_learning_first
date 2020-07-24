#1. Interger and Float

import math
x = 5   #interger
pi = 3.14
radius = 8

print(float(pi * radius**2))

name = "James"
surname = "Peterson"

print(name + " " + surname)
print(name.lower() + " " + surname.upper())

question = input('Is basic training difficult? "y or n"')

if question == "y":
    print("no it wasnt!")
else:
    print("are you sure?")

budget = float(input('What is your budget?' "Between 1-1000"))


if budget > 1000:
    print("YOU ARE TOO RICH!")

elif budget > 550:
    print("You will eat well this month!")

elif budget == 550:
    print("This is the average American food budget")

elif budget <= 0:
    print("GET A JOB YOU BUM!")

else:
    print("this is less than the average American food budget")


x = 0
while x <= 100:
    print(x)
    x = x + 2
#stopping multiple counters
#for i in  range(2, 100):
    #if i%2 == 0
        #print(i)

import random

nums = []

for z in range(100):
    nums.append(random.randint(1,100))

print(nums)