import random
from operator import truediv

#types are earth, fire, water, wind, lightning
#cards dict
cardsDict = {
    "Cactus" : {
        "type" : "earth",
        "damage" : "1",
        "health" : "4",
        "cost" : "2",
        "name" : "Cactus",
    },
    "Dragon" : {
        "type" : "fire",
        "damage" : "6",
        "health" : "6",
        "cost" : "6",
        "name" : "Dragon",
    },
    "Earth Golem" : {
        "type" : "earth",
        "damage" : "4",
        "health" : "8",
        "cost" : "6",
        "name" : "Earth Golem",
    },
    "Snowman" : {
        "type" : "water",
        "damage" : "1",
        "health" : "2",
        "cost" : "1",
        "name" : "Snowman",
    },
    "Thunder Bird" : {
        "type" : "lightning",
        "damage" : "6",
        "health" : "4",
        "cost" : "5",
        "name" : "Thunder Bird",
    },
    "Living Tree" : {
        "type" : "earth",
        "damage" : "3",
        "health" : "8",
        "cost" : "7",
        "name" : "Living Tree",
    },
    "Fire Spirit" : {
        "type" : "fire",
        "damage" : "4",
        "health" : "1",
        "cost" : "2",
        "name" : "Fire Spirit",
    },
    "Mermaid" : {
        "type" : "water",
        "damage" : "2",
        "health" : "3",
        "cost" : "3",
        "name" : "Mermaid",
    },
    "Happy Cloud" : {
        "type" : "wind",
        "damage" : "1",
        "health" : "2",
        "cost" : "1",
        "name" : "Happy Cloud",
    },
    "Angry Cloud" : {
        "type" : "lightning",
        "damage" : "3",
        "health" : "2",
        "cost" : "3",
        "name" : "Angry Cloud",
    },
    "Wind Knight" : {
        "type" : "wind",
        "damage" : "4",
        "health" : "6",
        "cost" : "4",
        "name" : "Wind Knight",
    },
}

#Start of Combat
playerCards = []
enemyCards = []
cardList = ["Cactus","Dragon","Earth Golem", "Snowman","Thunder Bird","Living Tree","Fire Spirit","Mermaid","Happy Cloud","Angry Cloud","Wind Knight"]
tempNum = 0
for i in range(3):
    cardRandom = random.choice(cardList)
    tempNum += 1
    playerCards.insert(tempNum, cardRandom)
tempNum = 0
for x in range(3):
    cardRandom = random.choice(cardList)
    tempNum += 1
    enemyCards.insert(tempNum, cardRandom)
playerHealth = 20
enemyHealth = 20
activePlayer = 0
activeEnemy = 0
#Combat Loop
while True:
    w = input("1")
    print("[You:",playerHealth,"] [Enemy:",enemyHealth,"]")
    print("Your Cards: [", cardsDict[playerCards[0]]["name"],"] [", cardsDict[playerCards[1]]["name"],"] [", cardsDict[playerCards[2]]["name"],"]")
    if activePlayer == 0:
        print("Active Player: [",activePlayer,"]")
    else: print("Active Player: [",activePlayer["name"],"]")
    if activeEnemy == 0:
        print("Active Enemy: [", activeEnemy, "]")
    else: print("Active Enemy: [",activeEnemy["name"], "]")
    print("")
    if activePlayer == 0:
        playerPlayingCard = int(input("Which Number Card do You Want to Play (1, 2, or 3) "))
        activePlayer = cardsDict[playerCards[(playerPlayingCard - 1)]]
        print("")
        print("You play a ",cardsDict[playerCards[(playerPlayingCard - 1)]]["name"])
        cardRandom = random.choice(cardList)
        playerCards[(playerPlayingCard - 1)] = cardRandom
        print("You Drew a ", cardRandom)
        print("")
    if activeEnemy == 0:
        enemyPlayingCard = int(input("Which Number Card do You Want to Play (1, 2, or 3) "))
        activePlayer = cardsDict[playerCards[(playerPlayingCard - 1)]]
        print("")
        print("You play a ", cardsDict[playerCards[(playerPlayingCard - 1)]]["name"])
        cardRandom = random.choice(cardList)
        playerCards[(enemyPlayingCard - 1)] = cardRandom
        print("Enemy Drew a ", cardRandom)
        print("")
    w = input("w")