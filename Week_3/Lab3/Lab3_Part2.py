"""
    Letter Grade Calculator
"""

average_grade = float(input("Enter the average grade for the student: "))

if average_grade >= 90:
    print("The student has an A.")
elif average_grade >= 80:
    print("The student has a B.")
elif average_grade >= 70:
    print("The student has a C.")
elif average_grade >= 60:
    print("The student has a D.")
else:
    print("The student has an F.")
