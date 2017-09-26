# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats
STATE_TAX= .01
STATE_TAX= float(STATE_TAX)

COUNTY_TAX= .02
COUNTY_TAX= float(COUNTY_TAX)

amount_purchase= input("What is the amount that you purchased:")
amount_purchase= float(amount_purchase)

total_sale= 0.0
total_sale= float(total_sale)

total_tax= 0.0
total_tax= float(total_tax)
# Constants for the state and county tax rates


# Get the amount of purchase from the user, casting it to a float.


# Calculate the state sales tax.
state_sales_tax= (STATE_TAX* amount_purchase)

# Calculate the county sales tax.
county_sales_tax= (COUNTY_TAX* amount_purchase)

# Sum the total tax.
total_tax= (state_sales_tax + county_sales_tax)

# Calculate the total of the sale.
total_sale= (total_tax + amount_purchase)

# Print detailed information about the sale, formatting all values to two decimal places.
print(state_sales_tax, "is the state sales tax")
print(county_sales_tax, "is the county sales tax")
print(total_tax, "is the total sales tax")
print(total_sale,"is the total sale")

