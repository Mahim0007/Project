#Treasure Island Project
print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')
print("Welcome to the treasure island.")
print("Your mission is to find the treaure.")
direction=input("You're at a cross road. Where do you want to go?" 
                 'Type "left" or "right".').lower()
if direction == "left":
    work=input("'You've come to a lake. There is an island in the middle of the lake.\n" 'Type "wait" to wait for a boat. Type "swim" to swim across.\n'
               ''"What do you want? Swim or Wait? ").lower()
    if work=='wait':
        colour=input("You arrive at the island unharmed\n. There is a house with 3 doors.One red, one yellow and one blue\n. Which colour do you choose?")
        if colour=='red':
            print("It's a room full of fire. Game Over.")
        elif colour == 'blue':
            print('You enter a room of beasts. Game Over.')
        elif colour == 'yellow':
            print("You found the treasure! You Win!")
        else:
            print("Your colour doesn't exist. You lose.")

    else:
        print("You get attacked by an angry trout. Game Over.")


else :
    print("Game Over")


