#Random Password Generator Project
#Description: This is a simple password generator project that generates a random password based on the user's input.
#The user can input the number of letters, numbers, and symbols they want in their password.
import random
word=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol=['!','@','#','$','%','^','&','*']
print("Welcome to the PyPassword Generator! ")
letters=int(input("How many letters would you like in your password? " ))
symbol_1=int(input("How many symbols would you like? "))
number_1=int(input("How many numbers would you like? "))

password=[]
for x in range(1,letters+1):
    password.append(random.choice(word))
for x in range(1,symbol_1+1):
    password.append(random.choice(number))
for x in range(1,number_1+1):
    password.append(random.choice(symbol))
random.shuffle(password)
password=''.join(password)
print(f"Your password is: {password}")