#Name: Jax Byrge
#Class: 6th
#Assignment: Playground
#Code from: https://www.geeksforgeeks.org/how-to-get-weighted-random-choice-in-python/
#Code from: https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/#:~:text=The%20exit()%20function%20in,immediately%20stop%20running%20and%20exit.
#Code from: https://discovery.cs.illinois.edu/learn/Simulation-and-Distributions/For-Loops-in-Python/#:~:text=The%20line%20of%20code%20with,appears%20after%20the%20in%20statement.

import random
from logging.config import stopListening

#Entering All the first inputs
balance = 50
print("Your Balance Is [", balance,"]")
for i in range(10):
    gambleAmount = int(input("How much of your balance would you like to gamble, "))
    if gambleAmount > balance: print("You gamble amount exceeds your balance"), exit(1)
    if gambleAmount < 0: print("You gamble amount is below zero"), exit(1)

#Creating The Number Gamble Amount is Being Multiplied by  \
    multipliers = [0.5, 1.5, 2, 5, 10, 100]
    weights = random.choices(multipliers, weights=(50, 40, 30, 20, 10, 5), k=6)
    finalMultiplier = weights[0]

#Gambling Math
    balance -= gambleAmount
    winnings = gambleAmount * finalMultiplier
    balance += winnings

#Final Winnings
    if finalMultiplier == 10: print("MINI JACKPOT!")
    if finalMultiplier == 100: print("JACKPOT!!!!!!!")
    print("You have won (", winnings,")")
    print("Your balance is now [", balance,"]")
    print("")
    print("")
print("You ended up with [", balance,"]")

