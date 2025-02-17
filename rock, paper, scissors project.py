import random
rock=('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
paper=('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
scissors=('''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
game_images=[rock, paper, scissors]

user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
else:
    print("safe Exit")
computer_choice=random.randint(0,2)
print('computer_choice')
print(game_images[computer_choice])
if user_choice>=3 and user_choice<0:
    print("This is not valid")
elif user_choice== 0 and computer_choice==2:
    print('You Win')
elif computer_choice ==0 and user_choice==2:
    print("You Lose")
elif user_choice == 0 and computer_choice == 1:
    print('You lose')
elif computer_choice == 0 and user_choice == 1:
    print('You Win')
elif user_choice == 1 and computer_choice == 2:
    print("You Lose")
elif computer_choice == 1 and user-choice == 2:
    print("You Win")
else: #user_choice == computer_choice
    print("Match Draw")






































