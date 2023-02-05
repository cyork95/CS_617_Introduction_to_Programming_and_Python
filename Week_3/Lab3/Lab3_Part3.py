"""
    Employee Salary Calculator
"""

hours_worked = int(input("Enter the number of hours worked: "))
job_title = int(input("Enter the number corresponding to your title (1 - Tester, 2 - Developer, 3 - Manager): "))

if job_title == 1:
    salary = 35 * hours_worked
elif job_title == 2:
    salary = 50 * hours_worked
else:
    salary = 65 * hours_worked

print("Your salary is: ", salary)
