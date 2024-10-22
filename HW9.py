#Name:
#Class: 6th Hour
#Assignment: HW9
from encodings.rot_13 import rot13_map

#1. Print Hello World!
print("Hello world")

#2. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg
while True:
    tempature = int(input("Whats the tempature: "))

    if tempature > 20:
        print("Its hot")
    elif tempature > 10:
        print("Its mild")
    else:
        print("Its cold")
    print("Thank you")