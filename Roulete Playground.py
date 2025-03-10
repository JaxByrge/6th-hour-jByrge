import random
numberX = 0
color = "Green"
def spin():
    numberX = random.randint(0,32)
    if numberX == 0:
        color = "Green"
    elif numberX%2 == 0:
        color = "Black"
    else:
        color = "Red"
    print(numberX)
    print(color)

def number():
    numberChoice = int(input("Choose a number from 1 to 32"))
    spin()
    if numberX ==

def betChoice():
    choice = int(input("Number Bet(1) Color Bet(2)"))
spin()