print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give?"))
people=int(input("How many people t split the bill?"))
calculation_1= tip / 100
calculation_2= calculation_1 * bill
calculation_3= calculation_2 + bill
calculation_4= calculation_3 / people
nigga=round(calculation_4, 3)
print(f"Each person should pay: ${nigga}")