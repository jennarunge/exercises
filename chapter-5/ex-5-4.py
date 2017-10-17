# Programming Exercise 5-4
#
# Program to compute monthly and annual auto expenses.
# This program prompts a user for several auto monthly expense amounts,
# then passes them to a function to total the values, annualize them,
# and display the details and totals on the screen.



# define the main function
    # Define local float variables for loan, insurance, gas, oil, tires and maintenance
    # Get the amount of the monthly loan payment from the user.
    # Get the amount of the monthly insurance from the user.
    # Get the amount of the monthly gas from the user.
    # Get the amount of the monthly oil from the user.
    # Get the amount for monthly tire wear from the users.
    # Get the amount for monthly maintenance from the user.
    # Call the function to summarize car expenses,
    # passing the loan, insurance, gas, oil, tires and maintenance as arguments.
def main():
    loan= float(input("What is your monthly loan payment: "))
    insurance= float(input("What is your monthly insurance payment: "))
    gas= float(input("How much do you spend on gasoline per month: "))
    oil= float(input("How much do you spend on oil monthly: "))
    tire_wear= float(input("What is your monthly tire wear: "))
    maintenance= float(input("How mush do you spend on maintenance per month: "))
    the_others(loan, insurance, gas, oil, tire_wear, maintenance)

# Define a function to summarize car expenses,
# it accepts loan, insurance, gas, oil, tires, and maintenance as arguments,
# calculates a monthly total and an annual total,
# and displays these totals.
    # Define local float variables for monthly total and annual total
    # calculate the monthly total
    # calculate the annual total
    # Print monthly and annual information, formatting float value to 2 decimal places.
# Call the main function to start the program

def the_others(loan, insurance, gas, oil, tire_wear, maintenance):
    monthly_total= loan + insurance + gas + oil + tire_wear + maintenance
    annual_total= monthly_total*12
    print("Your monthly expenses are ", format(monthly_total, '.2f'))
    print("Your annual expenses are ", format(annual_total, '.2f'))

main()