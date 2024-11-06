#Name: Jax Byrge
#Class: 6th Hour
#Assignment: HW12
import random
import time
from time import sleep

#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.
x = 5
for i in range(5):
    print(x)
    x -=1
print("Hello World")
#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
for i in range(31):
    if i % 2 == 0:
        print(i)

#3. Create a for loop that prints 5 different animals from a list.
animals = ["Dog","Cat","Lizard","Bird","Monkey"]
for i in animals:
    print(i)

#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
x = input("input:")
rev = x[::-1]
for i in rev:
    print(i)
