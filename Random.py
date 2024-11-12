import random
gambleAmount= int(input("How much do you want to gamble? "))
x = random.randint(0,100)
winning = (gambleAmount * x)
print("You win ", winning)