# Programming Exercise 3-4
#
# Program to convert a number from 1 to 10 to a Roman numeral.
# This program will accept an integer from 1 to 10 from the user
# and use it to choose an appropriate Roman numeral
# to display on the screen.

# Variables to hold a number and a numeral.
# initialize the number as an int and the numeral as a string.
number= int(input("What is a number bewteen one and ten: "))
numeral= "I"
numeral= str(numeral)
# Get number from user and convert it to an int


# Set numeral to a Roman numeral value based on the value of number
# use a set of if ... elif .... etc. statements.

if number == 1:
    print(numeral)
elif number == 2:
    print("II")
elif number == 3:
    print("III")
elif number == 4:
    print("IV")
elif number ==5:
    print("V")
elif number == 6:
    print("VI")
elif number == 7:
    print("VII")
elif number == 8:
    print("VIII")
elif number ==9:
    print("IX")
elif number == 10:
    print("X")
elif number >= 11:
    print("Error. Imput is too large")
# use a final else to display an error if number is out of range.


# display the numeral on the screen.






