#Name:Jax Byrge
#Class: 6th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def helloworld():
    print("Hello world")
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["blue","red","black","purple","white"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def bean():
    x = random.choice(beanBag)
    print(x)
    beanBag.remove(x)
    beanAgain()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def beanAgain():
    y = input("Would you like to pull another bean: ")
    if y == "Yes":
        bean()
    else:
        exit(0)
#5. Call the #3 function at the bottom.
bean()
