#Name:Jax Byrge
#Class: 6th Hour
#Assignment: HW16

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
import random
from operator import truediv


def rpc():
    ai = random.randint(1,3)
    pl = int(input("1 for rock,2 for paper,3 for scissors: "))
    print(pl, ai)
    if pl == ai:
        print("draw")
    if pl == 1 and ai == 3:
        print("You win")
    if pl == 2 and ai == 1:
        print("You win")
    if pl == 3 and ai == 2:
        print("You win")
    if pl == 1 and ai == 2:
        print("You lose")
    if pl == 2 and ai == 3:
        print("You lose")
    if pl == 3 and ai == 1:
        print("You lose")

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
rpc()
while True:
    x = input("Would you like to play again: ")
    if x != "yes":
        exit(0)
    else: rpc()
