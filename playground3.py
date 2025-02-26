#Name: Jax Byrge
#Class: 6th
#Assignment: Playground
import random

#Gambling
moneyTotal = 10
moneySpend = 10
while True:
    print("Your total is",int(moneyTotal))
    moneySpend = int(input("How much do you want to spend: "))
    moneyTotal -= moneySpend
    for i in range(3):
        mult = random.randint(0,20)
        mult = mult * 0.1
        moneySpend = moneySpend * mult
    moneyTotal += moneySpend
    print("You won ",int(moneySpend))
    if moneyTotal < 1:
        print("You are out of money")
        exit(0)