"""
    BMI Calculator
"""

weight = int(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

BMI = weight * 703 / (height**2)

print("Your BMI is: ", BMI)

if 18.5 <= BMI <= 25.5:
    print("You are the optimal weight!")
elif BMI < 18.5:
    print("You are underweight!")
else:
    print("You are overweight!")
