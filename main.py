import art
import random
import data
print(art.logo)
def cho1():
    des =data.data[choice1]["description"]
    name = data.data[choice1]["name"]
    city = data.data[choice1]["country"]
    print(f"Compare A: {name}, a {des}, from {city}.")
def cho2():
    des = data.data[choice2]["description"]
    name = data.data[choice2]["name"]
    city = data.data[choice2]["country"]
    print(f"Compare B: {name}, a {des}, from {city}.")
def checkA():
    global points
    global  repe
    fol1 = data.data[choice1]["follower_count"]
    fol2 = data.data[choice2]["follower_count"]
    if fol1 > fol2:
        points+=1
        print(f"You're Right! Current score is: {points}.")
    else:
        repe = False
def checkB():
    global  repe
    global  points
    fol1 = data.data[choice1]["follower_count"]
    fol2 = data.data[choice2]["follower_count"]
    if fol2 > fol1:
        points+=1
        print(f"You're Right! Current score is: {points}.")
    else:
        repe = False
points = 0
repe = True
while repe:
    choice1 = random.randint(0,49)
    choice2 = random.randint(0, 49)
    cho1()
    print(art.vs)
    cho2()
    user_choice=input("Who Has More Followers? Type 'A' or 'B' :")
    if user_choice =="A" or user_choice =="a":
        checkA()
    elif user_choice=="B" or user_choice =="b":
        checkB()
    else:
        print("Enter the correct options!")
        repe = False
print(f"Sorry, that's wrong. Final score is: {points}")