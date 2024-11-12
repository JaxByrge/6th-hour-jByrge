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
import random
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
yn = input("would you like to change an animal ")
if yn == "Yes":
    animal = input("What animal do you want to change ")
    value = input("what attribute do you want to change ")
    enemyDict[animal][value] = int(input("What do you want to change it to "))
    print(enemyDict)

#Variables For fighting
animalFight = input("What animal do you want to fight ")
playerHp = 25
playerDamage = 10
playerSpeed = 5
enemyHp = enemyDict[animalFight]["health"]
enemyDamage = enemyDict[animalFight]["damage"]
enemySpeed = enemyDict[animalFight]["speed"]
#for loop for fighting
for i in range(99):
    enemyAction = random.randint(1, 3)
    print("You [",playerHp,"]", animalFight, "[",enemyHp,"]")
    print("Actions:")
    print("[Attack]")
    print("[Heal]")
    print("[Block]")
    action = input(":")
    #Player Attacks
    if action == "Attack":
        if enemyAction < 3:
            enemyHp -= playerDamage
    #Player Heals
    if action == "Heal":
        playerHp += (playerDamage - 3)
    if playerHp > 25:
        playerHp = 25
    #Enemy attack and player Blocks
    if action != ("Block"):
        if enemyAction < 3:
            playerHp -= enemyDamage
    print("")
    if enemyAction == 3:
        print("Your enemy blocks")
    if enemyAction < 3:
        print("Your enemy Attacks")
    print("")
    print("You", action)
    print("")
    #Winning or losing
    if playerHp < 1:
        print("You have been defeated by a", animalFight, "You lose")
        exit(0)
    if enemyHp < 1:
        print("You have defeated a", animalFight, "You win")
        exit(0)




