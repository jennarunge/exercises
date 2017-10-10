# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats


# Get length A from the user and convert it to a float
a_length = float(input("What is the length of A:"))

# Get width A from the user and convert it to a float
a_width = float(input("What is the width of A:"))

# Get length B from the user and convert it to a float
b_length = float(input("What is the length of B:"))

# Get width B from the user and convert it to a float
b_width = float(input("What is the width of B:"))

# Calculate area A
a_area = a_length * a_width
a_area = float(a_area)

# Calculate area B
b_area = b_length * b_width
b_area = float(b_area)

# Print each area, formatting the values to 2 decimal places
print(a_area)
print(b_area)
# if area A is greater, print "A is greater" message.
if a_area > b_area:
    print(" A is greater")
if a_area == b_area:
    print("A and B are equal")
if b_area > a_area:
    print(" B is greater")
# else if area B is greater, print "B is greater" message.

# else print "A and B are equal" message.

print("I didn't get it to round to two decimal places")