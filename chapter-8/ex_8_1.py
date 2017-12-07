# Programming Exercise 8-1
#
# Program to extract initials from a person's name.
# This program prompts a user for his or her full name,
# Splits the name into a list of parts and extracts the first character from each,
# and displays the characters in upper case, followed by periods.

# Define the main function
def main():
    
    # Get a full name as user input
    name = input("Enter your first and last name: ")

    # Split the string on spaces into a list of name parts and assign to a variable
    name_s = name.split(" ")
    # iterate over each name part in the list
    name_s_zero = name_s[0]
    name_s_zero = name_s_zero.replace(name_s_zero[0], name_s_zero[0].upper())
    name_s_one = name_s[1]
    name_s_one = name_s_one.replace(name_s_one[0], name_s_one[0].upper())
    print(name_s_zero, name_s_one)    
        # display the first character ( parts[0] ) of the name part as upper case

# Call the main function.
main()



#SCRATCH/ SCRATCH/ SCRATCH
s = "Hello World"
index= s.index("World")

number = [1,2,3,4]
numbers[0] = 9
#S[6] = "p" NOT LEGAL
c= s[index:11]
