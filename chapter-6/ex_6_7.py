def main():
    valid_number = False
    while not valid_number:
        user_input= ""
        user_input = input("Please enter a number:")
        try:
            float(user_input)
        except ValueError:
            print(user_input, "is not a valid number. Have you been in a math class? Ever?")
        else:
            valid_number = True
    print("Thank you. You are now competent. Your number is", user_input)    
    
    
main()