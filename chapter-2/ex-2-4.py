# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.
item_1= input("What is the first items price?")
item_1= float(item_1)

item_2= input("What is the second items price?")
item_2= float(item_2)

item_3= input("What is the thrid items pridce?")
item_3= float(item_3)

item_4= input("What is the fourth items price?")
item_4= float(item_4)

item_5= input("What is the fifth items price?")
item_5= float(item_5)

# Constant for the sales tax rate.
SALES_TAX= .07
SALES_TAX= float(SALES_TAX)

# Get the price of each item by prompting the user.
# You will need to convert each input to a float.

# Calculate the subtotal by adding up the item prices.
subtotal=(item_1+ item_2+ item_3+ item_4+ item_5)
subtotal= float(subtotal)
# Calculate the sales tax by multiplying the subtotal by the tax rate.
sales_tax= (subtotal* SALES_TAX)
sales_tax= float(sales_tax)
subtotal_including_tax= (subtotal + sales_tax)
subtotal_including_tax= float(subtotal_including_tax)
# Calculate the total by adding the subtotal and tax.


# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 
print("The subtotal is", subtotal)
print("The sales tax is", sales_tax)
print("The total including tax is", subtotal_including_tax)




