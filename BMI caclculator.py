# BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"
# Refer to this graphic for help:
weight=float(input("Enter your weight: "))
height=float(input("Enter your height: "))
bmi=weight/(height**2)
if bmi < 18.5:
    print("underweight")
elif bmi >=25 :
    print('overweight')
else:
    print("normal weight")

print(f"Your BMI is {round(bmi,2)}")
