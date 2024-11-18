#Name:Jax Byrge
#Class: 6th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
import random
import time
playerAmount = int(input("How many players do you want to rate: "))
type = ["Dress","Suit",]
color = ["Red","Yellow","Blue","White","Black","Orange","Green","Purple"]
style = ["Plain","Lepeord Print","Striped","Polka Dots","Fluffy","Silk"]
overall = []
for i in range(playerAmount):
    typeX = random.choice(type)
    colorX = random.choice(color)
    styleX = random.choice(style)
    print("Contestant Number",i+1,"Is Wearing A", colorX, styleX, typeX)
    j = int(input("What do you rate this 1-5: "))
    if j >= 5:
        j = 5
    if j <= 1:
        j = 1
    overall.insert(i,j)
x = sum(overall)
x /= playerAmount
print("Your Average Rating Was: ", x)
