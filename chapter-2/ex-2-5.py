# Programming Exercise 2-5
#
# Program to calculate distances traveled over time at a speed.
# This program uses no input.
# It will calculate the distance traveled for 6, 10 and 15 hours at a constant speed,
# then display all the results on the screen.

# Variables to hold the three distances.
# be sure to initialize these as floats.
time_one= 6
time_two= 10
time_three= 15

# Constant for the speed.
speed= 65
#speed is in miles/hour
# Calculate the distance the car will travel in
# 6, 10, and 15 hours.
distance_one= time_one* speed
distance_two= time_two* speed
distance_three= time_three* speed

# Print the results for all calculations.
print(distance_one, "miles")
print(distance_two, "miles")
print(distance_three, "miles")


