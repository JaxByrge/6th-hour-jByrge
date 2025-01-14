#Name:Jax Byrge
#Class: 6th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"
def helloWorld():
    print("Hello World")
#2. Create a def function that calculates the average of three numbers.
def average():
    x1 = int(input("Number 1:"))
    x2 = int(input("Number 2:"))
    x3 = int(input("Number 3:"))
    total = x1 + x2 + x3
    total = total // 3
    print(total)
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal(*a):
    print(a[2])
#4. Create a def function that loops from 1 to the number put in the argument.
def loop(*loopNum):
    y = 1
    for i in range(loopNum[0]):
        print(y)
        y+=1
#5. Call all of the functions created in 1 - 4 with relevant arguments.
helloWorld()
average()
animal("Cheeta","Leopard","Lion","Orangutan","Ape")
loop(int(input("How many loops do you want ")))