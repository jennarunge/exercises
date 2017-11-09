#while valid number is between the min and max it is true

def main():
    valid_number = False
    while not valid_number:
        MIN= int(0)
        MAX= int(100)
        user_input= input("Enter a number between 0 and 100: ")
        try:
            user_input = int(user_input)
            if user_input > MAX or user_input < MIN:
               print("Sorry,",user_input, " isn't in the range")
            else:
                 valid_number = True
        except ValueError:
            print(user_input, "is not a valid number. Please try again")
            
    print("Thank you. Your number is", user_input)
main()
