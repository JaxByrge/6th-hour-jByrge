#Name:Jax Byrge
#Class: 6th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
sportDict = {
    "wrestling" : {
        "ball" : False,
        "people" : 1,
    },
    "Football" : {
        "ball": True,
        "people": 11,
    },
    "Tennis": {
        "ball": False,
        "people": 1,
    },

}

#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def sportsSum():
    print(sportDict["wrestling"]["people"] + sportDict["Football"]["people"] + sportDict["Tennis"]["people"] )
#3. Call the function with arguments here
sportsSum()