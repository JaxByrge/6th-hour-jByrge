#Name:
#Class: 6th Hour
#Assignment: HW20


#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
x = 0
try:
    print(x)
except:
    print("Hello World!")

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.

y = int(input("Pick a number to be divided by 100: "))
try:
    print(y/100)
except:
    print("Divide by Zero Error")

#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.

z = input("Pick a number: ")
try:
    print(int(z))
except:
    print("Exception for value error")

#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
i = 5
while True:
    if i < 0:
        raise Exception("Bellow Zero")
    else:
        print(i)
        i -= i