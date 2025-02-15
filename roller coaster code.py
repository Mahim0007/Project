print('Welcome to the roller coaster.')
height=int(input('What is your height'))
bill=0
if height >= 120:
     print("You can ride")
     age=int(input("What is your age?"))
     if age < 12:
          bill=5
          print("You have to pay 5$")
     elif age >=18:
          bill=8
          print('You have to pay 12$')
     else:
          bill=12
          print('You have to pay 7$')
     photo=input("IF you want photos then press Y or rathern than N")
     if photo == 'Y':
          bill=bill+3
          print(f"Your bill is {bill}")
     else:
          print('NO')
else:
     print("Invalid")