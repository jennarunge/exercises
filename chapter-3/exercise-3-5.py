# Programming Exercise 3-5
#
# Program to convert a value in kilograms to Newtons, then check whether it is in range.
# This program will prompt a user for a mass in kilograms,
# convert it to Newtons and use constants to check if the weight is within range,
# then display the weight and a range message.



# Global constants for minimum, maximum and mass multiplier values
kilograms_per_newton= 9.81
minimum= 0.0


# Variables for weight and mass initialized as floats   


# Get mass from user and convert it to a float
kilograms= float(input("What is the mass in kilograms: "))

# Calculate weight using the mass multiplier constant
newtons= kilograms_per_newton* kilograms

# Display the weight
print(format(newtons, '.2f'))
# If weight > maximum or < than minimum display an appropriate message
if newtons< minimum:
    print("Weight is out of range")
else:
    print("Weight is in ranges")





