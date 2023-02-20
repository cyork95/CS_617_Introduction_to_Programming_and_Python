"""
Define a function that computes the balance of a bank account with a given initial balance and interest rate,
after a given number of years. Assume interest is compounded yearly.

Future Balance = Initial Balance * (1 + interest rate) ^ years
"""


def calculate_balance(balance, interest, years):
    future_balance = balance * (1 + interest) ** years
    return future_balance


initial_balance = float(input("Enter your current bank balance: "))

interest_rate = float(input("Enter the interest rate: "))

number_of_years = int(input("Enter the number of years: "))

print("Your future balance in", number_of_years, "years is $", round(calculate_balance(initial_balance, interest_rate, number_of_years), 2))
