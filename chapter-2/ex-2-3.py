# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as floats
tract_size=float(0)
acre_number=float(0)
# Constant for the number of square feet in an acre.
acre_sqaure_feet=43560
acre_sqaure_feet=float(acre_sqaure_feet)

# Get the square feet in the tract from the user.
# you will need to convert this input to a float
tract_size= input("What is the tract size in sqaure feet?")
tract_size= float(tract_size)
# Calculate the number of acres.
print(tract_size/acre_sqaure_feet)

# Print the number of acres.
# remember to format the acres to two decimal places





