#Name:Jax Byrge
#Class: 6th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)

class stats:
    def __init__(self,health,atkroll,atkmod,ac):
        self.health = health
        self.atkroll = atkroll
        self.atkmod = atkmod
        self.ac = ac
#party stats
warrior = stats(25,6,3,13)
thief = stats(18,6,2,11)
mage = stats(16,8,1,9)
#enemy stats
skeleton = stats(19,4,2,13)
goblin = stats(15,6,1,12)
witch = stats(18,10,1,8)
#damage roll def
damage = 0
def damageroll(attacker,target):
    global damage
    randomX = random.randint(1,20)
    if randomX > target.ac:
        damage = random.randint(1,attacker.atkroll)
        damage += attacker.atkmod
        target.health -= damage
        print(attacker,"has done",damage,"damage to",target)
damageroll(thief,skeleton)

