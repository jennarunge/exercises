# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.

# Get the person's age.
# remember to convert the input to an int.
age= int(input("What is your age: "))

# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.
if age <= 3:
    print("Infant")
elif age <= 12:
    print("Child")
elif age < 18:
    print("Teenager")
elif age >= 110:
    print("Dead")
elif age >=18:
    print("Adult")



# display a message with the age category.



