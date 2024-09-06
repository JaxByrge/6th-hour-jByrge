#Name: Jax Byrge
#Class: 6th
#Assignment: Playground

#Variables
import random
enemyHealth = (3)
playerHealth = (3)
enemyDecision = (random.randint(1, 3,))
#1 is rock 2 is scissors 3 is paper

#for loop
for i in range(999):

#Rock paper scissors
    enemyDecision = (random.randint(1, 3,))
    playerOption = input("Rock, Paper, or Scissors ")
    print("You have chosen [",playerOption,"]")

    if enemyDecision == 1: print("Your enemy has chosen [Rock]")
    if enemyDecision == 2: print("Your enemy has chosen [Scissors]")
    if enemyDecision == 3: print("Your enemy has chosen [Paper]")
    print("")
#Loses
    if playerOption == "Scissors" and enemyDecision == 1:
        print("You lose")
        playerHealth -= 1
    if playerOption == "Rock" and enemyDecision == 3:
        print("You lose")
        playerHealth -= 1
    if playerOption == "Paper" and enemyDecision == 2:
        print("You lose")
        playerHealth -= 1
#Wins
    if playerOption == "Paper" and enemyDecision == 1:
        print("You won")
        enemyHealth -= 1
    if playerOption == "Scissors" and enemyDecision == 3:
        print("You won")
        enemyHealth -= 1
    if playerOption == "Rock" and enemyDecision == 2:
        print("You won")
        enemyHealth -= 1
#Draws
    if playerOption == "Paper" and enemyDecision == 3:
        print("Draw")
    if playerOption == "Scissors" and enemyDecision == 2:
        print("Draw")
    if playerOption == "Rock" and enemyDecision == 1:
        print("Draw")

#Print Healths
    print("")
    print("Enemy: ", enemyHealth)
    print("Player: ", playerHealth)
    print("")

#Total Win or Lose
    if enemyHealth < 1: print("You have won!"), exit(1)
    if playerHealth < 1: print("You have lost"), exit(1)

