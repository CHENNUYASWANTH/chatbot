import random
from datetime import datetime


def greeting_bot():
    responses = [
        "Hi!I am a bot",
        "Hello handsome",
        "!Nice to see you",
        "i am very glad to interact with you",
        "Pleased to meet you"
    ]
    print(random.choice(responses))
    print("-----------------------------------------------------")


def cur_time():
    current_time = datetime.now().hour
    greeting = "Good Morning"
    if(current_time >= 22):
        greeting = "Good night It`s too late to work"
    elif(current_time >= 16):
        greeting = "Good Evening"
    elif(current_time >= 11):
        greeting = "Good Afternoon"
    return greeting

def welcome():
    greeting_bot()
    name=input("enter your good name please  ")
    print(f"{cur_time()} {name}")
    print("-----------------------------------------------------")


def evaluator():
    expression=input("Enter your expression: ")
    try:
        print("Result of the expression: ",eval(expression))
        print("-----------------------------------------------------")
    except :
        print("you haven't entered the correct expression")
        print("-----------------------------------------------------")


def randomnumber():
    try:
        n=int(input("enter a number in b/w 1 to 6 :"))
        if n in range(1,7):
            m=random.choice(range(1,7))
            if n==m:
                print("hey you won")
                print("-----------------------------------------------------")
            else:
                print("you select",n,"but the number is ",m,"\n_________sorry try again__________")
                print("-----------------------------------------------------")
        else:
            print(" you enter a number not in range")
            print("-----------------------------------------------------")
            randomnumber()
    except:
        print("you didn't entered a number")
        print("-----------------------------------------------------")
        randomnumber()

def task():
    print("these are the tasks that i can perform for you")
    print("1.evaluate an expression \n2.play a random number game")
    print("enter 3 to stop my interaction with you")
    print("-----------------------------------------------------")


def menu():
    cur_time()
    welcome()
    
    while 1:
        try:
            task()
            n = int(input('select your task >>> '))
            print("---------------------------------------------")
        # Check if input is in range
            if n==1:
                evaluator()
            elif n==2:
                randomnumber()
            elif n>=4:
                print("select only given ")
                print("-"*25)
            else:
                print(" it was a nice meet with you have a great day")
                return 0
                
        except:
            print ("That's not a number")
            print("-"*35)




