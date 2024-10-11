#Name:
#Class: 6th Hour
#Assignment: Scenario 3
import random
#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4




#Party Dictionary Goes Here
partyDict = {
    "Warrior" : {
        "Hp" :  "30",
        "Ac" : "14",
        "Atk Mod" : 3,
        "Atk Roll" : 6,
    },
    "Mage" : {
        "Hp" :  "23",
        "Ac" : "10",
        "Atk Mod" : 0,
        "Atk Roll" : 10,
    },
    "Archer": {
        "Hp": "27",
        "Ac": "12",
        "Atk Mod" : 4,
        "Atk Roll" : 4,
    },
    "Rouge": {
        "Hp": "25",
        "Ac": "11",
        "Atk Mod" : 1,
        "Atk Roll" : 6,
    }
}


#Enemy Dictionary Goes Here

enemyDict = {
    "Necromancer": {
        "Hp": "40",
        "Ac": "12",
        "Atk Mod" : 0,
        "Atk Roll" : 10,
    },
    "Skeleton Archer": {
        "Hp": "27",
        "Ac": "10",
        "Atk Mod" : 4,
        "Atk Roll" : 4,
    },
    "Skeleton Warrior": {
        "Hp": "25",
        "Ac": "10",
        "Atk Mod" : 3,
        "Atk Roll" : 6,
    }
}


