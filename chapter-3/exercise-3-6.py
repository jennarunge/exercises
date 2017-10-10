# Programming Exercise 3-6
#
# Program to check if a date is 'magic' (day * month = year).
# This program takes a month, day and year from the user as integers,
# Checks to see if each is in range, then checks whether month * day = year,
# then displays an appropriate message depending on the result

# Variables for month, day, year and message
# initialize month, day and year as integers, message as a string


# Get month and cast it to int
month= int(input("What is the month?"))

# Get day and cast it to int
day= int(input("What is the day?"))

# Get year and cast it to int
year= int(input("What is the year?"))

# This problem can be solved with if-else logic by the reducing the problem domain
# if month input is out of range

	# set message to hold "invalid month" message
if month > 12:
    print("Invalid Month")
if day > 31:
    print("Day is out of range")
# else if day input is out of range

    # set message to hold "invalid day" message

# else if  year input is out of range (greater than 99 or less than 0)
if year > 99:
    print("Invalid Year")
elif year < 0:
    print("Invalid Year")
    # set message to hold "invalid year" message

# else 
print(" ", day, "/", month, "/", year)
    # set message to hold the date in 00/00/00 form
if day*month == year:
    print("is a magic date")
    # if day * month equals year, add " is a magic date" to message
elif day*month!= year:
    print("is not a magic number")
    # else add " is not a magic date" to message


# print message for the user


