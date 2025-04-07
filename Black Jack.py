import random
import time

#Draw the card
numberCards = []
suitCards = []
suits = ["hearts","spades","diamonds","clubs"]
def drawCard():
    global numberCards
    global suitCards
    cardDrawNumber = random.randint(1,13)
    cardDrawSuit = random.choice(suits)
    if cardDrawNumber == 1:
        print("You drew a Ace of",cardDrawSuit)
        yN = input("Do you want your Ace to be 1 or 10: ")
        if yN == "10":
            cardDrawNumber = 10
        elif yN == "1":
            cardDrawNumber = 1
        else:
            cardDrawNumber = 10
    elif cardDrawNumber < 11:
        print("You drew a",cardDrawNumber,"of",cardDrawSuit)
    elif cardDrawNumber == 11:
        print("You drew a Jack of",cardDrawSuit)
        cardDrawNumber = 10
    elif cardDrawNumber == 12:
        print("You drew a Queen of",cardDrawSuit)
        cardDrawNumber = 10
    elif cardDrawNumber == 13:
        print("You drew a King of",cardDrawSuit)
        cardDrawNumber = 10
    numberCards.append(cardDrawNumber)
    suitCards.append(cardDrawSuit)

#hit or stand
def hitOrStand():
    global numberCards
    try:
        sumCards = sum(numberCards)
        print("Your total is ",sumCards)
        hitStand = input("H for hit S for stand: ")
    except:
        print("Not valid option try again")
        hitOrStand()
    if hitStand == "H":
        hit()
    elif hitStand == "S":
        print("stand")
        stand()
#hit
def hit():
    global numberCards
    drawCard()
    if sum(numberCards) > 21:
        print("Bust!")
        start()
    else:
        hitOrStand()
#stand
def stand():
    time.sleep(0.5)
    global numberCards
    dealerTotal = 0
    for i in range(random.randint(1,2)):
        dealerTotal += random.randint(1,10)
        if dealerTotal < 11:
            dealerTotal += random.randint(1, 10)
    if dealerTotal > 21:
        print("Dealer busted you win it had, ",dealerTotal)
        start()
    elif dealerTotal > sum(numberCards):
        print("The dealer stands with, ",dealerTotal)
        print("You lose")
        start()
    elif dealerTotal < sum(numberCards):
        print("The dealer stands with, ",dealerTotal)
        print("You win")
        start()

#start
def start():
    time.sleep(3)
    print("")
    global numberCards
    global suitCards
    numberCards = []
    suitCards = []
    drawCard()
    drawCard()
    hitOrStand()

start()