#Combat Code Goes Here
partyMemberOne = int(partyDict["Warrior"]["Hp"])
partyMemberTwo = int(partyDict["Mage"]["Hp"])
partyMemberThree = int(partyDict["Archer"]["Hp"])
partyMemberFour = int(partyDict["Rouge"]["Hp"])
enemyOne = int(enemyDict["Necromancer"]["Hp"])
enemyTwo = int(enemyDict["Skeleton Archer"]["Hp"])
enemyThree = int(enemyDict["Skeleton Warrior"]["Hp"])
partyList = ["Warrior","Mage","Archer","Rouge"]
while True:
    print("[Warrior",partyMemberOne,"/ 30] [Mage",partyMemberTwo,"/ 23] [Archer",partyMemberThree,"/ 27] [Rouge",partyMemberFour,"/ 25]")
    print("[Necromancer",enemyOne,"/ 40] [Skeleton Archer",enemyTwo,"/ 27] [Skeleton Warrior",enemyThree,"/ 25]")
    print("")
    #Rouge Attack
    if partyMemberFour > 0:
        attacking = input("Which enemy does your Rouge Attack: ")
        acRoll = random.randint(1, 20)
        if acRoll > int(enemyDict[attacking]["Ac"]):
            print("The Rouge attacks", attacking)
            if attacking == "Necromancer" :
                enemyOne -= (random.randint(1, partyDict["Rouge"]["Atk Roll"]) + partyDict["Rouge"]["Atk Mod"])
            if attacking == "Skeleton Archer":
                enemyTwo -= (random.randint(1, partyDict["Rouge"]["Atk Roll"]) + partyDict["Rouge"]["Atk Mod"])
            if attacking == "Skeleton Warrior":
                enemyThree -= (random.randint(1, partyDict["Rouge"]["Atk Roll"]) + partyDict["Rouge"]["Atk Mod"])
        else: print("Failed Ac Roll")
        print("")
    else:
        print("Rouge is dead")
    #Skelton Warrior
    if enemyThree > 0:
        attacking = random.choice(partyList)
        acRoll = random.randint(1, 20)
        if acRoll > int(partyDict[attacking]["Ac"]):
            print("The Skeleton Warrior attacks", attacking)
            if attacking == "Warrior" :
                partyMemberOne -= (random.randint(1, enemyDict["Skeleton Warrior"]["Atk Roll"]) + enemyDict["Skeleton Warrior"]["Atk Mod"])
            if attacking == "Archer" :
                partyMemberThree -= (random.randint(1, enemyDict["Skeleton Warrior"]["Atk Roll"]) + enemyDict["Skeleton Warrior"]["Atk Mod"])
            if attacking == "Mage" :
                partyMemberTwo -= (random.randint(1, enemyDict["Skeleton Warrior"]["Atk Roll"]) + enemyDict["Skeleton Warrior"]["Atk Mod"])
            if attacking == "Rouge" :
                partyMemberFour -= (random.randint(1, enemyDict["Skeleton Warrior"]["Atk Roll"]) + enemyDict["Skeleton Warrior"]["Atk Mod"])
        else: print("Skeleton Warrior Failed Ac Roll")
        print("")
    else:
        print("Skeleton Warrior is dead")
    #Archer Attack
    if partyMemberThree > 0:
        attacking = input("Which enemy does your Archer Attack: ")
        acRoll = random.randint(1, 20)
        if acRoll > int(enemyDict[attacking]["Ac"]):
            print("The Archer attacks", attacking)
            if attacking == "Necromancer" :
                enemyOne -= (random.randint(1, partyDict["Archer"]["Atk Roll"]) + partyDict["Archer"]["Atk Mod"])
            if attacking == "Skeleton Archer":
                enemyTwo -= (random.randint(1, partyDict["Archer"]["Atk Roll"]) + partyDict["Archer"]["Atk Mod"])
            if attacking == "Skeleton Warrior":
                enemyThree -= (random.randint(1, partyDict["Archer"]["Atk Roll"]) + partyDict["Archer"]["Atk Mod"])
        else: print("Failed Ac Roll")
        print("")
    else:
        print("Archer is dead")
    #Skelton Archer
    if enemyTwo > 0:
        attacking = random.choice(partyList)
        acRoll = random.randint(1, 20)
        if acRoll > int(partyDict[attacking]["Ac"]):
            print("The Skeleton Archer attacks", attacking)
            if attacking == "Warrior" :
                partyMemberOne -= (random.randint(1, enemyDict["Skeleton Archer"]["Atk Roll"]) + enemyDict["Skeleton Archer"]["Atk Mod"])
            if attacking == "Archer" :
                partyMemberThree -= (random.randint(1, enemyDict["Skeleton Archer"]["Atk Roll"]) + enemyDict["Skeleton Archer"]["Atk Mod"])
            if attacking == "Mage" :
                partyMemberTwo -= (random.randint(1, enemyDict["Skeleton Archer"]["Atk Roll"]) + enemyDict["Skeleton Archer"]["Atk Mod"])
            if attacking == "Rouge" :
                partyMemberFour -= (random.randint(1, enemyDict["Skeleton Archer"]["Atk Roll"]) + enemyDict["Skeleton Archer"]["Atk Mod"])
        else: print("Skeleton Warrior Failed Ac Roll")
        print("")
    else:
        print("Skeleton Archer is dead")
    #Mage Attack
    if partyMemberTwo > 0:
        attacking = input("Which enemy does your Mage Attack: ")
        acRoll = random.randint(1, 20)
        if acRoll > int(enemyDict[attacking]["Ac"]):
            print("The Mage attacks", attacking)
            if attacking == "Necromancer" :
                enemyOne -= (random.randint(1, partyDict["Mage"]["Atk Roll"]) + partyDict["Mage"]["Atk Mod"])
            if attacking == "Skeleton Archer":
                enemyTwo -= (random.randint(1, partyDict["Mage"]["Atk Roll"]) + partyDict["Mage"]["Atk Mod"])
            if attacking == "Skeleton Warrior":
                enemyThree -= (random.randint(1, partyDict["Mage"]["Atk Roll"]) + partyDict["Mage"]["Atk Mod"])
        else: print("Failed Ac Roll")
        print("")
    else:
        print("Mage is dead")
    #Necromancer
    if enemyOne > 0:
        attacking = random.choice(partyList)
        acRoll = random.randint(1, 20)
        if acRoll > int(partyDict[attacking]["Ac"]):
            print("The Necromancer attacks", attacking)
            if attacking == "Warrior" :
                partyMemberOne -= (random.randint(1, enemyDict["Necromancer"]["Atk Roll"]) + enemyDict["Necromancer"]["Atk Mod"])
            if attacking == "Archer" :
                partyMemberThree -= (random.randint(1, enemyDict["Necromancer"]["Atk Roll"]) + enemyDict["Necromancer"]["Atk Mod"])
            if attacking == "Mage" :
                partyMemberTwo -= (random.randint(1, enemyDict["Necromancer"]["Atk Roll"]) + enemyDict["Necromancer"]["Atk Mod"])
            if attacking == "Rouge" :
                partyMemberFour -= (random.randint(1, enemyDict["Necromancer"]["Atk Roll"]) + enemyDict["Necromancer"]["Atk Mod"])
        else: print("Necromancer Failed Ac Roll")
        print("")
        randomHeal = random.randint (1, 10)
        if randomHeal > 5:
            if enemyTwo < 15:
                enemyTwo += random.randint(1, 6)
                print("Necromancer Heals his skeleton Archer")
            if enemyThree < 15:
                enemyThree += random.randint(1, 6)
                print("Necromancer Heals his skeleton Warrior")
    else:
        print("Necromancer is dead")
    #Warrior Attack
    if partyMemberOne > 0:
        attacking = input("Which enemy does your Warrior Attack: ")
        acRoll = random.randint(1, 20)
        if acRoll > int(enemyDict[attacking]["Ac"]):
            print("The Warrior attacks", attacking)
            if attacking == "Necromancer" :
                enemyOne -= (random.randint(1, partyDict["Warrior"]["Atk Roll"]) + partyDict["Warrior"]["Atk Mod"])
            if attacking == "Skeleton Archer":
                enemyTwo -= (random.randint(1, partyDict["Warrior"]["Atk Roll"]) + partyDict["Warrior"]["Atk Mod"])
            if attacking == "Skeleton Warrior":
                enemyThree -= (random.randint(1, partyDict["Warrior"]["Atk Roll"]) + partyDict["Warrior"]["Atk Mod"])
        else: print("Failed Ac Roll")
        print("")
    else:
        print("Warrior is dead")

    #Win/Lose
    if enemyOne < 1 and enemyTwo < 1 and enemyThree < 1:
        print("You have defeated all your enemies")
        exit(0)
    if partyMemberOne < 1 and partyMemberTwo < 1 and partyMemberThree < 1 and partyMemberFour < 1:
        print("You have been defeated by your enemies")
        exit(0)