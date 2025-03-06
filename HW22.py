#Name:Jax Byrge
#Class: 6th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class store:
    def __init__(self,stock,cost,weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double_price(self):
        self.cost *= 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
apple = store(10,2,1)
milk = store(5,5,4)
bannana = store(4,3,2)
#3. Print the stock of all three objects and the cost of the second store item.
print("The stock of apples is",apple.stock)
print("The stock of milk is",milk.stock)
print("The stock of bannana is",bannana.stock)

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
print("The old cost of milk is", milk.cost)
milk.double_price()
print("The new cost of milk is", milk.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
bannana.stock = (bannana.stock/4)
print("The new stock of bannana is",bannana.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del apple
try:
    print("The weight of apples is", apple.weight)
except:
    print("There is no apples")
