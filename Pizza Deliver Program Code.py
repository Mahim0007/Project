#Write a pizza delivery program
print('Welcome to the Python pizza Deliveries')
size=input("Which size do you want? S, M or L: ")
pepperoni=input("Do you want pepperoni in your pizza? Y or N: ")
extra_cheeze=input("Do you want extra size? Y or N: ")
bill=0
if size=='S':
    bill+=15
elif size == 'M':
    bill+=20
elif size == 'L':
    bill+=25
else:
    print('Your input is invalid')
if pepperoni =='Y':
    if size == 'S':
        bill+=2
    else:
        bill+=3
if extra_cheeze == 'Y':
    bill+=1
print(f"Your final bill is {bill}")
























