#!/usr/bin/env python
"""Author: James Peterson || This program to run a quiz"""
class Question:                         #this is a Class. allows me to point to questions inside of list
    def __init__(self, prompt, answer): #this initiates the class.  (sets what the Class can be called,
        self.prompt = prompt            #defines this variable       #prompt refers to first ?variable? in a list(0),
        self.answer = answer            #    "                       #answer refers to second ?variable? in a list(2))

def run_quiz_Harry_Potter(questions):                #runs the quiz that is turned on.
    global correct
    correct = 0
    for question in questions:
        answer = input(f"{question.prompt}\n:")
        if answer == question.answer:
            correct += 25
    score_Harry_Potter()

def run_quiz_FMA(questions):                #runs the quiz that is turned on.
    global correct
    correct = 0
    for question in questions:
        answer = input(f"{question.prompt}\n:")
        if answer == question.answer:
            correct += 25
    score_FMA()


def Quiz_Harry_Potter():
    question_prompts = [
    "\n1. Harry Potter's birthday is on?\n(a) April 1st\n(b) July 31st\n(c) February 29th\n(d)August 20th",

    "\n2. How does Harry manage to breathe underwater during the second task of the Triwizard Tournament?\n"
        "(a) He transfigures into a shark\n(b) He kisses a mermaid\n(c) He eats gillyweed\n(d)"
        "He performs a bubble-head charm",

    "\n3. What is the name of Fred and George’s joke shop?\n(a) Weasley Joke Emporium\n(b) Weasleys’ Wizard Wheezes\n"
        "(c) Fred & George’s Wonder Emporium\n(d) Zonko’s Joke Shop",

    "\n4. Which of these is NOT one of the Unforgivable Curses?\n(a) Cruciatus Curse\n(b) Imperius Curse\n(c)"
        "Sectumsempra\n(d) Avada Kedavra"]

    global questions
    questions = [Question(question_prompts[0],"b"),Question(question_prompts[1],"c"),
                 Question(question_prompts[2],"b"),Question(question_prompts[3],"c")]

def Quiz_FullMetal_Alchemist_Brotherhood():
    question_prompts = [
    "\n1. Who is the main character(s)\n(a) Edward and Alphonse Elric\n(b) Roy Mustang\n(c) Izumi Curtis\n(d)Riza Hawkeye",

    "\n2. Who died in the last episodes of part 1?\n(a) Maes Hughes\n(b) Roy Mustang\n(c) Alphonse Elric\n"
        "(d) Winry Rockbell",

    "\n3. What is Roy Mustang's special 'power'?\n(a) Water\n(b) Fire\n(c)Ice\n(d)Sand",

    "\n4. Who is the snobby guy who used up all of the Elric's money?\n(a) Lin Yao\n(b) Fu\n(c)"
        " May Chang\n(d) Father"]

    global questions
    questions = [Question(question_prompts[0], "a"), Question(question_prompts[1], "a"),
                 Question(question_prompts[2], "b"), Question(question_prompts[3], "a")]

def quiz_list():
    global quizlist
    quizlist = ["Harry Potter", "FullMetal Alchemist: Brotherhood"]

def quiz_choice():
    selection = str(input(f"1. {quizlist[0]}?\n2. {quizlist[1]}\nPlease enter the number of the quiz: "))
    if selection == "1":
        Quiz_Harry_Potter()
        run_quiz_Harry_Potter(questions)
    else:
        Quiz_FullMetal_Alchemist_Brotherhood()
        run_quiz_FMA(questions)

def your_name():
    print("Before we begin,")

    global name
    name = str(input("What is your name?: "))

    you_sure()

def you_sure():
    sure = str(input(f"{name} is it? (y or n): "))
    if sure.lower() == "y":
        print(f"Okay then {name}, Please pick one of the following topics: ")
        quiz_list()
        quiz_choice()
    else:
        your_name()

def score_Harry_Potter():
    score = correct
    if(score == 25 or score== 0):
        print(f"OUCH! {score}% YOU SUCK {name} would you like to try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_Harry_Potter(questions)
        else:
            quitter_Harry_Potter()
    elif score == 50:
        print(f"{score}%! So close to passing {name}, would you like to try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_Harry_Potter(questions)
        else:
            quitter_Harry_Potter()
    elif score == 75:
        print(f"{score}% WOOO! You passed {name}! But you can do better I know it! Try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_Harry_Potter(questions)
        else:
            quitter_Harry_Potter()
    else:
        print(f"{score}%! You really know Harry Potter! Would you like to try the FMA Quiz?")
        other = str(input("y or n: "))
        if other.lower() == "y":
            Quiz_FullMetal_Alchemist_Brotherhood()
            run_quiz_FMA(questions)
        else:
            print(f"Have a great day {name}! Please play again sometime.")


def score_FMA():
    score = correct
    if(score == 25 or score== 0):
        print(f"OUCH! {score}% YOU SUCK {name} would you like to try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_FMA(questions)
        else:
            quitter_FMA()
    elif score == 50:
        print(f"{score}%! So close to passing {name}, would you like to try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_FMA(questions)
        else:
            quitter_FMA()
    elif score == 75:
        print(f"{score}% WOOO! You passed {name}! But you can do better I know it! Try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_FMA(questions)
        else:
            quitter_FMA()
    else:
        print(f"{score}%! Big Fan of FMA I see! Would you like to try Harry Potter quiz")
        other = str(input("y or n: "))
        if other.lower() == "y":
            Quiz_Harry_Potter()
            run_quiz_Harry_Potter(questions)
        else:
            print(f"Have a great day {name}! Please play again sometime.")

def quitter_Harry_Potter():
    print(f"{name}, I can't believe you are quiting!")
    print(f"Goodbye and Good riddance {name}!\nUnless you would like to try the other quiz?")
    other = str(input("y or n: "))
    if other.lower() == "y":
        Quiz_FullMetal_Alchemist_Brotherhood()
        run_quiz_FMA(questions)
    else:
        print(f"Have a great day {name}! Please play again sometime.")

def quitter_FMA():
    print(f"{name}, I can't believe you are quiting!")
    print(f"Goodbye and Good riddance {name}!\nUnless! you would like to try the other quiz?")
    other = str(input("y or n: "))
    if other.lower() == "y":
        Quiz_Harry_Potter()
        run_quiz_Harry_Potter(questions)
    else:
        print(f"Have a great day {name}! Please play again sometime.")

intro = "Welcome to the Nerdom Quizzes!!!"
print(intro.upper())

your_name()
