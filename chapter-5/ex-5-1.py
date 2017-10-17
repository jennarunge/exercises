# Programming Exercise 5-1
#
# Program to convert kilometers to miles.
# This program accepts a distance in kilometers from the user,
# passes it to a function, which calculates its value in miles
# and displays the result for the user.


# Global constant for the ratio of kilometers to miles
KM_PER_MILE= 1.60934
distance= 0.0

# define the main function
def main():
    print("Running program")
    distance = 0.0
    distance = float(input("Enter distance in kilometers:"))
    convert_km_to_miles(distance)
    
    # Define a local float variable to hold the distance in kilometers
    # Get distance in kilometers from the user
    # pass the distance in kilometers to a function to convert to miles

# define the function to convert to miles
# the function takes kilometers as an argument
# calculates the equivalent number of miles
# and prints the result

def convert_km_to_miles(distance_in_km):
    
    # Define a local float variable for miles
    distance_in_mi = 0.0
	# use the global conversion constant to compute miles    
    distance_in_mi = KM_PER_MILE* distance_in_km
    formatted_miles= format(distance_in_mi, '.2f')
    # print the results, formatting float values to 2 decimal places
    print("You have travled", formatted_miles, "miles")


# Call the main function to start the program

main()