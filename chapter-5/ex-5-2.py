# Programming Exercise 5-2
#
# Program to calculate final purchase details.
# This program takes a purchase amount from a user,
# then calculates state tax, county tax and total tax,
# 	and passes them to a function to be totaled
# and displayed



# Global constants for the state and county tax rates
STATE_SALES_TAX = .05
COUNTY_SALES_TAX = .01

# define the main function
def main():
     STATE_SALES_TAX = .05
     COUNTY_SALES_TAX = .01
     purchase= input("What is your total purchase:")
     purchase= float(purchase)
     state_tax= purchase* STATE_SALES_TAX
     county_tax= purchase*COUNTY_SALES_TAX
     total_tax= state_tax + county_tax
     total_sale= purchase + total_tax
     results(purchase, total_tax, total_sale, state_tax, county_tax)

    # Define local float variables for purchase, state tax and county tax
    # Get the purchase amount from the user
    # Calculate the state tax using the global constant for state tax rate
    # Calculate the county tax using the global constant for county tax rate
    # Call the sale details function, passing the purchase, state tax and county tax

#I DIDN'T DO THIS CORRECTLY

# define a function to display purchase details
# this function accepts purchase, stateTax, and countyTax as arguments,
# calculates the total tax and sale total,
# then displays the purchase details
def results(purchase, total_tax, total_sale, state_tax, county_tax):
     print("Your total tax is", format(total_tax, '.2f'))
     print("Your total sale is", format(total_sale, '.2f'))
     print("Your purchase is", format(purchase, '.2f'))
     print("The county tax is", format(county_tax, '.2f'))
    
    # Define local float variables for total tax and sale total
	# Calculate the total tax
	# Calculate the total sale
    # Display the purchase details, including purchase, state tax, county tax,
    #	total tax, and sale total, each on a line.  Format floats to 2 decimal places.

main()



# Call the main function to start the program.

