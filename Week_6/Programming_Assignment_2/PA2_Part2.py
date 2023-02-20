"""
A county collects property taxes on the assessment value of property, which is 60 percent of the property’s
actual value. For example, if an acre of land is valued at $10,000, its assessment value is $6,000.
The property tax is then 72¢ for each $100 of the assessment value. The tax for the acre assessed at $6,000
will be $43.20. Write a program that asks for the actual value of a piece of property and displays the assessment
value and property tax.
"""

import math

assessment_percent = 0.60
property_tax_rate = 0.72


def CalculateAssessment(value=10000.0):
    assessment_value = value * assessment_percent
    return assessment_value


def CalculatePropertyTax(value=6000.0):
    number_of_taxable_100 = math.floor(value/100)
    property_tax = property_tax_rate * number_of_taxable_100
    return round(property_tax, 2)


actual_value_of_property = float(input("Enter the actual value of the property: "))

assessment_value_of_property = CalculateAssessment(actual_value_of_property)

property_tax_total = CalculatePropertyTax(assessment_value_of_property)

print("For a property valued at ${}, you will have an assessment value of ${} and your property taxes will be ${}.".format(actual_value_of_property, assessment_value_of_property, property_tax_total))