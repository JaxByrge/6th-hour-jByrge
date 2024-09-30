#Name: Jax Byrge
#Class: 6th Hour
#Assignment: HW6
#Code from:https://www.toppr.com/guides/python-guide/examples/python-examples/functions/number-divisible/python-program-find-numbers-divisible-another-number/#:~:text=In%20Python%2C%20the%20remainder%20operator,then%20it%20will%20be%20divisible.

#Objectives

#1. Print Hello World!
print("Hello World")

#2. Create a variable named num and assign it a variable.
num = int(input("Enter a number "))
#3. Create a nested if statement follows this structure:

#If num is divisible by 2
#   if num is divisible by 3
#       print the result of num being divided by 2
#       print the result of num being divided by 3
#   else
#       print that it is not divisible by 3
#       print the result of num being divided by 2
#else
#   if num is divisible by 3
#       print that num is not divisible by 2
#       print the result of num being divided by 3
#   else
#       print that neither is divisible by 2 or 3
if num % 2 == 0:
    if num % 3 == 0:
        print("Num divided by 2 = ",num / 2)
        print("Num divided by 3 = ",num / 3)
    else:
        print("Num is not divisiable by 3")
        print("Num divided by 2 = ",num / 2)
else:
    if num % 3 == 0:
        print("Num is not divisiable by 2")
        print("Num divided by 3 = ", num / 3)
    else:
        print("Num isn't divisible by 3 or 2")