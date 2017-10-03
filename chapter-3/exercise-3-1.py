# Programming Exercise 3-1
#
# Program to display the name of a week day from its number.
# This program prompts a user for the number (1 to 7)
# and uses it to choose the name of a weekday
# to display on the screen.

# Variables to hold the day of the week and the name of the day.
# Be sure to initialize the day of the week to an int and the name as a string.
day_one=int(1)
day_two=int(2)
day_three= int(3)
day_four= int(4)
day_five= int(5)
day_six= int(6)
day_seven= int(7)
monday= str("Monday")
tuesday= str("Tuesday")
wednesday= str("Wednesday")
thursday= str("Thursday")
friday= str("Friday")
saturday= str("Saturday")
sunday= str("Sunday")

# Get the number for the day of the week.
# be sure to format the input as an int
day_of_week= input("Which day is it:")
day_of_week= int(day_of_week)
# Determine the value to assign to the day of the week.
# use a set of if ... elif ... etc. statements to test the day of the week value.
if day_of_week == day_one:
    print("The day of the week is", monday)
elif day_of_week == day_two:
    print("The day of the week is", tuesday)
elif day_of_week == day_three:
    print("The day of the week is", wednesday)
elif day_of_week == day_four:
    print("The day of the week is", thursday)
elif day_of_week == day_five:
    print("The day of the week is", friday)
elif day_of_week == day_six:
    print("The day of the weeek is", saturday)
elif day_of_week == day_seven:
    print("The day of the week is", sunday)
else:
    print("Error, the number is out of range")




# use the final else to display an error message if the number is out of range.


# display the name of the day on the screen.




