#Name:Jax Byrge
#Class: 6th Hour
#Assignment: Scenario8
import random
import time


#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)
damage = 0
class stats:
    def __init__(self,health,atkroll,atkmod,ac,name):
        self.health = health
        self.atkroll = atkroll
        self.atkmod = atkmod
        self.ac = ac
        self.name = name
#party stats
warrior = stats(25,6,3,12,"warrior")
thief = stats(18,6,2,9,"thief")
mage = stats(16,8,1,10,"mage")
partylist = [warrior,thief,mage]
#enemy stats
skeleton = stats(19,4,2,8,"skeleton")
goblin = stats(15,6,1,9,"goblin")
witch = stats(18,10,1,7,"witch")
enemylist = [skeleton,goblin,witch]
#damage roll def
def damageroll(attacker,target):
    global damage
    randomX = random.randint(1,20)
    if randomX > target.ac:
        damage = random.randint(1,attacker.atkroll)
        damage += attacker.atkmod
        target.health -= damage
    else:
        damage = 0
#enemy attack
def enemy_attack():
    try:
        enemyAttacker = random.choice(enemylist)
        try:
            partyTarget = random.choice(partylist)
            damageroll(enemyAttacker, partyTarget)
            if damage > 0:
                print(enemyAttacker.name, "has done", damage, "damage to", partyTarget.name)
            else:
                print(enemyAttacker.name, "missed the", partyTarget.name)
        except:
            enemy_attack()
    except:
        enemy_attack()
#party attack
def party_attack():
    partyAttacker = int(input("Which do you choose to attack the enemy 1(warrior) 2(thief) 3(mage): "))
    enemyTarget = int(input("Which do you attack 1(goblin) 2(skeleton) 3(witch): "))
    try:
        if enemyTarget == 2:
            enemyTarget = skeleton
        if enemyTarget == 1:
            enemyTarget = goblin
        if enemyTarget == 3:
            enemyTarget = witch
        try:
            if partyAttacker == 2:
                partyAttacker = thief
            if partyAttacker == 1:
                partyAttacker = warrior
            if partyAttacker == 3:
                partyAttacker = mage
            damageroll(partyAttacker, enemyTarget)
            if damage > 0:
                print(partyAttacker.name, "has done", damage, "damage to", enemyTarget.name)
            else:
                print(partyAttacker.name, "missed the", enemyTarget.name)
        except:
            print("That party member is dead")
    except:
        print("That enemy is dead")

#show healths
def show_healths():
    try:
        print("warrior health:",warrior.health)
    except:
        print("warrior is dead")
    try:
        print("thief health:", thief.health)
    except:
        print("thief is dead")
    try:
        print("mage health:", mage.health)
    except:
        print("mage is dead")
    try:
        print("skeleton health:", skeleton.health)
    except:
        print("skeleton is dead")
    try:
        print("goblin health:", goblin.health)
    except:
        print("goblin is dead")
    try:
        print("witch health:", witch.health)
    except:
        print("witch is dead")
#check if dead

def check_death():
    global warrior
    global thief
    global mage
    global skeleton
    global goblin
    global witch
    try:
        if warrior.health < 1:
            del warrior
            partylist.remove(warrior)
    except:
        print("")
    try:
        if thief.health < 1:
            del thief
            partylist.remove(thief)
    except:
        print("")
    try:
        if mage.health < 1:
            del mage
            partylist.remove(mage)
    except:
        print("")
    try:
        if skeleton.health < 1:
            del skeleton
            enemylist.remove(skeleton)
    except:
        print("")
    try:
        if goblin.health < 1:
            del goblin
            enemylist.remove(goblin)
    except:
        print("")
    try:
        if witch.health < 1:
            del witch
            enemylist.remove(witch)
    except:
        print("")

while True:
    check_death()
    show_healths()
    time.sleep(1)
    party_attack()
    time.sleep(2)
    enemy_attack()
    time.sleep(2)