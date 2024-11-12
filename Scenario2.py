#Name: Jax
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 2:
#The programmer in charge of the player character party stats is
#having some issues with their code. Despite rigorous testing,
#they are inexperienced and can't seem to figure out why it damage
#testing isn't working. Your team lead has asked you to help by fixing
#the party dictionary, insert an enemy into the code below, and
#testing to see if a player character can damage the with a printed
#test that shows the enemy health has changed.

import random

partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
    }
}

#Enemy Dictionary goes here

enemyDict = {
    "Zombo" : {
        "Damage" : 15,
        "Health" : 15,
        "AC" : 6,
    },
    "Bogo": {
        "Damage" : 5,
        "Health" : 12,
        "AC" : 17,
    },
    "Trogo": {
        "Damage" : 12,
        "Health" :  16,
        "AC" : 15,
    },
    "Thrag": {
        "Damage" : 22,
        "Health" : 18,
        "AC" : 13,
    },
    "Drackon": {
        "Damage" : 30,
        "Health" : 35,
        "AC" : 18,
    }
}

#Test the damage here by subtracting a party member's damage from the enemy's health.

randomEncounters =   ("Zombo", "Bogo", "Trogo", "Thrag", "Drackon")
encounter = random.choice(randomEncounters)
print("You have enountered a wild", encounter)
print("Which party member do you want to send forward")
partyMember = input("[LaeZel] [Shadowheart] [Gale] [Astarion] : ")
print(partyMember)
playerHealth = partyDictionary[partyMember]["Health"]
playerDamage = partyDictionary[partyMember]["Health"]
playerAc = partyDictionary[partyMember]["AC"]
if partyMember != "LaeZel":
    if partyMember != "Shadowheart":
        if partyMember != "Gale":
            if partyMember != "Astarion":
                partyMember = Unknown
                playerHealth = 10
                playerDamage = 10
                playerAc = 10
enemyHealth = enemyDict[encounter]["Health"]
enemyDamage = enemyDict[encounter]["Damage"]
enemyAc = enemyDict[encounter]["AC"]
print("[",partyMember,"]   [",encounter,"]")
print("[HP]",playerHealth,"    [HP]",enemyHealth)
print("[STR]",playerDamage,"   [STR]",enemyDamage)
print("[DEF]",playerAc,"  [DEF]",enemyAc)
print("")

acHit = random.randint(1, 20)
if acHit > enemyAc:
    print("Your party member attacks for", playerDamage, " damage")
    enemyHealth -= playerDamage
else:
    print("Your party member attacks for", playerDamage, " damage but it blocks")
print("")
print("[",partyMember,"]   [",encounter,"]")
print("[HP]",playerHealth,"    [HP]",enemyHealth)
print("[STR]",playerDamage,"   [STR]",enemyDamage)
print("[DEF]",playerAc,"  [DEF]",enemyAc)

