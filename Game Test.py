import random
from time import sleep

slots = {
    "slot00": "O",
    "slot01": "O",
    "slot02": "O",
    "slot03": "O",
    "slot04": "O",
    "slot10": "O",
    "slot11": "O",
    "slot12": "O",
    "slot13": "O",
    "slot14": "O",
    "slot20": "O",
    "slot21": "O",
    "slot22": "O",
    "slot23": "O",
    "slot24": "O",
    "slot30": "O",
    "slot31": "O",
    "slot32": "O",
    "slot33": "O",
    "slot34": "O",
    "slot40": "O",
    "slot41": "O",
    "slot42": "O",
    "slot43": "O",
    "slot44": "O",
}
#Random Pos
maxX = 4
maxY = 4
playerX = 2
playerY = 2
#Loop
while True:
    #Printing out Player Position
    playerX = str(playerX)
    playerY = str(playerY)
    playerPos = ("slot" + playerY + playerX)
    slots = {
        "slot00": "[ ]",
        "slot01": "[ ]",
        "slot02": "[ ]",
        "slot03": "[ ]",
        "slot04": "[ ]",
        "slot10": "[ ]",
        "slot11": "[ ]",
        "slot12": "[ ]",
        "slot13": "[ ]",
        "slot14": "[ ]",
        "slot20": "[ ]",
        "slot21": "[ ]",
        "slot22": "[ ]",
        "slot23": "[ ]",
        "slot24": "[ ]",
        "slot30": "[ ]",
        "slot31": "[ ]",
        "slot32": "[ ]",
        "slot33": "[ ]",
        "slot34": "[ ]",
        "slot40": "[ ]",
        "slot41": "[ ]",
        "slot42": "[ ]",
        "slot43": "[ ]",
        "slot44": "[ ]",
    }
    print(moveChoice)
    slots[playerPos] = "[O]"
    print(slots["slot00"],slots["slot01"],slots["slot02"],slots["slot03"],slots["slot04"])
    print(slots["slot10"],slots["slot11"],slots["slot12"],slots["slot13"],slots["slot14"])
    print(slots["slot20"],slots["slot21"],slots["slot22"],slots["slot23"],slots["slot24"])
    print(slots["slot30"],slots["slot31"],slots["slot32"],slots["slot33"],slots["slot34"])
    print(slots["slot40"],slots["slot41"],slots["slot42"],slots["slot43"],slots["slot44"])
    playerX = int(playerX)
    playerY = int(playerY)
    #Movement Controls
    movements = ["Down","Up","Right","Left"]
    moveChoice = random.choice(movements)
    if moveChoice == "Down":
        playerY += 1
    if moveChoice == "Up":
        playerY -= 1
    if moveChoice == "Left":
        playerX -= 1
    if moveChoice == "Right":
        playerX += 1
    sleep(1)
    #Borders
    if playerX > maxX: playerX = maxX
    if playerX < 0: playerX = 0
    if playerY > maxY: playerY = maxY
    if playerY < 0: playerY = 0