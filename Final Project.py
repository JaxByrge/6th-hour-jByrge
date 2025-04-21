import random
import time


#character class
class Character:
    def __init__(self,maxhp,hp,physDamage,specDamage,defense):
        self.maxhp = maxhp
        self.hp = hp
        self.physDamage = physDamage
        self.specDamage = specDamage
        self.defense = defense
player = Character(20,20,6,6,10)
#enemy class
class Enemy:
    def __init__(self,name,maxhp,hp,physDamage,specDamage,defense):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.physDamage = physDamage
        self.specDamage = specDamage
        self.defense = defense

enemySlot = 0
#list of enemies
slime = Enemy("Slime",15,15,4,6,10)
enemies = [slime]

#combat
#choose enemy
def chooseEnemy():
    global enemies
    global enemySlot
    enemyRandom = random.choice(enemies)
    enemySlot = enemyRandom
def showStats():
    global enemySlot
    print("Player HP:",player.hp,"/",player.maxhp)
    print(enemySlot.name,"HP:",enemySlot.hp,"/",enemySlot.maxhp)
def playerAction():
    try:
        action = int(input("(1) Strike (2) Spell:"))
    if action =
chooseEnemy()
showStats()