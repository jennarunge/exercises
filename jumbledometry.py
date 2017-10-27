#Happy Death Day
#That was a good movie
from Geometry import circle 
from Geometry import rectangle


AREA_OF_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():

    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input("Which would you like to do: ")
        output = handle_choice(choice)
        print(output)
        
#I don't know why line 20 is wrong. It also was saying there was a syntax error in the display_menu earlier and nothing has changed

def display_menu():
    print(" MENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")

def handle_choice(choice):
     if choice == AREA_OF_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            return "The area is" + str(circle.area_of_a_circle(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            return"The area is" + str(rectangle.area(width,length))
        elif choice ==CIRCUMFERENCE_CHOICE:
            radius= float(input("Enter the circle's radius: "))
            return "The circumference is" + str(circle.circumference(radius))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            return "The perimeter is" + str(rectangle.perimeter(width,length))
        elif choice == QUIT_CHOICE:
            return "Exiting the program..."
        else:
            return "Error: Invalid selection."

main()


