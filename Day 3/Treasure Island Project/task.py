import random

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = True
while True:
    choice1 = input("There is a crossroad in front of you.\n       Do you choose \"Right\" or \"Left\"?\n").lower()
    if choice1 == "left":
        left = input("You spot a castle but its across a huge river, What will you do?\n\"Try to Swim across\" or \"Go Back\"\n       Type \"S\" to Swim or \"B\" to go back.\n ").lower()
        if left == "s":
            swim = input("The force of the river is too strong, Its taking you away.\n       \"L\" to Accept you fate or \"P\" to pray to GOD\n").lower()
            if swim == "l":
                choice = False
                break
            else:
                if random.random() < 0.3:
                    continue
                else:
                    choice = False
                    break
    elif choice1 == "right":
        right = input("There is a strange guy sitting under a tree.\n       \"A\" to \"Approach him\" or \"B\" to \"Go Back\"\n").lower()
        if right == "a":
            approach = input("The guy stares at you and asks you for a body part.\n       \"E\" to give him your \"Eyes\" or \"F\" to give him your \"fingers\" or \"A\" to give him an \"Arm\" or \"N\" to refuse him.\n").lower()
            if approach == "f":
                break
        else:
            print("*He smirks* You lost memory and You go back to the start. Restarting\n")
            continue
if not choice:
        print("\"GAME OVER\"\nYou got swept away by the river")
elif choice:
    boat = input("He gives you a boat\n     Press \"W\" to continue\n").lower()
    choices = True
    if boat == "w":
        choice2 = input("There are three doors in front of you. Red, Green, and Blue, Make a choice.\n       \"R\" or \"G\" or \"B\"\n").lower()
        if choice2 == "r":
            print("You Fall into the deepest pits of Lava.")
            choices = False
        elif choice2 == "g":
            print("You got the Treasure!!!\n\"HOORAH!!!\"")
        elif choice2 == "b":
            print("You fell into a sea full of Sharks, Ouch!")
            choices = False
        if not choices:
            print("\"GAME OVER\"")
        if choices:
            print("\"Thanks for playing\"")

