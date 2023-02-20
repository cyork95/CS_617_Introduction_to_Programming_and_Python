"""
Discount Calculator

A retailer offers discounts to customers based on the total cost of goods purchased:

Cost	Discount percentage
less than $20	no discount
From $20 to less than $50	5%
From $50 to less than $100	7%
More than $100	10%
Write a program that asks the user to enter the total cost of goods and then computes and displays the final cost
after applying the discount.

"""

cost = int(input("Enter the total of goods purchased: "))

if cost < 20:
    print("There will be no discount today. Your total is: $", cost)
elif 20 <= cost < 50:
    discount_5_percent_cost = cost - (cost * 0.05)
    print("There will be a 5% discount. Your total is: $", discount_5_percent_cost)
elif 50 <= cost < 100:
    discount_7_percent_cost = cost - (cost * 0.07)
    print("There will be a 7% discount. Your total is: $", discount_7_percent_cost)
else:
    discount_10_percent_cost = cost - (cost * 0.1)
    print("There will be a 10% discount. Your total is: $", discount_10_percent_cost)