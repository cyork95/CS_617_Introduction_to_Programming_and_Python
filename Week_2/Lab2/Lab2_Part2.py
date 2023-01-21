"""
Write a program that calculated the total cost of dinner at a restaurant.
Prompt the user to enter the charge for the food.
Calculate the tip amount (18% of charge) and sales tax amount (9% of charge).
Display the total cost by adding the three amounts.
"""

cost_of_food = int(input("Enter the cost of the food: "))

tip_amount = cost_of_food * 0.18

sales_tax_amount = cost_of_food * 0.09

total_cost = cost_of_food + tip_amount + sales_tax_amount

print("The cost of the food was: ", cost_of_food, "\nThe tip amount is: ", tip_amount, "\nThe sales tax is: ",
      sales_tax_amount, "\nAnd the total cost of everything is: ", total_cost)
