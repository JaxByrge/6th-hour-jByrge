#Name:Jax Byrge
#Class: 6th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.

#2. Create a fourth attribute in the class called max_health that has the same values as health
class stats:
    def __init__(self,health,damage,speed):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.maxHealth = health
    def burn(self):
        for i in range(10):
            self.health -= random.randint(1,6)
        if self.health < 0:
            self.health = 0
    def heal(self):
        self.health += 30
        if self.health > self.maxHealth:
            self.health = self.maxHealth
#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
warrior = stats(100,20,30)
healer = stats(60,10,30)
thief = stats(50,30,40)
mage = stats(45,35,25)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
partyList = [warrior,healer,thief,mage]
partyPick = random.choice(partyList)
partyPick.burn()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
print("The party member's current health is ",partyPick.health)
partyPick.heal()
print("The party member's after the heal is ",partyPick.health)

