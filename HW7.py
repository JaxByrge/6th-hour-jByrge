#Name:Jax
#Class: 6th Hour
#Assignment: HW7
from operator import truediv
import random
print(random.randint(1, 6))
#1. Print Hello World!
print("Hello world")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = True
admin = True

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
adminInt = 5

#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".

if wifi == True:
    if login == True:
        if admin == True:
            adminInt += 1
            print("Welcome, Amount of admins are", adminInt)
if wifi == False:
    print("Wifi is missing")
if login == False:
    print("Login is missing")
if admin == False:
    print("Admin is missing")


    print(random.randint(1, 6))
