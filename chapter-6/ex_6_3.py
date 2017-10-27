# Programming Exercise 6-3
#
# Program to open a file and display its contents with line numbers.
# This program prompts the user for a file name,
# reads the file until it ends
# then displays each line with its line number before closing the file.

# define the main function
def main():
    # Define local variables for line and filename (strings) and counter (int)
    line= ""
    file_name= ""
    counter= int(0)
    
    
    # Prompt the user for a file name
    file_name= input("Enter the file name: ")

    # Open the specified file for reading
    file = open(file_name, 'r')
    # use a for loop to loop through all the lines
    for line in file:
        # increment the counter
        counter +=1
        # print the current line number without carriage return
        print(counter, line.rstrip())
        # Strip the '\n' from the end of the line
        # display the line (should be on same line as line number)
        

    # Close file
    file.close


# Call the main function to start the program


main()