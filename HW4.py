#Name: Jax
#Hour:6th
#Assignment: HW4

#Objectives:

#1. Print Hello World!
print("Hello world!")

#2. Create a dictionary with 3 keys and a value for each key.
#One of the keys must have a value with a list containing
#three numbers inside.
jax = {
    "Name" : "Jax",
    "Sport" : "Wrestling",
    "Age" : [2010,3,8]
}

#3. Print one of the three numbers by itself
print(jax["Age"][1])

#4. Using the update function, add a fourth key to the dictionary
#and give it a value.
jax.update({"Favorite Food": "Chicken"})

#5. Print the entire dictionary
print(jax)

#6. Clear all of the data inside of the dictionary and print it.
jax.clear()
print(jax)

#7. Make a nested dictionary with three entries containing the name
#of another classmate and two other pieces of information within each entry.
studentDict = {
    "Stuart" : {
    "Name" : "Stuart",
    "Sport" : "Baseball",
    "Favorite Food" : "Cake",
    },
    "Joe" : {
    "Name" : "Joe",
    "Sport" : "Basketball",
    "Favorite Food" : "Steak",
    },
    "Bob": {
    "Name": "Bob",
    "Sport": "Baseball",
    "Favorite Food": "Pasta",
    }
}
#8. Print the names of all three classmates on the same line.
print(studentDict)