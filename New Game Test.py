import random
from time import sleep

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
#Random Pos
maxX = 4
maxY = 4
playerX = 2
playerY = 2
#Loop
    #Printing out Player Position
while True:
    playerX = str(playerX)
    playerY = str(playerY)
    playerPos = ("slot" + playerY + playerX)
    slots[playerPos] = "[O]"
    print(slots["slot00"],slots["slot01"],slots["slot02"],slots["slot03"],slots["slot04"])
    print(slots["slot10"],slots["slot11"],slots["slot12"],slots["slot13"],slots["slot14"])
    print(slots["slot20"],slots["slot21"],slots["slot22"],slots["slot23"],slots["slot24"])
    print(slots["slot30"],slots["slot31"],slots["slot32"],slots["slot33"],slots["slot34"])
    print(slots["slot40"],slots["slot41"],slots["slot42"],slots["slot43"],slots["slot44"])
    playerX = int(playerX)
    playerY = int(playerY)
    #Place barrier
    xY = ("slot" + (input("Input X and Y: ")))
    if slots[xY] == "[ ]":
        slots[xY] = "[X]"
    #Movement of O
    x = 1
    movements = ["Down", "Up", "Right", "Left"]
  #  while x == 1:
  #      moveChoice = random.choice(movements)
  #      if moveChoice == "Down":
  #          playerY += 1
  #          playerX = str
  #          playerY = str
  #          if slots[("slot" + playerY + playerX)] != "[ ]":
  #              playerY = int
  #              playerX = int
  #              playerY -= 1
  #          else: x = 0
  #      if moveChoice == "Up":
  #          playerY -= 1
  #          playerX = str
  #          playerY = str
  #          if slots[("slot" + playerY + playerX)] != "[ ]":
  #              playerY = int
  #              playerX = int
  #              playerY += 1
  #          else: x = 0
  #      if moveChoice == "Left":
  #          playerX -= 1
  #          playerX = str
  #          playerY = str
  #          if slots[("slot" + playerY + playerX)] != "[ ]":
  #              playerY = int
  #              playerX = int
  #              playerX += 1
  #          else: x = 0
  #      if moveChoice == "Right":
  #          playerX += 1
  #          playerX = str
  #          playerY = str
  #          if slots[("slot" + playerY + playerX)] != "[ ]":
  #              playerY = int
  #              playerX = int
  #              playerX -= 1
  #          else: x = 0

    #Borders
    if playerX > maxX:
        print("You Lost")
        exit(0)
    if playerX < 0:
        print("You Lost")
        exit(0)
    if playerY > maxY:
        print("You Lost")
        exit(0)
    if playerY < 0:
        print("You Lost")
        exit(0)
    slots[playerPos] = "[ ]"
   # print(moveChoice)