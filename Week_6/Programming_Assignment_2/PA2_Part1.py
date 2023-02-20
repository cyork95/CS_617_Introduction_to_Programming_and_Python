"""
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
The program should first ask for the number of years. The outer loop will iterate once for each year.
The inner loop will iterate twelve times, once for each month.
Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
After all iterations, the program should display the number of months, the total inches of rainfall,
and the average rainfall per month for the entire period.
"""

import statistics as s

number_of_years = int(input("Enter the number of years of rainfall you would like: "))
number_of_months = 12
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "November",
          "December"]
total_in_of_rainfall = 0
total_number_of_months = number_of_years * number_of_months
rainfall_per_month = []
i = 0

while i < number_of_years:
    i += 1
    j = 0
    while j < number_of_months - 1:
        in_of_rainfall_input = float(input("Enter the inches of rainfall for year {} {}: ".format(i,months[j])))
        total_in_of_rainfall += in_of_rainfall_input
        rainfall_per_month.append(in_of_rainfall_input)
        j += 1


average_rainfall = s.mean(rainfall_per_month)

print("There were {} months of calculations. The total inches of rainfall is {}in. and the average rainfall over the "
      "period is {}in.".format(total_number_of_months, total_in_of_rainfall, average_rainfall))
