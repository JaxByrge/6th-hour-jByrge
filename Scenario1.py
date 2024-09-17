#Name: Jax
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead
#has asked you to create a nested dictionary containing five enemy
#creatures (and their properties) for combat testing. Additionally,
#the testers are asking for a way to input changes to the enemy's
#damage values for balancing, as well as having it print those changes to
#confirm they went through.

#It is up to you to decide what properties
#are important and the theme of the game.

enemyDict = {
    "Bogo" : {
        "damage" : 10,
        "health" : 50,
        "speed" : 3,
        "size" : 20,
    },
    "Glorb": {
        "damage": 2,
        "health": 10,
        "speed": 10,
        "size": 3,
    },
    "Zorgo": {
        "damage": 4,
        "health": 25,
        "speed": 6,
        "size": 10,
    },
    "Thrag": {
        "damage": 8,
        "health": 35,
        "speed": 6,
        "size": 12,
    },
    "Drackor": {
        "damage": 15,
        "health": 100,
        "speed": 7,
        "size": 25,
    }
}
print(enemyDict)
animal = input("What animal do you want to change ")
if animal != ("Bogo" or "Glorb" or "Zorgo" or "Thrag" or "Drackor") :
    print("Not Valid Animal")
    exit(0)
value = input("what attribute do you want to change ")
if value != ("damage" or "health" or "speed" or "size") :
    print("Not Valid Value")
    exit(0)
enemyDict[animal][value] = int(input("What do you want to change it to "))
print(enemyDict)






